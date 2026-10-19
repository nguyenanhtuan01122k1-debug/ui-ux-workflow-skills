#!/usr/bin/env python3
"""Check packaging invariants and local Markdown links; no UX quality claims."""

from __future__ import annotations

import json
import re
import runpy
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "ui-ux-workflow"


def check() -> list[str]:
    errors = []
    required = [ROOT / "README.md", SKILL / "SKILL.md", SKILL / "agents" / "openai.yaml",
                SKILL / "scripts" / "new_project.py", ROOT / "tests" / "test_new_project.py"]
    for path in required:
        if not path.is_file():
            errors.append(f"Thiếu file: {path.relative_to(ROOT)}")
    entry = SKILL / "SKILL.md"
    if entry.is_file():
        content = entry.read_text(encoding="utf-8")
        match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", content, re.DOTALL)
        if not match:
            errors.append("SKILL.md thiếu frontmatter.")
        else:
            name = re.search(r"^name:\s*(.+)$", match[1], re.MULTILINE)
            description = re.search(r"^description:\s*(.+)$", match[1], re.MULTILINE)
            if not name or name[1].strip() != SKILL.name:
                errors.append("Tên skill không khớp thư mục.")
            if not description or not description[1].strip():
                errors.append("Thiếu mô tả định tuyến skill.")
    # External URLs are not fetched. Ignore fenced code and link anchors.
    for path in sorted(ROOT.rglob("*.md")):
        if ".git" in path.parts or "projects" in path.relative_to(ROOT).parts:
            continue
        content = path.read_text(encoding="utf-8")
        content = re.sub(r"^(`{3,}|~{3,}).*?^\1\s*$", "", content, flags=re.MULTILINE | re.DOTALL)
        for dest in re.findall(r"!?\[[^\]]*\]\(([^\s)]+)\)", content):
            dest = dest.strip("<>")
            parsed = urlsplit(dest)
            if parsed.scheme or dest.startswith(("#", "//")):
                continue
            target = (path.parent / unquote(parsed.path)).resolve()
            if target != ROOT and ROOT not in target.parents:
                errors.append(f"Link thoát repo: {path.relative_to(ROOT)} -> {dest}")
            elif not target.exists():
                errors.append(f"Link hỏng: {path.relative_to(ROOT)} -> {dest}")
    templates = SKILL / "assets" / "project"
    if len(list(templates.glob("*.md"))) != 9:
        errors.append("Cần 9 mẫu hồ sơ dự án.")
    for path in templates.glob("*.md"):
        if "{{PROJECT_NAME}}" not in path.read_text(encoding="utf-8"):
            errors.append(f"Mẫu thiếu tên dự án: {path.name}")
    metadata = SKILL / "agents" / "openai.yaml"
    if metadata.is_file() and "$ui-ux-workflow" not in metadata.read_text(encoding="utf-8"):
        errors.append("Default prompt không gọi đúng skill.")
    token_checker = SKILL / "scripts" / "check_tokens.py"
    try:
        checker = runpy.run_path(str(token_checker))
        token_dir = SKILL / "assets" / "tokens"
        result = checker["audit"](
            json.loads((token_dir / "base.tokens.json").read_text(encoding="utf-8-sig")),
            json.loads((token_dir / "alias.tokens.json").read_text(encoding="utf-8-sig")),
        )
        errors.extend(result["errors"])
    except (OSError, ValueError, TypeError) as exc:
        errors.append(f"Không kiểm tra được token: {exc}")
    return errors


if __name__ == "__main__":
    errors = check()
    print(json.dumps({"ok": not errors, "errors": errors}, ensure_ascii=False, indent=2))
    raise SystemExit(1 if errors else 0)
