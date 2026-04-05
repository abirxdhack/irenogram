(function () {
    "use strict";

    function applyStoredTheme() {
        var stored = localStorage.getItem("theme");
        if (stored && stored !== "auto") {
            document.body.setAttribute("data-theme", stored);
        }
    }

    applyStoredTheme();

    function initThemeToggle() {
        document.querySelectorAll(".theme-toggle").forEach(function (btn) {
            btn.addEventListener("click", function (e) {
                e.stopImmediatePropagation();
                var current = document.body.getAttribute("data-theme") || "auto";
                var next = current === "auto" ? "light" : current === "light" ? "dark" : "auto";
                document.body.setAttribute("data-theme", next);
                localStorage.setItem("theme", next === "auto" ? "" : next);
            }, true);
        });
    }

    function fetchGitHubCounters() {
        var starsCountEl = document.getElementById("ire-stars-count");
        var usedByCountEl = document.getElementById("ire-usedby-count");

        if (!starsCountEl && !usedByCountEl) return;

        fetch("https://api.github.com/repos/abirxdhack/irenogram")
            .then(function (r) { return r.json(); })
            .then(function (data) {
                if (starsCountEl && data.stargazers_count !== undefined) {
                    starsCountEl.textContent = data.stargazers_count.toLocaleString();
                }
                if (usedByCountEl && data.subscribers_count !== undefined) {
                    usedByCountEl.textContent = data.subscribers_count.toLocaleString();
                }
            })
            .catch(function () {});

        fetch("https://api.github.com/search/repositories?q=irenogram&sort=stars")
            .then(function (r) { return r.json(); })
            .catch(function () {});
    }

    function highlightCurrentNav() {
        var path = window.location.pathname;
        document.querySelectorAll(".sidebar-tree a.reference").forEach(function (link) {
            var href = link.getAttribute("href");
            if (href && path.endsWith(href.replace(/^\.\//, "").replace(/^\.\.\//, ""))) {
                link.style.color = "var(--color-brand-content)";
                link.style.fontWeight = "600";
                var parent = link.closest("li");
                if (parent) parent.classList.add("current");
            }
        });
    }

    function addCopyFeedback() {
        document.addEventListener("click", function (e) {
            var btn = e.target.closest(".copybtn");
            if (btn) {
                var orig = btn.innerHTML;
                btn.innerHTML = "✓ Copied";
                setTimeout(function () { btn.innerHTML = orig; }, 2000);
            }
        });
    }

    function initSmoothScroll() {
        document.querySelectorAll('a[href^="#"]').forEach(function (a) {
            a.addEventListener("click", function (e) {
                var target = document.querySelector(this.getAttribute("href"));
                if (target) {
                    e.preventDefault();
                    target.scrollIntoView({ behavior: "smooth", block: "start" });
                    history.pushState(null, null, this.getAttribute("href"));
                }
            });
        });
    }

    function initBackToTop() {
        var btn = document.querySelector(".back-to-top");
        if (!btn) return;
        window.addEventListener("scroll", function () {
            var visible = window.scrollY > 300;
            btn.style.opacity = visible ? "1" : "0";
            btn.style.pointerEvents = visible ? "auto" : "none";
        });
        btn.addEventListener("click", function (e) {
            e.preventDefault();
            window.scrollTo({ top: 0, behavior: "smooth" });
        });
    }

    document.addEventListener("DOMContentLoaded", function () {
        initThemeToggle();
        fetchGitHubCounters();
        highlightCurrentNav();
        addCopyFeedback();
        initSmoothScroll();
        initBackToTop();
    });
})();
