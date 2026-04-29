(function () {
    "use strict";

    const state = {
        query: "",
        requested: false,
        decorated: false,
        attempts: 0,
        observer: null
    };

    function ready(fn) {
        if (document.readyState === "loading") {
            document.addEventListener("DOMContentLoaded", fn, { once: true });
            return;
        }

        fn();
    }

    function isSearchPage() {
        return Boolean(document.getElementById("search-results"))
            || /\/search\/?(?:index\.html|search\.html)?(?:[?#]|$)/.test(window.location.pathname)
            || /\/search\.html(?:[?#]|$)/.test(window.location.pathname);
    }

    function safeHTML(value) {
        return String(value || "").replace(/[&<>"']/g, function (char) {
            return {
                "&": "&amp;",
                "<": "&lt;",
                ">": "&gt;",
                "\"": "&quot;",
                "'": "&#39;"
            }[char];
        });
    }

    function cleanText(value) {
        return String(value || "").replace(/\s+/g, " ").trim();
    }

    function getDocRoot() {
        const meta = document.querySelector("meta[name='docs_url_root']");

        if (meta && meta.content) {
            return meta.content;
        }

        return document.documentElement.getAttribute("data-content_root") || "../";
    }

    function getSearchAction() {
        const root = getDocRoot();

        if (root.endsWith("/")) {
            return root + "search/";
        }

        return root + "/search/";
    }

    function getQuery() {
        const sources = [];

        if (window.location.search) {
            sources.push(window.location.search);
        }

        if (window.location.hash) {
            sources.push(window.location.hash.replace(/^#\??/, "?"));
        }

        for (const source of sources) {
            try {
                const params = new URLSearchParams(source);
                const value = params.get("q");

                if (value && value.trim()) {
                    return value.trim();
                }
            } catch (error) {}
        }

        const input = document.querySelector("input[name='q'], input[type='search'], #searchbox input");

        if (input && input.value) {
            return input.value.trim();
        }

        return "";
    }

    function applyStoredTheme() {
        const stored = localStorage.getItem("theme");
        const prefersDark = window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches;
        const theme = stored || (prefersDark ? "dark" : "light");

        document.body.setAttribute("data-theme", theme);
        localStorage.setItem("theme", theme);
    }

    function initThemeToggle() {
        document.querySelectorAll(".theme-toggle").forEach(function (button) {
            button.addEventListener("click", function (event) {
                event.stopImmediatePropagation();

                const current = document.body.getAttribute("data-theme") || "light";
                const next = current === "light" ? "dark" : "light";

                document.body.setAttribute("data-theme", next);
                localStorage.setItem("theme", next);

                button.style.animation = "none";

                setTimeout(function () {
                    button.style.animation = "";
                }, 10);
            }, true);
        });
    }

    function rewireSearchForms() {
        document.querySelectorAll(".sidebar-search-container, #searchbox form, form.search, form[role='search']").forEach(function (form) {
            if (!form || form.tagName !== "FORM") {
                return;
            }

            form.setAttribute("method", "get");
            form.setAttribute("action", getSearchAction());

            const input = form.querySelector("input[type='search'], input[name='q'], input");

            if (input) {
                input.setAttribute("name", "q");
            }
        });
    }

    function categorizeResult(href, title, context) {
        const text = [href, title, context].join(" ").toLowerCase();

        if (text.includes("inlinekeyboard") || text.includes("keyboardbutton") || text.includes("replykeyboard")) {
            return { label: "Keyboard", cls: "ire-rs-keyboard", icon: "fa-keyboard" };
        }

        if (text.includes("/api/methods/") || /\.[a-z_]+\(/i.test(title || "")) {
            return { label: "Method", cls: "ire-rs-method", icon: "fa-bolt" };
        }

        if (text.includes("/api/types/") || text.includes("pyrogram.types")) {
            return { label: "Type", cls: "ire-rs-type", icon: "fa-cube" };
        }

        if (text.includes("/api/enums/") || text.includes("pyrogram.enums")) {
            return { label: "Enum", cls: "ire-rs-enum", icon: "fa-list" };
        }

        if (text.includes("/api/filters/") || text.includes("filter")) {
            return { label: "Filter", cls: "ire-rs-filter", icon: "fa-filter" };
        }

        if (text.includes("/api/handlers/") || text.includes("handler")) {
            return { label: "Handler", cls: "ire-rs-handler", icon: "fa-plug" };
        }

        if (text.includes("/api/decorators/") || text.includes("decorator")) {
            return { label: "Decorator", cls: "ire-rs-deco", icon: "fa-at" };
        }

        if (text.includes("/api/errors/") || text.includes("error")) {
            return { label: "Error", cls: "ire-rs-error", icon: "fa-triangle-exclamation" };
        }

        if (text.includes("/telegram/base/")) {
            return { label: "Raw Base", cls: "ire-rs-raw", icon: "fa-layer-group" };
        }

        if (text.includes("/telegram/types/")) {
            return { label: "Raw Type", cls: "ire-rs-raw", icon: "fa-layer-group" };
        }

        if (text.includes("/telegram/functions/")) {
            return { label: "Raw Func", cls: "ire-rs-raw", icon: "fa-layer-group" };
        }

        if (text.includes("/start/") || text.includes("/intro/") || text.includes("guide")) {
            return { label: "Guide", cls: "ire-rs-guide", icon: "fa-book-open" };
        }

        if (text.includes("faq")) {
            return { label: "FAQ", cls: "ire-rs-guide", icon: "fa-circle-question" };
        }

        if (text.includes("release")) {
            return { label: "Release", cls: "ire-rs-guide", icon: "fa-tag" };
        }

        return { label: "Page", cls: "ire-rs-page", icon: "fa-file-lines" };
    }

    function highlight(text, query) {
        const safe = safeHTML(text);

        if (!query) {
            return safe;
        }

        const tokens = query
            .split(/\s+/)
            .map(function (token) {
                return token.trim();
            })
            .filter(function (token) {
                return token.length > 1;
            });

        if (!tokens.length) {
            return safe;
        }

        const escaped = tokens.map(function (token) {
            return token.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
        });

        const pattern = new RegExp("(" + escaped.join("|") + ")", "ig");

        return safe.replace(pattern, '<mark class="ire-rs-mark">$1</mark>');
    }

    function readablePath(href) {
        let value = String(href || "documentation");

        value = value.split("#")[0].split("?")[0];
        value = value.replace(/^(\.\.\/)+/, "");
        value = value.replace(/^\.\//, "");
        value = value.replace(/index\.html$/, "");
        value = value.replace(/\.html$/, "");
        value = value.replace(/\/$/, "");
        value = value.replace(/\//g, " / ");

        return value || "documentation";
    }

    function splitTitle(title) {
        const clean = cleanText(title).replace(/¶/g, "");
        const parts = clean.split(/\s+[–—-]\s+/);

        return {
            main: parts[0] || clean,
            detail: parts.slice(1).join(" — ")
        };
    }

    function getMainArticle() {
        return document.querySelector("article[role='main']")
            || document.querySelector("#furo-main-content")
            || document.querySelector("article")
            || document.querySelector("main")
            || document.body;
    }

    function buildSearchPage() {
        const article = getMainArticle();

        if (!article) {
            return null;
        }

        if (article.querySelector(".ire-search-page")) {
            return article.querySelector(".ire-search-page");
        }

        let host = document.getElementById("search-results");

        if (!host) {
            host = document.createElement("div");
            host.id = "search-results";
        }

        host.classList.add("ire-rs-host");

        const wrap = document.createElement("div");
        wrap.className = "ire-search-page";

        wrap.innerHTML =
            '<header class="ire-search-hero">' +
                '<div class="ire-search-hero-inner">' +
                    '<div class="ire-search-badge"><i class="fa-solid fa-magnifying-glass"></i> Search</div>' +
                    '<h1 class="ire-search-title">Search the Irenogram docs</h1>' +
                    '<p class="ire-search-sub">Find methods, types, enums, filters, handlers, raw API objects and guides.</p>' +
                    '<form class="ire-search-form" method="get" action="' + safeHTML(getSearchAction()) + '">' +
                        '<i class="fa-solid fa-magnifying-glass ire-search-form-icon"></i>' +
                        '<input class="ire-search-input" type="search" name="q" autocomplete="off" spellcheck="false" placeholder="Try: send_message, InlineKeyboardButton, filters.text">' +
                        '<input type="hidden" name="check_keywords" value="yes">' +
                        '<input type="hidden" name="area" value="default">' +
                        '<button type="submit" class="ire-search-submit">Search</button>' +
                    '</form>' +
                    '<div class="ire-search-status" role="status" aria-live="polite"></div>' +
                '</div>' +
            '</header>' +
            '<section class="ire-search-results-wrap" aria-label="Search results"></section>';

        wrap.querySelector(".ire-search-results-wrap").appendChild(host);
        article.replaceChildren(wrap);

        const input = wrap.querySelector(".ire-search-input");

        if (state.query && input) {
            input.value = state.query;
        }

        document.body.classList.add("ire-search-active");

        return wrap;
    }

    function setSearchStatus(text, mode) {
        const status = document.querySelector(".ire-search-status");

        if (!status) {
            return;
        }

        status.textContent = text || "";
        status.setAttribute("data-state", mode || "");
    }

    function decorateSearchResults() {
        const host = document.getElementById("search-results");

        if (!host) {
            return;
        }

        const text = cleanText(host.textContent).toLowerCase();

        if (text.includes("searching") && !host.querySelector("ul")) {
            host.classList.add("ire-rs-loading");
            setSearchStatus("Searching for “" + state.query + "” …", "loading");
            return;
        }

        host.classList.remove("ire-rs-loading");

        const list = host.querySelector("ul.search, ul");

        if (!list) {
            if (state.query && (text.includes("did not match") || text.includes("no results"))) {
                host.classList.add("ire-rs-empty");
                setSearchStatus("No results matched “" + state.query + "”. Try another keyword.", "empty");
            }

            return;
        }

        list.classList.add("ire-rs-list");
        host.classList.remove("ire-rs-empty");

        list.querySelectorAll("li").forEach(function (item, index) {
            if (item.dataset.ireDecorated === "1") {
                return;
            }

            const link = item.querySelector("a");
            const context = item.querySelector(".context, p");
            const href = link ? link.getAttribute("href") || "#" : "#";
            const rawTitle = link ? cleanText(link.textContent) : cleanText(item.textContent);
            const rawContext = context ? cleanText(context.textContent) : "";
            const title = splitTitle(rawTitle);
            const category = categorizeResult(href, rawTitle, rawContext);

            item.dataset.ireDecorated = "1";
            item.classList.add("ire-rs-item", category.cls);
            item.style.animationDelay = Math.min(index, 28) * 38 + "ms";

            const card = document.createElement("article");
            card.className = "ire-rs-card";

            card.innerHTML =
                '<div class="ire-rs-card-top">' +
                    '<span class="ire-rs-tag"><i class="fa-solid ' + category.icon + '"></i> ' + safeHTML(category.label) + '</span>' +
                    '<span class="ire-rs-path" title="' + safeHTML(href) + '">' + safeHTML(readablePath(href)) + '</span>' +
                '</div>' +
                '<a class="ire-rs-title" href="' + safeHTML(href) + '">' + highlight(title.main, state.query) + '</a>' +
                '<div class="ire-rs-detail">' + safeHTML(title.detail || "Matched documentation entry") + '</div>' +
                '<p class="ire-rs-context">' + highlight(rawContext || "Open this result in the generated Irenogram documentation.", state.query) + '</p>' +
                '<div class="ire-rs-card-bottom"><span class="ire-rs-cta">Open <i class="fa-solid fa-arrow-right"></i></span></div>';

            item.replaceChildren(card);

            item.addEventListener("click", function (event) {
                if (event.target.closest("a")) {
                    return;
                }

                window.location.href = href;
            });
        });

        const total = list.querySelectorAll("li.ire-rs-item").length;

        if (total > 0) {
            state.decorated = true;
            document.body.classList.add("ire-search-has-results");
            setSearchStatus(total + " result" + (total === 1 ? "" : "s") + " for “" + state.query + "”", "ok");
        }
    }

    function observeSearchResults() {
        const host = document.getElementById("search-results");

        if (!host) {
            return;
        }

        if (state.observer) {
            state.observer.disconnect();
        }

        state.observer = new MutationObserver(function () {
            window.requestAnimationFrame(decorateSearchResults);
        });

        state.observer.observe(host, {
            childList: true,
            subtree: true,
            characterData: true
        });
    }

    function runSphinxSearch() {
        if (!state.query) {
            return true;
        }

        if (typeof window.Search === "undefined") {
            return false;
        }

        try {
            if (typeof window.Search.init === "function") {
                window.Search.init();
            }
        } catch (error) {}

        try {
            if (typeof window.Search.performSearch === "function") {
                window.Search.performSearch(state.query);
                state.requested = true;
                return true;
            }
        } catch (error) {
            window.__irenogramSearchError = error;
        }

        return false;
    }

    function initSearchPage() {
        if (!isSearchPage()) {
            return;
        }

        state.query = getQuery();

        buildSearchPage();
        observeSearchResults();

        if (state.query) {
            setSearchStatus("Searching for “" + state.query + "” …", "loading");
        } else {
            setSearchStatus("Type a query and press Enter.", "idle");
        }

        const tick = function () {
            state.attempts += 1;

            runSphinxSearch();
            decorateSearchResults();

            if (state.query && (!state.decorated || !state.requested) && state.attempts < 120) {
                window.setTimeout(tick, 120);
                return;
            }

            if (state.query && state.attempts >= 120 && !state.decorated) {
                setSearchStatus("Search index loaded slowly. Refresh once if results are missing.", "error");
            }
        };

        tick();

        const form = document.querySelector(".ire-search-form");

        if (form) {
            form.addEventListener("submit", function (event) {
                const input = form.querySelector(".ire-search-input");
                const value = input && input.value ? input.value.trim() : "";

                if (!value) {
                    event.preventDefault();

                    if (input) {
                        input.focus();
                    }
                }
            });
        }
    }

    function fetchGitHubCounters() {
        const stars = document.getElementById("ire-stars-count");
        const usedBy = document.getElementById("ire-usedby-count");

        if (!stars && !usedBy) {
            return;
        }

        const cacheKey = "ire-github-cache";
        const cacheTime = localStorage.getItem(cacheKey + "-time");
        const now = Date.now();

        if (cacheTime && now - parseInt(cacheTime, 10) < 3600000) {
            try {
                const cached = JSON.parse(localStorage.getItem(cacheKey));

                if (cached && stars) {
                    stars.textContent = cached.stars;
                }

                if (cached && usedBy) {
                    usedBy.textContent = cached.used;
                }

                return;
            } catch (error) {}
        }

        fetch("https://api.github.com/repos/abirxdhack/irenogram", {
            headers: { Accept: "application/vnd.github.v3+json" }
        })
            .then(function (response) {
                if (!response.ok) {
                    throw new Error("GitHub unavailable");
                }

                return response.json();
            })
            .then(function (data) {
                const starCount = data.stargazers_count ? data.stargazers_count.toLocaleString() : "—";
                const usedCount = data.network_count ? data.network_count.toLocaleString() : "—";

                if (stars) {
                    stars.textContent = starCount;
                }

                if (usedBy) {
                    usedBy.textContent = usedCount;
                }

                localStorage.setItem(cacheKey, JSON.stringify({ stars: starCount, used: usedCount }));
                localStorage.setItem(cacheKey + "-time", now.toString());
            })
            .catch(function () {
                if (stars) {
                    stars.textContent = "—";
                }

                if (usedBy) {
                    usedBy.textContent = "—";
                }
            });
    }

    function highlightCurrentNav() {
        const path = window.location.pathname;

        document.querySelectorAll(".sidebar-tree a.reference").forEach(function (link) {
            const href = link.getAttribute("href");

            if (href && path.endsWith(href.replace(/^\.\//, "").replace(/^\.\.\//, ""))) {
                link.style.color = "var(--color-brand-content)";
                link.style.fontWeight = "600";

                const parent = link.closest("li");

                if (parent) {
                    parent.classList.add("current");
                }
            }
        });
    }

    function addCopyFeedback() {
        document.addEventListener("click", function (event) {
            const button = event.target.closest(".copybtn");

            if (!button) {
                return;
            }

            const html = button.innerHTML;
            const className = button.className;

            button.innerHTML = "✓ Copied";
            button.classList.add("copied");

            setTimeout(function () {
                button.innerHTML = html;
                button.className = className;
            }, 2000);

            const block = button.closest(".highlight");

            if (block) {
                const code = block.querySelector("pre");

                if (code && navigator.clipboard) {
                    navigator.clipboard.writeText(code.textContent).catch(function () {});
                }
            }
        });
    }

    function initSmoothScroll() {
        document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
            anchor.addEventListener("click", function (event) {
                const hash = anchor.getAttribute("href");

                if (!hash || hash === "#") {
                    return;
                }

                const target = document.querySelector(hash);

                if (!target) {
                    return;
                }

                event.preventDefault();
                target.scrollIntoView({ behavior: "smooth", block: "start" });
                history.pushState(null, "", hash);
            });
        });
    }

    function initBackToTop() {
        const button = document.querySelector(".back-to-top");

        if (!button) {
            return;
        }

        let ticking = false;

        window.addEventListener("scroll", function () {
            if (ticking) {
                return;
            }

            requestAnimationFrame(function () {
                const visible = window.scrollY > 300;

                button.style.opacity = visible ? "1" : "0";
                button.style.pointerEvents = visible ? "auto" : "none";
                ticking = false;
            });

            ticking = true;
        }, { passive: true });

        button.addEventListener("click", function (event) {
            event.preventDefault();
            window.scrollTo({ top: 0, behavior: "smooth" });
        });
    }

    function initReadingProgress() {
        if (document.querySelector(".ire-reading-progress")) {
            return;
        }

        const progress = document.createElement("div");
        progress.className = "ire-reading-progress";
        document.body.appendChild(progress);

        window.addEventListener("scroll", function () {
            const height = document.documentElement.scrollHeight - window.innerHeight;
            const percent = height > 0 ? window.scrollY / height * 100 : 0;

            progress.style.width = percent + "%";
        }, { passive: true });
    }

    function initAnimationHints() {
        if (isSearchPage()) {
            return;
        }

        document.querySelectorAll("table.docutils, .highlight").forEach(function (element, index) {
            element.style.animation = "fadeInUp " + Math.min(0.6 + index * 0.03, 1.2) + "s ease-out";
        });
    }

    function cleanupEnumDocumentation() {
        if (isSearchPage()) {
            return;
        }

        const article = document.querySelector("article[role='main']");

        if (!article) {
            return;
        }

        article.querySelectorAll("dl dt").forEach(function (dt) {
            const text = dt.textContent.trim();

            if (text.includes("=") && text.includes("<class")) {
                const match = text.match(/^([A-Z_]+)\s*=/);

                if (match) {
                    dt.textContent = match[1];
                }
            }
        });

        article.querySelectorAll("div.docinfo, .field-list").forEach(function (element) {
            if (element.textContent.includes("pyrogram.raw")) {
                element.style.display = "none";
            }
        });
    }

    applyStoredTheme();

    ready(function () {
        initThemeToggle();
        rewireSearchForms();
        initSearchPage();
        fetchGitHubCounters();
        highlightCurrentNav();
        addCopyFeedback();
        initSmoothScroll();
        initBackToTop();
        initReadingProgress();
        initAnimationHints();
        cleanupEnumDocumentation();
    });
})();
