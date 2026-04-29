(function () {
    "use strict";

    const PERFORMANCE_OBSERVER = {
        start: performance.now(),
        metrics: {}
    };

    function recordMetric(name) {
        PERFORMANCE_OBSERVER.metrics[name] = performance.now() - PERFORMANCE_OBSERVER.start;
    }

    function isSearchPage() {
        return !!document.getElementById("search-results")
            || /\/search\/?(\?|$)/.test(window.location.pathname);
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
                    setTimeout(function () {
                        toggleBtn.style.animation = "";
                    }, 10);
                }
            }, true);
        });
    }

    function getQueryParam(name) {
        try {
            const params = new URLSearchParams(window.location.search || window.location.hash.replace(/^#/, "?"));
            return params.get(name) || "";
        } catch (e) {
            return "";
        }
    }

    function getDocRoot() {
        const meta = document.querySelector("meta[name='docs_url_root']");
        if (meta && meta.content) return meta.content;
        const html = document.documentElement;
        return html.getAttribute("data-content_root") || "../";
    }

    function categorizeResult(href) {
        const url = (href || "").toLowerCase();
        if (url.includes("/api/methods/")) return { label: "Method", cls: "ire-rs-method", icon: "fa-bolt" };
        if (url.includes("/api/types/")) return { label: "Type", cls: "ire-rs-type", icon: "fa-cube" };
        if (url.includes("/api/enums/")) return { label: "Enum", cls: "ire-rs-enum", icon: "fa-list" };
        if (url.includes("/api/filters/")) return { label: "Filter", cls: "ire-rs-filter", icon: "fa-filter" };
        if (url.includes("/api/handlers/")) return { label: "Handler", cls: "ire-rs-handler", icon: "fa-plug" };
        if (url.includes("/api/decorators/")) return { label: "Decorator", cls: "ire-rs-deco", icon: "fa-at" };
        if (url.includes("/api/errors/")) return { label: "Error", cls: "ire-rs-error", icon: "fa-triangle-exclamation" };
        if (url.includes("/telegram/base/")) return { label: "Raw Base", cls: "ire-rs-raw", icon: "fa-layer-group" };
        if (url.includes("/telegram/types/")) return { label: "Raw Type", cls: "ire-rs-raw", icon: "fa-layer-group" };
        if (url.includes("/telegram/functions/")) return { label: "Raw Func", cls: "ire-rs-raw", icon: "fa-layer-group" };
        if (url.includes("/start/")) return { label: "Guide", cls: "ire-rs-guide", icon: "fa-book-open" };
        if (url.includes("/intro/")) return { label: "Intro", cls: "ire-rs-guide", icon: "fa-flag" };
        if (url.includes("/faq")) return { label: "FAQ", cls: "ire-rs-guide", icon: "fa-circle-question" };
        if (url.includes("/releases")) return { label: "Release", cls: "ire-rs-guide", icon: "fa-tag" };
        return { label: "Page", cls: "ire-rs-page", icon: "fa-file-lines" };
    }

    function highlightMatch(text, query) {
        if (!text || !query) return text || "";
        const tokens = query.split(/\s+/).filter(function (t) { return t.length > 1; });
        if (!tokens.length) return text;
        const escaped = tokens.map(function (t) {
            return t.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
        });
        const re = new RegExp("(" + escaped.join("|") + ")", "ig");
        return text.replace(re, '<mark class="ire-rs-mark">$1</mark>');
    }

    function buildSearchPageScaffold(query) {
        const article = document.querySelector('article[role="main"]');
        if (!article) return null;

        if (article.querySelector(".ire-search-page")) {
            return article.querySelector(".ire-search-page");
        }

        const wrap = document.createElement("div");
        wrap.className = "ire-search-page";
        wrap.innerHTML =
            '<header class="ire-search-hero">' +
                '<div class="ire-search-hero-inner">' +
                    '<div class="ire-search-badge"><i class="fa-solid fa-magnifying-glass"></i> Search</div>' +
                    '<h1 class="ire-search-title">Search the Irenogram docs</h1>' +
                    '<p class="ire-search-sub">Find methods, types, enums, filters, handlers, raw API and guides.</p>' +
                    '<form class="ire-search-form" method="get" action="">' +
                        '<i class="fa-solid fa-magnifying-glass ire-search-form-icon"></i>' +
                        '<input class="ire-search-input" type="search" name="q" autocomplete="off" spellcheck="false" placeholder="Try: send_message, InlineKeyboardButton, filters.text" />' +
                        '<input type="hidden" name="check_keywords" value="yes" />' +
                        '<input type="hidden" name="area" value="default" />' +
                        '<button type="submit" class="ire-search-submit">Search</button>' +
                    '</form>' +
                    '<div class="ire-search-status" role="status" aria-live="polite"></div>' +
                '</div>' +
            '</header>' +
            '<section class="ire-search-results-wrap" aria-label="Search results"></section>';

        const existing = document.getElementById("search-results");
        if (existing) {
            existing.classList.add("ire-rs-host");
            wrap.querySelector(".ire-search-results-wrap").appendChild(existing);
        } else {
            const host = document.createElement("div");
            host.id = "search-results";
            host.classList.add("ire-rs-host");
            wrap.querySelector(".ire-search-results-wrap").appendChild(host);
        }

        article.innerHTML = "";
        article.appendChild(wrap);

        const input = wrap.querySelector(".ire-search-input");
        if (query) input.value = query;

        return wrap;
    }

    function setSearchStatus(text, state) {
        const status = document.querySelector(".ire-search-status");
        if (!status) return;
        status.textContent = text || "";
        status.setAttribute("data-state", state || "");
    }

    function decorateSearchResults(query) {
        const host = document.getElementById("search-results");
        if (!host) return;

        const list = host.querySelector("ul.search, ul");
        if (!list) return;
        list.classList.add("ire-rs-list");

        list.querySelectorAll("li").forEach(function (li, idx) {
            if (li.dataset.ireDecorated === "1") return;
            li.dataset.ireDecorated = "1";

            const link = li.querySelector("a");
            const ctx = li.querySelector(".context, p");
            const href = link ? link.getAttribute("href") : "";
            const cat = categorizeResult(href);

            li.classList.add("ire-rs-item", cat.cls);
            li.style.animationDelay = (Math.min(idx, 30) * 40) + "ms";

            const titleHTML = link ? highlightMatch(link.textContent, query) : "";
            const ctxHTML = ctx ? highlightMatch(ctx.textContent, query) : "";
            const safeHref = href ? href : "#";

            const card = document.createElement("div");
            card.className = "ire-rs-card";
            card.innerHTML =
                '<div class="ire-rs-card-top">' +
                    '<span class="ire-rs-tag"><i class="fa-solid ' + cat.icon + '"></i> ' + cat.label + '</span>' +
                    '<span class="ire-rs-path" title="' + safeHref + '">' + safeHref + '</span>' +
                '</div>' +
                '<a class="ire-rs-title" href="' + safeHref + '">' + titleHTML + '</a>' +
                (ctxHTML ? '<p class="ire-rs-context">' + ctxHTML + '</p>' : "") +
                '<div class="ire-rs-card-bottom"><span class="ire-rs-cta">Open <i class="fa-solid fa-arrow-right"></i></span></div>';

            li.innerHTML = "";
            li.appendChild(card);
        });

        const total = list.querySelectorAll("li.ire-rs-item").length;
        if (total > 0) {
            setSearchStatus(total + " result" + (total === 1 ? "" : "s") + " for \u201C" + query + "\u201D", "ok");
        }
    }

    function observeSearchResults(query) {
        const host = document.getElementById("search-results");
        if (!host) return;

        decorateSearchResults(query);

        const mo = new MutationObserver(function () {
            decorateSearchResults(query);

            const summary = host.querySelector("p.search-summary, .search-summary");
            if (summary) {
                const text = summary.textContent.trim();
                if (text) setSearchStatus(text, "ok");
            }
            if (host.textContent.toLowerCase().indexOf("did not match any documents") !== -1) {
                setSearchStatus("No results matched \u201C" + query + "\u201D. Try different keywords.", "empty");
            }
        });
        mo.observe(host, { childList: true, subtree: true, characterData: true });
    }

    function runSphinxSearch(query) {
        if (typeof window.Search === "undefined") return false;
        try {
            if (typeof window.Search.init === "function") {
                window.Search.init();
            }
            if (query && typeof window.Search.performSearch === "function") {
                window.Search.performSearch(query);
            }
            return true;
        } catch (e) {
            return false;
        }
    }

    function initSearchPage() {
        if (!isSearchPage()) return;

        const query = getQueryParam("q") || "";
        buildSearchPageScaffold(query);

        if (query) {
            setSearchStatus("Searching for \u201C" + query + "\u201D \u2026", "loading");
        } else {
            setSearchStatus("Type a query and press Enter.", "idle");
        }

        observeSearchResults(query);

        let attempts = 0;
        const maxAttempts = 60;
        const timer = setInterval(function () {
            attempts++;
            const ok = runSphinxSearch(query);
            const indexReady = window.Search && window.Search._index;
            if ((ok && indexReady) || attempts >= maxAttempts) {
                clearInterval(timer);
                if (query && attempts >= maxAttempts && !indexReady) {
                    setSearchStatus("Search index could not be loaded. Reload the page.", "error");
                }
            }
        }, 150);

        const form = document.querySelector(".ire-search-form");
        if (form) {
            form.addEventListener("submit", function (e) {
                const input = form.querySelector(".ire-search-input");
                const v = input && input.value.trim();
                if (!v) {
                    e.preventDefault();
                    input && input.focus();
                }
            });
        }

        const sidebarForm = document.querySelector(".sidebar-search-container");
        if (sidebarForm) {
            sidebarForm.setAttribute("action", getDocRoot() + "search.html");
        }
    }

    function rewireSidebarSearch() {
        const sidebarForm = document.querySelector(".sidebar-search-container");
        if (!sidebarForm) return;
        const action = sidebarForm.getAttribute("action") || "";
        if (action === "" || action === "#") {
            sidebarForm.setAttribute("action", getDocRoot() + "search.html");
        }
    }

    function fetchGitHubCounters() {
        const starsCountEl = document.getElementById("ire-stars-count");
        const usedByCountEl = document.getElementById("ire-usedby-count");

        if (!starsCountEl && !usedByCountEl) return;

        const cacheKey = "ire-github-cache";
        const cacheTime = localStorage.getItem(cacheKey + "-time");
        const now = Date.now();

        if (cacheTime && now - parseInt(cacheTime) < 3600000) {
            try {
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
            } catch (e) {}
        }

        fetch("https://api.github.com/repos/abirxdhack/irenogram", {
            headers: { "Accept": "application/vnd.github.v3+json" }
        })
            .then(function (r) {
                if (!r.ok) throw new Error("rate limited");
                return r.json();
            })
            .then(function (data) {
                const starsCount = data.stargazers_count ? data.stargazers_count.toLocaleString() : "\u2014";
                const usedCount = data.network_count ? data.network_count.toLocaleString() : "\u2014";

                if (starsCountEl) {
                    starsCountEl.textContent = starsCount;
                    starsCountEl.style.animation = "slideInRight 0.5s ease-out";
                }
                if (usedByCountEl) {
                    usedByCountEl.textContent = usedCount;
                    usedByCountEl.style.animation = "slideInRight 0.5s ease-out";
                }

                localStorage.setItem(cacheKey, JSON.stringify({ stars: starsCount, used: usedCount }));
                localStorage.setItem(cacheKey + "-time", now.toString());
                recordMetric("githubCountersFetched");
            })
            .catch(function () {
                if (starsCountEl) starsCountEl.textContent = "\u2014";
                if (usedByCountEl) usedByCountEl.textContent = "\u2014";
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

                btn.innerHTML = "\u2713 Copied";
                btn.classList.add("copied");

                setTimeout(function () {
                    btn.innerHTML = originalText;
                    btn.className = originalClass;
                }, 2000);

                if (btn.closest(".highlight")) {
                    const codeBlock = btn.closest(".highlight").querySelector("pre");
                    if (codeBlock) {
                        navigator.clipboard.writeText(codeBlock.textContent).catch(function () {});
                    }
                }
            }
        });
    }

    function initSmoothScroll() {
        document.querySelectorAll('a[href^="#"]').forEach(function (a) {
            a.addEventListener("click", function (e) {
                const hash = this.getAttribute("href");
                if (!hash || hash === "#") return;
                const target = document.querySelector(hash);
                if (target) {
                    e.preventDefault();
                    target.scrollIntoView({ behavior: "smooth", block: "start" });
                    history.pushState(null, "", hash);

                    target.style.animation = "none";
                    setTimeout(function () {
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
                requestAnimationFrame(function () {
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
        document.querySelectorAll("table.docutils").forEach(function (table) {
            table.style.animation = "fadeInUp 0.6s ease-out";
            const rows = table.querySelectorAll("tbody tr");
            rows.forEach(function (row, idx) {
                row.style.animation = "fadeInUp " + (0.05 * (idx + 1)) + "s ease-out";
            });
        });
    }

    function initCodeBlockEnhancements() {
        document.querySelectorAll(".highlight").forEach(function (block, idx) {
            block.style.animation = "fadeInUp " + (0.1 * (idx + 1)) + "s ease-out";
        });
    }

    function initIntersectionObserver() {
        if (!("IntersectionObserver" in window)) return;
        if (isSearchPage()) return;

        const observerOptions = { threshold: 0.1, rootMargin: "0px 0px -50px 0px" };
        const observer = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    entry.target.style.animation = "fadeInUp 0.6s ease-out";
                    observer.unobserve(entry.target);
                }
            });
        }, observerOptions);

        document.querySelectorAll("article p, article ul, article ol").forEach(function (el) {
            observer.observe(el);
        });
    }

    function initLazyLoading() {
        if (!("IntersectionObserver" in window)) return;
        const lazyImages = document.querySelectorAll("img[data-src]");
        const imageObserver = new IntersectionObserver(function (entries, observer) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.getAttribute("data-src");
                    img.removeAttribute("data-src");
                    img.style.animation = "fadeInUp 0.4s ease-out";
                    observer.unobserve(img);
                }
            });
        });
        lazyImages.forEach(function (img) { imageObserver.observe(img); });
    }

    function initReadingProgress() {
        const progressBar = document.createElement("div");
        progressBar.className = "ire-reading-progress";
        document.body.appendChild(progressBar);

        window.addEventListener("scroll", function () {
            const docHeight = document.documentElement.scrollHeight - window.innerHeight;
            const scrolled = docHeight > 0 ? (window.scrollY / docHeight) * 100 : 0;
            progressBar.style.width = scrolled + "%";
        }, { passive: true });
    }

    function initPreloadLinks() {
        document.querySelectorAll("a[href]").forEach(function (link) {
            const href = link.getAttribute("href");
            if (href && href.startsWith("/") && !href.includes("javascript:")) {
                link.addEventListener("mouseenter", function () {
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
            themeToggle.addEventListener("click", function () {
                document.body.style.transition = "background-color 0.3s ease-out, color 0.3s ease-out";
                setTimeout(function () { document.body.style.transition = ""; }, 300);
            });
        }
    }

    function initHeaderStickyBehavior() {
        const header = document.querySelector("header");
        if (!header) return;
        let lastScrollY = 0;
        window.addEventListener("scroll", function () {
            const currentScrollY = window.scrollY;
            header.classList.toggle("ire-header-shrunk", currentScrollY > 80);
            lastScrollY = currentScrollY;
        }, { passive: true });
    }

    function cleanupEnumDocumentation() {
        if (isSearchPage()) return;
        const article = document.querySelector('article[role="main"]');
        if (!article) return;

        const dts = article.querySelectorAll('dl dt');
        dts.forEach(function (dt) {
            const text = dt.textContent.trim();
            if (text.includes('=') && text.includes('<class')) {
                const nameMatch = text.match(/^([A-Z_]+)\s*=/);
                if (nameMatch) {
                    dt.textContent = nameMatch[1];
                }
            }
        });

        const docinfos = article.querySelectorAll('div.docinfo, .field-list');
        docinfos.forEach(function (el) {
            if (el.textContent.includes('pyrogram.raw')) {
                el.style.display = 'none';
            }
        });
    }

    applyStoredTheme();

    document.addEventListener("DOMContentLoaded", function () {
        initThemeToggle();
        rewireSidebarSearch();
        initSearchPage();
        fetchGitHubCounters();
        highlightCurrentNav();
        addCopyFeedback();
        initSmoothScroll();
        initBackToTop();
        initTableEnhancements();
        initCodeBlockEnhancements();
        initIntersectionObserver();
        initLazyLoading();
        initReadingProgress();
        initPreloadLinks();
        initDarkModeTransition();
        initHeaderStickyBehavior();
        cleanupEnumDocumentation();

        recordMetric("domReady");
    });
})();
