"""Generate docs/_autogen/config_schema.rst by parsing CONFIG_*.txt files.
Accepts both "key: value" and "key = value" lines and strips inline comments.
"""
from __future__ import annotations
import re
import pathlib
import yaml

ROOT = pathlib.Path(__file__).resolve().parents[2]   # repo root
DOCS = pathlib.Path(__file__).resolve().parents[1]
AUTOGEN = DOCS / "_autogen"
DESCR = DOCS / "descriptions.yaml"

# Matches either 'key: value' or 'key = value' with optional whitespace
KEY_RE = re.compile(r"^\s*([A-Za-z0-9_]+)\s*[:=]\s*(.+?)\s*$")

def _read_descriptions():
    if DESCR.exists():
        with DESCR.open("r", encoding="utf-8") as f:
            raw = yaml.safe_load(f) or {}
    else:
        raw = {}
    # keys are used as-is
    return raw

def _parse_config(path: pathlib.Path):
    out = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        # strip inline comments
        line = raw.split('#', 1)[0].strip()
        if not line:
            continue
        m = KEY_RE.match(line)
        if m:
            out.append((m.group(1).strip(), m.group(2).strip()))
    return out

def _as_list_table(rows):
    lines = [
        ".. list-table:: CONFIG key schema",
        "   :header-rows: 1",
        "",
        "   * - Key",
        "     - Example value",
        "     - Type",
        "     - Units",
        "     - Description",
        "     - Section",
    ]
    for r in rows:
        lines.append("   * - " + r[0])
        lines.append("     - " + r[1])
        lines.append("     - " + r[2])
        lines.append("     - " + r[3])
        lines.append("     - " + r[4])
        lines.append("     - " + r[5])
    return "\n".join(lines) + "\n"

def generate_config_schema():
    meta = _read_descriptions()
    found = {}
    for f in sorted(ROOT.glob("CONFIG_*.txt")):
        for k, v in _parse_config(f):
            found.setdefault(k, {})[f.name] = v

    rows = []
    for key in sorted(found):
        ex = ", ".join(f"{fn}:{val}" for fn, val in sorted(found[key].items()))
        m = meta.get(key, {})
        rows.append([
            key,
            ex,
            str(m.get("type", "")),
            str(m.get("units", "")),
            str(m.get("description", "")),
            str(m.get("section", "")),
        ])

    AUTOGEN.mkdir(exist_ok=True)
    (AUTOGEN / "config_schema.rst").write_text(_as_list_table(rows), encoding="utf-8")

if __name__ == "__main__":
    generate_config_schema()