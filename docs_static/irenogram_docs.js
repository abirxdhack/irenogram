(function () {
    "use strict";

    const PERFORMANCE_OBSERVER = {
        start: performance.now(),
        metrics: {}
    };

    function recordMetric(name) {
        PERFORMANCE_OBSERVER.metrics[name] = performance.now() - PERFORMANCE_OBSERVER.start;
    }

    function applyStoredTheme() {
        const stored = localStorage.getItem("theme");
        const prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
        const theme = stored || (prefersDark ? "dark" : "light");
        document.body.setAttribute("data-theme", theme);
        localStorage.setItem("theme", theme);
        recordMetric("themeApplied");
    }

    function initThemeToggle() {
        document.querySelectorAll(".theme-toggle").forEach(function (btn) {
            btn.addEventListener("click", function (e) {
                e.stopImmediatePropagation();
                const current = document.body.getAttribute("data-theme") || "light";
                const next = current === "light" ? "dark" : "light";
                document.body.setAttribute("data-theme", next);
                localStorage.setItem("theme", next);
                
                const toggleBtn = e.target.closest(".theme-toggle");
                if (toggleBtn) {
                    toggleBtn.style.animation = "none";
                    setTimeout(() => {
                        toggleBtn.style.animation = "";
                    }, 10);
                }
            }, true);
        });
    }

    function streamTextToElement(element, text, speed = 15) {
        element.textContent = "";
        let index = 0;

        function typeNext() {
            if (index < text.length) {
                const char = text[index];
                if (char === "\n") {
                    element.appendChild(document.createElement("br"));
                } else {
                    element.textContent += char;
                }
                index++;
                setTimeout(typeNext, speed);
            }
        }

        typeNext();
    }

    /* ═══════════════════════════════════════════════
       IRENOGRAM LIVE SEARCH  –  full rewrite
       Sources  : sidebar nav tree  (all pages)
                  current-page headings + dt members
       Features : debounced fuzzy match, score ranking,
                  categorised results, text highlight,
                  keyboard nav, sessionStorage cache,
                  dark-mode, accessible
       ═══════════════════════════════════════════════ */

    /* ── helpers ───────────────────────────────────── */

    function escapeRe(s) {
        return s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
    }

    function highlight(text, query) {
        if (!query) return escapeHtml(text);
        const re = new RegExp("(" + escapeRe(query) + ")", "gi");
        return escapeHtml(text).replace(
            new RegExp("(" + escapeRe(escapeHtml(query)) + ")", "gi"),
            '<mark class="ire-hl">$1</mark>'
        );
    }

    function escapeHtml(s) {
        return String(s)
            .replace(/&/g, "&amp;")
            .replace(/</g, "&lt;")
            .replace(/>/g, "&gt;")
            .replace(/"/g, "&quot;");
    }

    function debounce(fn, ms) {
        let t;
        return function(...args) { clearTimeout(t); t = setTimeout(() => fn.apply(this, args), ms); };
    }

    /* ── tag pills ─────────────────────────────────── */

    const TAG_META = {
        method:   { label: "Method",  cls: "tag-method"  },
        type:     { label: "Type",    cls: "tag-type"    },
        enum:     { label: "Enum",    cls: "tag-enum"    },
        page:     { label: "Page",    cls: "tag-page"    },
        section:  { label: "Section", cls: "tag-section" },
        member:   { label: "Member",  cls: "tag-member"  },
    };

    function classifyUrl(url) {
        if (/\/api\/methods\//.test(url))      return "method";
        if (/\/api\/types\//.test(url))        return "type";
        if (/\/api\/enums\//.test(url))        return "enum";
        if (/\/api\/bound-methods\//.test(url)) return "method";
        return "page";
    }

    function tagPill(kind) {
        const m = TAG_META[kind] || TAG_META.page;
        return `<span class="ire-tag ${m.cls}">${m.label}</span>`;
    }

    /* ── index builders ─────────────────────────────── */

    // Nav-tree index: one entry per sidebar link  (cross-page)
    function buildNavIndex() {
        const CACHE_KEY = "ire-nav-index-v2";
        const cached = sessionStorage.getItem(CACHE_KEY);
        if (cached) {
            try { return JSON.parse(cached); } catch (_) {}
        }

        const entries = [];
        document.querySelectorAll(".sidebar-tree a.reference").forEach(a => {
            const title = a.textContent.trim();
            const url   = a.getAttribute("href");
            if (!title || !url || url.startsWith("http")) return;
            entries.push({
                title,
                url,
                kind: classifyUrl(url),
                searchText: title.toLowerCase(),
            });
        });

        sessionStorage.setItem(CACHE_KEY, JSON.stringify(entries));
        return entries;
    }

    // In-page index: headings + API member dt elements
    function buildPageIndex() {
        const entries = [];
        const base    = window.location.pathname;

        document.querySelectorAll("article h1, article h2, article h3").forEach(h => {
            const id    = h.id || h.querySelector("[id]")?.id;
            const title = h.textContent.trim().replace(/¶$/, "");
            if (!title) return;
            entries.push({
                title,
                url:        base + (id ? "#" + id : ""),
                kind:       "section",
                searchText: title.toLowerCase(),
            });
        });

        document.querySelectorAll("article dt[id]").forEach(dt => {
            const id    = dt.id;
            const title = dt.querySelector(".sig-name")?.textContent.trim()
                       || dt.textContent.trim().replace(/¶$/, "").split("(")[0].trim();
            if (!title || title.length > 80) return;
            entries.push({
                title,
                url:        base + "#" + id,
                kind:       "member",
                searchText: title.toLowerCase(),
            });
        });

        return entries;
    }

    /* ── scoring + search ───────────────────────────── */

    function scoreEntry(entry, q) {
        const s = entry.searchText;
        const ql = q.toLowerCase();
        if (s === ql)             return 100;
        if (s.startsWith(ql))    return 80;
        if (s.includes(ql))      return 60;
        // word-boundary partial
        const words = s.split(/[\s._-]+/);
        if (words.some(w => w.startsWith(ql))) return 40;
        if (words.some(w => w.includes(ql)))   return 20;
        return 0;
    }

    function runSearch(q, navIndex, pageIndex) {
        const ql = q.toLowerCase().trim();
        if (ql.length < 2) return { page: [], nav: [] };

        function rank(list) {
            return list
                .map(e => ({ entry: e, score: scoreEntry(e, ql) }))
                .filter(x => x.score > 0)
                .sort((a, b) => b.score - a.score);
        }

        const pageRanked = rank(pageIndex);
        const navRanked  = rank(navIndex);

        // De-duplicate nav vs page by url
        const pagePaths = new Set(pageRanked.map(x => x.entry.url));
        const navFiltered = navRanked.filter(x => !pagePaths.has(x.entry.url));

        return {
            page: pageRanked.slice(0, 4).map(x => x.entry),
            nav:  navFiltered.slice(0, 6).map(x => x.entry),
            total: pageRanked.length + navFiltered.length,
        };
    }

    /* ── dropdown DOM ───────────────────────────────── */

    function buildDropdown() {
        const el = document.createElement("div");
        el.className    = "ire-search-dropdown";
        el.id           = "ireSearchDropdown";
        el.setAttribute("role", "listbox");
        el.setAttribute("aria-label", "Search results");
        el.style.display = "none";
        return el;
    }

    function renderEntry(entry, q, idx) {
        const div = document.createElement("div");
        div.className = "ire-result-item";
        div.setAttribute("role", "option");
        div.setAttribute("data-idx", idx);
        div.setAttribute("data-url", entry.url);
        div.tabIndex = -1;

        div.innerHTML = `
            <div class="ire-result-row">
                <span class="ire-result-title">${highlight(entry.title, q)}</span>
                ${tagPill(entry.kind)}
            </div>`;

        return div;
    }

    function renderDropdown(dropdown, results, q, searchRoot) {
        dropdown.innerHTML = "";

        const { page, nav, total } = results;
        const hasResults = page.length + nav.length > 0;

        if (!hasResults) {
            dropdown.innerHTML = `
                <div class="ire-no-results">
                    <span class="ire-no-results-icon">⌕</span>
                    <span>No results for <strong>${escapeHtml(q)}</strong></span>
                </div>`;
            showDropdown(dropdown);
            return;
        }

        let idx = 0;

        if (page.length) {
            const sec = document.createElement("div");
            sec.className = "ire-section-header";
            sec.textContent = "On this page";
            dropdown.appendChild(sec);
            page.forEach(e => dropdown.appendChild(renderEntry(e, q, idx++)));
        }

        if (nav.length) {
            const sec = document.createElement("div");
            sec.className = "ire-section-header";
            sec.textContent = "Documentation";
            dropdown.appendChild(sec);
            nav.forEach(e => dropdown.appendChild(renderEntry(e, q, idx++)));
        }

        // Footer "see all"
        const searchHref = buildSearchUrl(q);
        const footer = document.createElement("a");
        footer.className = "ire-search-footer";
        footer.href      = searchHref;
        footer.innerHTML = `<span>See all results for <strong>${escapeHtml(q)}</strong></span><span class="ire-footer-arrow">→</span>`;
        dropdown.appendChild(footer);

        showDropdown(dropdown);
    }

    function buildSearchUrl(q) {
        // walk up from sidebar form to figure out search path
        const form = document.querySelector(".sidebar-search-container");
        const action = form ? form.getAttribute("action") : "/search/";
        return `${action}?q=${encodeURIComponent(q)}&check_keywords=yes&area=default`;
    }

    function showDropdown(dropdown) {
        dropdown.style.display = "block";
        dropdown.classList.remove("ire-dropdown-exit");
        dropdown.classList.add("ire-dropdown-enter");
    }

    function hideDropdown(dropdown) {
        if (dropdown.style.display === "none") return;
        dropdown.classList.remove("ire-dropdown-enter");
        dropdown.classList.add("ire-dropdown-exit");
        setTimeout(() => {
            dropdown.style.display = "none";
            dropdown.classList.remove("ire-dropdown-exit");
        }, 180);
    }

    /* ── keyboard navigation ────────────────────────── */

    function setupKeyboard(input, dropdown) {
        let active = -1;

        function items() {
            return Array.from(dropdown.querySelectorAll(".ire-result-item, .ire-search-footer"));
        }

        function activate(i) {
            const els = items();
            els.forEach(el => el.classList.remove("ire-active"));
            active = Math.max(-1, Math.min(i, els.length - 1));
            if (active >= 0) {
                els[active].classList.add("ire-active");
                els[active].scrollIntoView({ block: "nearest" });
            }
        }

        input.addEventListener("keydown", e => {
            if (dropdown.style.display === "none") return;

            switch (e.key) {
                case "ArrowDown":
                    e.preventDefault();
                    activate(active + 1);
                    break;
                case "ArrowUp":
                    e.preventDefault();
                    activate(active - 1);
                    break;
                case "Enter":
                    e.preventDefault();
                    if (active >= 0) {
                        const el = items()[active];
                        const url = el.dataset.url || el.getAttribute("href");
                        if (url) window.location.href = url;
                    } else {
                        // submit to full search
                        const form = document.querySelector(".sidebar-search-container");
                        if (form) form.submit();
                    }
                    break;
                case "Escape":
                    e.preventDefault();
                    hideDropdown(dropdown);
                    input.blur();
                    active = -1;
                    break;
            }
        });

        // reset active on new render
        dropdown.addEventListener("mouseenter", () => {
            items().forEach(el => el.classList.remove("ire-active"));
            active = -1;
        });

        return { reset: () => { active = -1; } };
    }

    /* ── click navigation on items ──────────────────── */

    function setupItemClicks(dropdown, input) {
        dropdown.addEventListener("click", e => {
            const item = e.target.closest(".ire-result-item");
            if (item) {
                const url = item.dataset.url;
                if (url) {
                    input.value = "";
                    hideDropdown(dropdown);
                    window.location.href = url;
                }
            }
        });
    }

    /* ── main init ──────────────────────────────────── */

    function initGlobalSearch() {
        const input = document.querySelector(".sidebar-search");
        if (!input) return;

        // Prevent default form submit when dropdown is open (let Enter handler take over)
        const form = input.closest("form");

        // Build dropdown
        const wrapper = document.createElement("div");
        wrapper.className = "ire-search-wrapper";
        input.parentNode.insertBefore(wrapper, input);
        wrapper.appendChild(input);

        const dropdown = buildDropdown();
        wrapper.appendChild(dropdown);

        // Build indices
        const navIndex  = buildNavIndex();
        const pageIndex = buildPageIndex();

        const { reset: kbReset } = setupKeyboard(input, dropdown);
        setupItemClicks(dropdown, input);

        // Live search on input
        const doSearch = debounce((q) => {
            if (q.length < 2) { hideDropdown(dropdown); return; }
            const results = runSearch(q, navIndex, pageIndex);
            renderDropdown(dropdown, results, q, wrapper);
            kbReset();
        }, 130);

        input.addEventListener("input", e => doSearch(e.target.value.trim()));

        // Show on focus if query already present
        input.addEventListener("focus", () => {
            if (input.value.trim().length >= 2) {
                doSearch(input.value.trim());
            }
        });

        // Close on outside click
        document.addEventListener("click", e => {
            if (!wrapper.contains(e.target)) {
                hideDropdown(dropdown);
            }
        }, true);

        // Prevent form submit if dropdown is showing
        if (form) {
            form.addEventListener("submit", e => {
                if (dropdown.style.display !== "none") {
                    e.preventDefault();
                    // navigate to full search instead
                    window.location.href = buildSearchUrl(input.value.trim());
                }
            });
        }
    }

    function fetchGitHubCounters() {
        const starsCountEl = document.getElementById("ire-stars-count");
        const usedByCountEl = document.getElementById("ire-usedby-count");

        if (!starsCountEl && !usedByCountEl) return;

        const cacheKey = "ire-github-cache";
        const cacheTime = localStorage.getItem(`${cacheKey}-time`);
        const now = Date.now();

        if (cacheTime && now - parseInt(cacheTime) < 3600000) {
            const cached = JSON.parse(localStorage.getItem(cacheKey));
            if (cached && starsCountEl) {
                starsCountEl.textContent = cached.stars;
                starsCountEl.style.animation = "pulse 0.6s ease-out";
            }
            if (cached && usedByCountEl) {
                usedByCountEl.textContent = cached.used;
                usedByCountEl.style.animation = "pulse 0.6s ease-out";
            }
            recordMetric("githubCountersCached");
            return;
        }

        fetch("https://api.github.com/repos/abirxdhack/irenogram", {
            headers: { "Accept": "application/vnd.github.v3+json" }
        })
            .then(function (r) {
                if (!r.ok) throw new Error("rate limited");
                return r.json();
            })
            .then(function (data) {
                const starsCount = data.stargazers_count ? data.stargazers_count.toLocaleString() : "—";
                const usedCount = data.network_count ? data.network_count.toLocaleString() : "—";

                if (starsCountEl) {
                    starsCountEl.textContent = starsCount;
                    starsCountEl.style.animation = "slideInRight 0.5s ease-out";
                }
                if (usedByCountEl) {
                    usedByCountEl.textContent = usedCount;
                    usedByCountEl.style.animation = "slideInRight 0.5s ease-out";
                }

                localStorage.setItem(cacheKey, JSON.stringify({
                    stars: starsCount,
                    used: usedCount
                }));
                localStorage.setItem(`${cacheKey}-time`, now.toString());
                recordMetric("githubCountersFetched");
            })
            .catch(function () {
                if (starsCountEl) starsCountEl.textContent = "—";
                if (usedByCountEl) usedByCountEl.textContent = "—";
            });
    }

    function highlightCurrentNav() {
        const path = window.location.pathname;
        document.querySelectorAll(".sidebar-tree a.reference").forEach(function (link) {
            const href = link.getAttribute("href");
            if (href && path.endsWith(href.replace(/^\.\//, "").replace(/^\.\.\//, ""))) {
                link.style.color = "var(--color-brand-content)";
                link.style.fontWeight = "600";
                link.style.animation = "slideInLeft 0.4s ease-out";
                const parent = link.closest("li");
                if (parent) {
                    parent.classList.add("current");
                    parent.style.animation = "fadeInUp 0.4s ease-out";
                }
            }
        });
        recordMetric("navHighlighted");
    }

    function addCopyFeedback() {
        document.addEventListener("click", function (e) {
            const btn = e.target.closest(".copybtn");
            if (btn) {
                const originalText = btn.innerHTML;
                const originalClass = btn.className;

                btn.innerHTML = "✓ Copied";
                btn.classList.add("copied");

                setTimeout(function () {
                    btn.innerHTML = originalText;
                    btn.className = originalClass;
                }, 2000);

                if (btn.closest(".highlight")) {
                    const codeBlock = btn.closest(".highlight").querySelector("pre");
                    if (codeBlock) {
                        navigator.clipboard.writeText(codeBlock.textContent).catch(() => {});
                    }
                }
            }
        });
    }

    function initSmoothScroll() {
        document.querySelectorAll('a[href^="#"]').forEach(function (a) {
            a.addEventListener("click", function (e) {
                const target = document.querySelector(this.getAttribute("href"));
                if (target) {
                    e.preventDefault();
                    target.scrollIntoView({ behavior: "smooth", block: "start" });
                    history.pushState(null, null, this.getAttribute("href"));

                    target.style.animation = "none";
                    setTimeout(() => {
                        target.style.animation = "glow 0.8s ease-out";
                    }, 10);
                }
            });
        });
    }

    function initBackToTop() {
        const btn = document.querySelector(".back-to-top");
        if (!btn) return;

        let ticking = false;

        window.addEventListener("scroll", function () {
            if (!ticking) {
                requestAnimationFrame(() => {
                    const visible = window.scrollY > 300;
                    btn.style.opacity = visible ? "1" : "0";
                    btn.style.pointerEvents = visible ? "auto" : "none";
                    ticking = false;
                });
                ticking = true;
            }
        }, { passive: true });

        btn.addEventListener("click", function (e) {
            e.preventDefault();
            window.scrollTo({ top: 0, behavior: "smooth" });
        });
    }

    function initTableEnhancements() {
        document.querySelectorAll("table.docutils").forEach(table => {
            table.style.animation = "fadeInUp 0.6s ease-out";

            const rows = table.querySelectorAll("tbody tr");
            rows.forEach((row, idx) => {
                row.style.animation = `fadeInUp ${0.05 * (idx + 1)}s ease-out`;
            });
        });
    }

    function initCodeBlockEnhancements() {
        document.querySelectorAll(".highlight").forEach((block, idx) => {
            block.style.animation = `fadeInUp ${0.1 * (idx + 1)}s ease-out`;
        });
    }

    function initIntersectionObserver() {
        if (!("IntersectionObserver" in window)) return;

        const observerOptions = {
            threshold: 0.1,
            rootMargin: "0px 0px -50px 0px"
        };

        const observer = new IntersectionObserver(entries => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.animation = "fadeInUp 0.6s ease-out";
                    observer.unobserve(entry.target);
                }
            });
        }, observerOptions);

        document.querySelectorAll("article p, article ul, article ol").forEach(el => {
            observer.observe(el);
        });
    }

    function initLazyLoading() {
        if (!("IntersectionObserver" in window)) return;

        const lazyImages = document.querySelectorAll("img[data-src]");
        const imageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.getAttribute("data-src");
                    img.removeAttribute("data-src");
                    img.style.animation = "fadeInUp 0.4s ease-out";
                    observer.unobserve(img);
                }
            });
        });

        lazyImages.forEach(img => imageObserver.observe(img));
    }

    function initReadingProgress() {
        const progressBar = document.createElement("div");
        progressBar.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            height: 3px;
            background: linear-gradient(90deg, #E04000, #f07040);
            z-index: 9999;
            transition: width 0.2s ease-out;
        `;
        document.body.appendChild(progressBar);

        window.addEventListener("scroll", () => {
            const docHeight = document.documentElement.scrollHeight - window.innerHeight;
            const scrolled = (window.scrollY / docHeight) * 100;
            progressBar.style.width = scrolled + "%";
        }, { passive: true });
    }

    function initPreloadLinks() {
        document.querySelectorAll("a[href]").forEach(link => {
            const href = link.getAttribute("href");
            if (href && href.startsWith("/") && !href.includes("javascript:")) {
                link.addEventListener("mouseenter", () => {
                    const preloadLink = document.createElement("link");
                    preloadLink.rel = "prefetch";
                    preloadLink.href = href;
                    document.head.appendChild(preloadLink);
                }, { once: true });
            }
        });
    }

    function initDarkModeTransition() {
        const themeToggle = document.querySelector(".theme-toggle");
        if (themeToggle) {
            themeToggle.addEventListener("click", () => {
                document.body.style.transition = "background-color 0.3s ease-out, color 0.3s ease-out";
                setTimeout(() => {
                    document.body.style.transition = "";
                }, 300);
            });
        }
    }

    function initHeaderStickyBehavior() {
        const header = document.querySelector("header");
        if (!header) return;

        let lastScrollY = 0;
        let scrollDirection = "down";

        window.addEventListener("scroll", () => {
            const currentScrollY = window.scrollY;
            scrollDirection = currentScrollY > lastScrollY ? "down" : "up";
            lastScrollY = currentScrollY;
        }, { passive: true });
    }

    applyStoredTheme();

    document.addEventListener("DOMContentLoaded", function () {
        initThemeToggle();
        fetchGitHubCounters();
        highlightCurrentNav();
        addCopyFeedback();
        initSmoothScroll();
        initBackToTop();
        initGlobalSearch();
        initTableEnhancements();
        initCodeBlockEnhancements();
        initIntersectionObserver();
        initLazyLoading();
        initReadingProgress();
        initPreloadLinks();
        initDarkModeTransition();
        initHeaderStickyBehavior();

        recordMetric("domReady");

        cleanupEnumDocumentation();

        if (window.performance && window.performance.measure) {
            try {
                performance.measure("irenogram-init", "navigationStart", undefined);
            } catch (e) {}
        }
    });

    function cleanupEnumDocumentation() {
        const article = document.querySelector('article[role="main"]');
        if (!article) return;

        const dts = article.querySelectorAll('dl dt');
        const dds = article.querySelectorAll('dl dd');
        
        dts.forEach((dt, idx) => {
            const text = dt.textContent.trim();
            if (text.includes('=') && text.includes('<class')) {
                const nameMatch = text.match(/^([A-Z_]+)\s*=/);
                if (nameMatch) {
                    dt.textContent = nameMatch[1];
                }
            }
        });

        const docinfos = article.querySelectorAll('div.docinfo, .field-list');
        docinfos.forEach(el => {
            if (el.textContent.includes('pyrogram.raw')) {
                el.style.display = 'none';
            }
        });
    }

    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", function () {
            recordMetric("contentLoaded");
        });
    }
})();
