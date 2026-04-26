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

    function createSearchIndex() {
        const index = {};
        const contentElements = document.querySelectorAll("h1, h2, h3, p, dt");

        contentElements.forEach((el, idx) => {
            const text = el.textContent.toLowerCase();
            const words = text.split(/\s+/).filter(w => w.length > 2);
            const id = el.id || `content-${idx}`;

            words.forEach(word => {
                if (!index[word]) {
                    index[word] = [];
                }
                if (!index[word].find(item => item.id === id)) {
                    index[word].push({
                        id,
                        text: el.textContent.substring(0, 100),
                        element: el,
                        type: el.tagName.toLowerCase(),
                        relevance: el.tagName === "H1" ? 10 : el.tagName === "H2" ? 7 : 5
                    });
                }
            });
        });

        return index;
    }

    function fuzzySearch(query, index) {
        if (!query || query.length < 2) return [];

        const results = [];
        const queryWords = query.toLowerCase().split(/\s+/).filter(w => w.length > 0);
        const seen = new Set();

        queryWords.forEach(word => {
            Object.keys(index).forEach(indexWord => {
                if (indexWord.includes(word) || word.includes(indexWord.substring(0, 3))) {
                    index[indexWord].forEach(item => {
                        if (!seen.has(item.id)) {
                            results.push({
                                ...item,
                                score: word === indexWord ? item.relevance * 2 : item.relevance
                            });
                            seen.add(item.id);
                        }
                    });
                }
            });
        });

        return results.sort((a, b) => b.score - a.score).slice(0, 8);
    }

    let searchIndex = null;

    function initGlobalSearch() {
        const searchInput = document.getElementById("globalSearch") || 
                           document.querySelector(".search-input");
        const searchResults = document.getElementById("searchResults") || 
                             document.querySelector(".search-results-dropdown");

        if (!searchInput) return;

        if (!searchIndex) {
            searchIndex = createSearchIndex();
        }

        searchInput.addEventListener("input", function (e) {
            const query = e.target.value;

            if (searchResults) {
                if (query.length < 2) {
                    searchResults.innerHTML = "";
                    searchResults.style.display = "none";
                    return;
                }

                const results = fuzzySearch(query, searchIndex);

                if (results.length === 0) {
                    searchResults.innerHTML = '<div style="padding: 12px; text-align: center; color: #999;">No results found</div>';
                } else {
                    searchResults.innerHTML = results.map((result, idx) => `
                        <div class="search-result-item" style="padding: 12px; border-bottom: 1px solid #eee; cursor: pointer; transition: background 0.2s; animation: fadeInUp ${0.1 * (idx + 1)}s ease-out;" onclick="document.getElementById('globalSearch').value = ''; this.closest('.search-results-dropdown').style.display = 'none'; document.querySelector('[id=\\"${result.id}\\"]')?.scrollIntoView({behavior: 'smooth', block: 'start'});">
                            <div style="font-weight: 600; font-size: 0.9em; color: #E04000;">${result.type.toUpperCase()}</div>
                            <div style="margin-top: 4px; font-size: 0.85em; color: #666;">${result.text}...</div>
                        </div>
                    `).join("");
                }

                searchResults.style.display = "block";
                searchResults.style.animation = "fadeInUp 0.3s ease-out";
            }
        });

        document.addEventListener("click", function (e) {
            if (searchResults && !searchInput.contains(e.target) && !searchResults.contains(e.target)) {
                searchResults.style.display = "none";
            }
        });

        searchInput.addEventListener("focus", function () {
            if (this.value.length > 1 && searchResults) {
                searchResults.style.display = "block";
            }
        });
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