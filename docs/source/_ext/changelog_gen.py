"""
Auto-generated changelog for Irenogram.

This Sphinx extension runs on ``builder-inited`` and produces
``docs/source/releases/changelog.rst`` from the git history of the
repository, classifying each commit (added / updated / fixed / removed /
docs / other) without any hard-coded entries.

Commits are grouped by version: every annotated or lightweight tag whose
name looks like a version (``vX.Y.Z`` or ``X.Y.Z``) starts a new section.
Commits made after the most recent tag are listed under the current
``__version__`` from ``pyrogram/__init__.py`` (marked *Unreleased* if the
tag for that version does not exist yet).

The TL scheme layer is detected from ``compiler/api/source/main_api.tl``
(``// LAYER NNN``) and rendered next to the version, matching the
``Irenogram {version} Layer {layer}`` site title.

Nothing about the release notes is hard-coded; re-running the build picks
up new commits automatically.
"""

from __future__ import annotations

import os
import re
import subprocess
from collections import OrderedDict
from pathlib import Path

# --------------------------------------------------------------------------- #
# Classification rules
# --------------------------------------------------------------------------- #

# Order matters: the first matching category wins. Patterns are matched
# against the lower-cased commit subject (and the conventional-commit
# ``type`` prefix when present, e.g. ``feat:`` / ``fix(scope):``).
_RULES = (
    ("Removed",       re.compile(r"\b(remove[ds]?|delete[ds]?|drop(ped)?|deprecat\w*)\b")),
    ("Fixed",         re.compile(r"\b(fix(e[ds])?|bug(fix)?|patch(ed)?|hotfix|resolve[sd]?|correct(ed)?)\b|^fix(\(|:)")),
    ("Added",         re.compile(r"\b(add(ed|s)?|introduce[sd]?|implement(ed|s)?|support|new|create[sd]?)\b|^feat(\(|:)")),
    ("Documentation", re.compile(r"\b(docs?|documentation|readme|changelog)\b|^docs(\(|:)")),
    ("Updated",       re.compile(r"\b(update[ds]?|upgrad\w+|bump(ed)?|improv\w+|enhanc\w+|refactor\w*|rename[ds]?|optimi[sz]\w+|tweak\w*|polish\w*|cleanup|clean[- ]?up|chore|style|perf)\b|^(refactor|perf|chore|style)(\(|:)")),
)

_SKIP = re.compile(r"^(merge\b|wip\b|revert\b)", re.I)
_VERSION_TAG = re.compile(r"^v?(\d+\.\d+\.\d+(?:[-.\w]*)?)$")


# --------------------------------------------------------------------------- #
# Helpers
# --------------------------------------------------------------------------- #

def _run(args, cwd):
    try:
        out = subprocess.check_output(args, cwd=str(cwd), stderr=subprocess.DEVNULL)
    except (subprocess.CalledProcessError, FileNotFoundError):
        return ""
    return out.decode("utf-8", errors="replace").strip()


def _read_version(repo_root: Path) -> str:
    init = (repo_root / "pyrogram" / "__init__.py").read_text(encoding="utf-8")
    m = re.search(r'^__version__\s*=\s*["\']([^"\']+)["\']', init, re.M)
    return m.group(1) if m else "0.0.0"


def _read_layer(repo_root: Path) -> str:
    tl = repo_root / "compiler" / "api" / "source" / "main_api.tl"
    try:
        text = tl.read_text(encoding="utf-8")
    except OSError:
        return "?"
    m = None
    for m in re.finditer(r"//\s*LAYER\s+(\d+)", text, re.I):
        pass
    return m.group(1) if m else "?"


def _classify(subject: str) -> str:
    s = subject.strip().lower()
    if _SKIP.match(s):
        return ""  # skipped
    for label, rx in _RULES:
        if rx.search(s):
            return label
    return "Other"


def _git_tags(repo_root: Path):
    raw = _run(["git", "for-each-ref", "--sort=-creatordate",
                "--format=%(refname:short)\t%(creatordate:iso8601)",
                "refs/tags"], repo_root)
    tags = []
    for line in raw.splitlines():
        if "\t" not in line:
            continue
        name, _date = line.split("\t", 1)
        m = _VERSION_TAG.match(name)
        if m:
            tags.append((name, m.group(1)))
    return tags  # newest first


def _git_log(repo_root: Path, rev_range: str):
    fmt = "%H%x1f%s%x1f%an%x1f%ad"
    args = ["git", "log", "--no-merges", "--date=short", f"--pretty=format:{fmt}"]
    if rev_range:
        args.append(rev_range)
    raw = _run(args, repo_root)
    commits = []
    for line in raw.splitlines():
        parts = line.split("\x1f")
        if len(parts) != 4:
            continue
        sha, subject, author, date = parts
        commits.append({
            "sha": sha, "short": sha[:7],
            "subject": subject, "author": author, "date": date,
        })
    return commits


