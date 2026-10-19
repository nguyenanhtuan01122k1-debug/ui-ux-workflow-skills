#!/usr/bin/env python3
"""Validate bundled Base/Alias exports without modifying source files."""

from __future__ import annotations

import argparse
import json
import math
import re
from pathlib import Path

TOKEN_DIR = Path(__file__).resolve().parents[1] / "assets" / "tokens"


def flatten(node: dict, prefix: str = "") -> dict:
    if not isinstance(node, dict):
        raise ValueError(f"Nhóm token không hợp lệ: {prefix or 'root'}")
    if "$value" in node:
        if not prefix:
            raise ValueError("Token cần đường dẫn có tên.")
        return {prefix: node}
    result = {}
    for key, child in node.items():
        if not key.startswith("$"):
            result.update(flatten(child, f"{prefix}/{key}" if prefix else key))
    return result


def is_number(value) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def validate_token(path: str, token: dict) -> list[str]:
    errors = []
    kind, value = token.get("$type"), token["$value"]
    if kind == "number":
        if not is_number(value) or value < 0:
            errors.append(f"{path}: số không âm không hợp lệ")
    elif kind == "string":
        if not isinstance(value, str) or not value.strip():
            errors.append(f"{path}: chuỗi rỗng hoặc không hợp lệ")
    elif kind == "color":
        if not isinstance(value, dict) or value.get("colorSpace") != "srgb":
            return [f"{path}: cần colorSpace srgb"]
        components = value.get("components")
        alpha = value.get("alpha")
        hex_value = value.get("hex", "")
        if not isinstance(components, list) or len(components) != 3 or not all(
                is_number(n) and 0 <= n <= 1 for n in components):
            errors.append(f"{path}: components phải gồm 3 số từ 0 đến 1")
        if not is_number(alpha) or not 0 <= alpha <= 1:
            errors.append(f"{path}: alpha không hợp lệ")
        if not isinstance(hex_value, str) or not re.fullmatch(r"#[0-9A-Fa-f]{6}", hex_value):
            errors.append(f"{path}: hex cần dạng #RRGGBB")
        if not errors:
            channels = [int(hex_value[i:i+2], 16) / 255 for i in (1, 3, 5)]
            if any(abs(a-b) > 1 / 255 + 1e-6 for a, b in zip(components, channels)):
                errors.append(f"{path}: hex khác components")
    else:
        errors.append(f"{path}: kiểu chưa hỗ trợ {kind!r}")
    return errors


def audit(base_doc: dict, alias_doc: dict) -> dict:
    base, aliases = flatten(base_doc), flatten(alias_doc)
    errors = []
    for path, token in base.items():
        errors.extend(validate_token(f"Base/{path}", token))
    for path, token in aliases.items():
        errors.extend(validate_token(f"Alias/{path}", token))
        target = token.get("$extensions", {}).get("com.figma.aliasData", {}).get("targetVariableName")
        if target not in base:
            errors.append(f"Alias/{path}: target không có trong Base: {target!r}")
            continue
        source = base[target]
        if token.get("$type") != source.get("$type"):
            errors.append(f"Alias/{path}: kiểu khác target {target}")
        left, right = token["$value"], source["$value"]
        if token.get("$type") == source.get("$type") == "color" and isinstance(left, dict) and isinstance(right, dict):
            # Ignore rounded float noise; alpha remains part of the value.
            if (left.get("hex", "").lower() != right.get("hex", "").lower()
                    or left.get("alpha") != right.get("alpha")
                    or left.get("colorSpace") != right.get("colorSpace")):
                errors.append(f"Alias/{path}: giá trị resolve khác target {target}")
        elif left != right:
            errors.append(f"Alias/{path}: giá trị resolve khác target {target}")
    return {"ok": not errors, "base_count": len(base), "alias_count": len(aliases), "errors": errors}


def main() -> int:
    parser = argparse.ArgumentParser(description="Kiểm tra token Văn Minh Việt, không sửa dữ liệu.")
    parser.add_argument("--base", type=Path, default=TOKEN_DIR / "base.tokens.json")
    parser.add_argument("--alias", type=Path, default=TOKEN_DIR / "alias.tokens.json")
    args = parser.parse_args()
    try:
        result = audit(json.loads(args.base.read_text(encoding="utf-8-sig")),
                       json.loads(args.alias.read_text(encoding="utf-8-sig")))
    except (OSError, ValueError, TypeError) as exc:
        result = {"ok": False, "errors": [str(exc)]}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
