#!/usr/bin/env python3
"""Create a UI/UX project dossier without overwriting existing data (stdlib)."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_DIR = SKILL_ROOT / "assets" / "project"
DOCUMENTS = (
    "00-brief.md", "01-research.md", "02-problem.md", "03-structure.md",
    "04-design.md", "05-test.md", "06-handoff.md", "07-measure.md", "08-decisions.md",
)
STAGES = (
    "discovery", "define", "structure", "ui", "test", "handoff", "measure",
)


def create_project(output: Path, name: str, template_dir: Path = TEMPLATE_DIR) -> dict:
    """Read and validate all inputs before creating an exclusively new folder.

    An I/O failure after creation may leave a partial dossier for inspection;
    never clean up an arbitrary user-provided output path automatically.
    """
    name = name.strip()
    if not name or "\n" in name or "\r" in name or "\x00" in name:
        raise ValueError("Tên dự án phải là một dòng không rỗng.")
    output = output.expanduser().resolve()
    if output == SKILL_ROOT or SKILL_ROOT in output.parents:
        raise ValueError("Đặt hồ sơ bên ngoài thư mục skill để giữ nguyên mẫu gốc.")
    if output.exists():
        raise FileExistsError(f"Đích đã tồn tại; không ghi đè: {output}")
    rendered = {}
    for filename in DOCUMENTS:
        content = (template_dir / filename).read_text(encoding="utf-8")
        if "{{PROJECT_NAME}}" not in content:
            raise ValueError(f"Mẫu thiếu trường tên dự án: {filename}")
        rendered[filename] = content.replace("{{PROJECT_NAME}}", name)
    state = {
        "schema_version": 1,
        "project_name": name,
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "mode": "unselected",
        "current_stage": "discovery",
        "stages": {stage: {"status": "not_started", "evidence": []} for stage in STAGES},
        "documents": list(DOCUMENTS),
        "decisions": [],
        "limitations": ["Chưa thu thập dữ liệu hoặc tiến hành kiểm thử người dùng."],
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.mkdir(exist_ok=False)
    for filename, content in rendered.items():
        with (output / filename).open("x", encoding="utf-8", newline="\n") as stream:
            stream.write(content)
    with (output / "project.json").open("x", encoding="utf-8", newline="\n") as stream:
        json.dump(state, stream, ensure_ascii=False, indent=2)
        stream.write("\n")
    return state


def main() -> int:
    parser = argparse.ArgumentParser(description="Tạo hồ sơ UI/UX mới, không ghi đè.")
    parser.add_argument("--name", required=True, help="Tên dự án bằng một dòng")
    parser.add_argument("--output", type=Path, required=True, help="Thư mục đích chưa tồn tại")
    args = parser.parse_args()
    try:
        state = create_project(args.output, args.name)
    except (OSError, ValueError) as exc:
        parser.exit(1, f"Không tạo được hồ sơ: {exc}\n")
    print(json.dumps({"output": str(args.output.resolve()), "document_count": len(state["documents"]),
                      "status": "not_started"}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