# --------------------------------------------------------------------------- #
# RST rendering
# --------------------------------------------------------------------------- #

_ORDER = ("Added", "Updated", "Fixed", "Removed", "Documentation", "Other")


def _escape(s: str) -> str:
    # Keep it simple: trim trailing periods, escape backticks lightly.
    s = s.strip().rstrip(".")
    return s.replace("``", "`")


def _render_section(title: str, layer: str, commits: list, repo_url: str | None) -> str:
    underline = "-" * len(title)
    out = [title, underline, ""]
    if layer:
        out.append(f":Layer: {layer}")
        out.append("")
    if not commits:
        out.append("*No changes recorded.*")
        out.append("")
        return "\n".join(out)

    buckets: OrderedDict[str, list] = OrderedDict((k, []) for k in _ORDER)
    for c in commits:
        label = _classify(c["subject"])
        if not label:
            continue
        buckets[label].append(c)

    any_written = False
    for label in _ORDER:
        items = buckets[label]
        if not items:
            continue
        any_written = True
        out.append(label)
        out.append("~" * len(label))
        out.append("")
        for c in items:
            subj = _escape(c["subject"])
            if repo_url:
                ref = f"`{c['short']} <{repo_url}/commit/{c['sha']}>`_"
            else:
                ref = f"``{c['short']}``"
            out.append(f"- {subj} ({ref}, {c['date']})")
        out.append("")

    if not any_written:
        out.append("*No notable changes.*")
        out.append("")
    return "\n".join(out)


# --------------------------------------------------------------------------- #
# Sphinx hook
# --------------------------------------------------------------------------- #

def _detect_repo_url(repo_root: Path) -> str | None:
    url = _run(["git", "config", "--get", "remote.origin.url"], repo_root)
    if not url:
        return None
    # Normalize git@github.com:user/repo.git â†’ https://github.com/user/repo
    m = re.match(r"git@([^:]+):(.+?)(?:\.git)?$", url)
    if m:
        return f"https://{m.group(1)}/{m.group(2)}"
    return url[:-4] if url.endswith(".git") else url


def generate(app):
    srcdir = Path(app.srcdir)
    repo_root = srcdir.parent.parent  # docs/source -> repo root
    out_path = srcdir / "releases" / "changelog.rst"

    version = _read_version(repo_root)
    layer = _read_layer(repo_root)
    repo_url = _detect_repo_url(repo_root)

    tags = _git_tags(repo_root)  # [(tagname, version), ...] newest first

    lines = [
        "Changelog",
        "=========",
        "",
        ".. note::",
        "",
        "   This page is generated automatically from the git history at build",
        "   time. Commit subjects are classified into *Added*, *Updated*,",
        "   *Fixed*, *Removed* and *Documentation* by keyword detection.",
        "",
    ]

    # Section: unreleased / current version (commits since latest tag)
    if tags:
        latest_tag = tags[0][0]
        latest_tag_version = tags[0][1]
        head_commits = _git_log(repo_root, f"{latest_tag}..HEAD")
        if head_commits:
            tag_for_current = next((t for t, v in tags if v == version), None)
            head_title = (
                f"Version {version} (Unreleased)"
                if tag_for_current is None else
                f"Version {version}"
            )
            lines.append(_render_section(head_title, layer, head_commits, repo_url))

        # Tagged releases, newest to oldest
        for i, (tag, tag_version) in enumerate(tags):
            prev = tags[i + 1][0] if i + 1 < len(tags) else None
            rev_range = f"{prev}..{tag}" if prev else tag
            commits = _git_log(repo_root, rev_range)
            section_layer = layer if tag_version == version else ""
            lines.append(_render_section(f"Version {tag_version}", section_layer, commits, repo_url))
    else:
        # No tags yet â€” list everything under the current version.
        commits = _git_log(repo_root, "")
        title = f"Version {version} (Unreleased)"
        lines.append(_render_section(title, layer, commits, repo_url))

    out_path.parent.mkdir(parents=True, exist_ok=True)
    new_text = "\n".join(lines).rstrip() + "\n"
    if out_path.exists() and out_path.read_text(encoding="utf-8") == new_text:
        return
    out_path.write_text(new_text, encoding="utf-8")


def setup(app):
    app.connect("builder-inited", generate)
    return {"version": "1.0", "parallel_read_safe": True, "parallel_write_safe": True}