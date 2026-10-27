#!/usr/bin/env python3
"""Link this checkout into all supported global skill directories, without prompts."""

from __future__ import annotations

import json
import os
from pathlib import Path
import sys
import uuid

NAME = "branch-breaker"
REQUIRED_FILES = (
    "SKILL.md", "agents/openai.yaml", "references/report-contract.md",
    "references/adversarial-probes.md", "references/web-execution.md",
    "references/mobile-execution.md", "references/pr-reporting.md",
    "references/full-stack-quality.md", "references/learning-sources.md",
)


def resolved(path: Path) -> Path | None:
    try:
        return path.resolve()
    except (OSError, RuntimeError):
        return None  # A broken symlink cycle can be preserved and replaced.


def install(source: Path, home: Path, codex_home: Path | None = None) -> list[dict]:
    source = source.resolve(strict=True)
    home = home.expanduser().absolute()
    for required in REQUIRED_FILES:
        path = source / required
        if not path.is_file():
            raise ValueError(f"Incomplete skill checkout: missing {path}")

    shared = home / ".agents/skills" / NAME
    codex = (codex_home.expanduser().absolute() if codex_home else home / ".codex")
    destinations = [shared, codex / "skills" / NAME,
                    home / ".cursor/skills" / NAME, home / ".claude/skills" / NAME]
    # Preflight before moving anything: never move a directory containing this script.
    for destination in destinations:
        actual = resolved(destination)
        parent = resolved(destination.parent)
        if parent is None:
            raise ValueError(f"Installation parent contains a symlink cycle: {destination.parent}")
        if parent == source or source in parent.parents:
            raise ValueError(f"Installation destination is inside checkout: {destination}")
        if actual is not None and actual != source and actual in source.parents:
            raise ValueError(f"Checkout is inside installation destination: {destination}")

    backup_root = home / ".local/state" / NAME / "backups" / uuid.uuid4().hex
    records: list[dict] = []
    manifest: list[dict] = []

    def preserve(path: Path) -> str:
        backup_root.mkdir(parents=True, exist_ok=True)
        backup = backup_root / f"{len(manifest) + 1}-{path.parent.name}-{path.name}"
        record = {"original": str(path), "backup": str(backup)}
        if path.is_symlink():
            record["link_target"] = os.readlink(path)
        path.rename(backup)  # Move the entry itself; never follow a displaced symlink.
        manifest.append(record)
        (backup_root / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
        return str(backup)

    # Repair only the known accidental `ln -s source existing-directory` child.
    nested = source / NAME
    if nested.is_symlink():
        raw_target = Path(os.path.abspath(nested.parent / os.readlink(nested)))
        if resolved(nested) == source or raw_target == nested:
            records.append({"path": str(nested), "status": "repaired", "backup": preserve(nested)})

    for destination in dict.fromkeys(destinations):
        if resolved(destination) == source:
            records.append({"path": str(destination), "status": "unchanged"})
            continue
        destination.parent.mkdir(parents=True, exist_ok=True)
        record = {"path": str(destination), "status": "linked"}
        if destination.exists() or destination.is_symlink():
            record["backup"] = preserve(destination)
        target = source if destination == shared else shared
        # symlink_to creates exactly this entry, never a child inside an existing directory.
        destination.symlink_to(target, target_is_directory=True)
        if destination.resolve(strict=True) != source:
            raise OSError(f"Installation verification failed: {destination}")
        records.append(record)
    return records


def main() -> int:
    if len(sys.argv) > 1:
        print("Usage: python3 install.py\nInstalls globally for Codex, Cursor, and Claude; no options or prompts.")
        return 0 if sys.argv[1:] == ["--help"] else 2
    try:
        configured = os.environ.get("CODEX_HOME")
        records = install(Path(__file__).resolve().parent, Path.home(),
                          Path(configured) if configured else None)
    except (OSError, ValueError, RuntimeError) as error:
        print(f"Install failed: {error}\nExisting entries are preserved in ~/.local/state/branch-breaker/backups when moved.", file=sys.stderr)
        return 1
    for record in records:
        print(f"{record['status']}: {record['path']}")
        if record.get("backup"):
            print(f"  previous entry: {record['backup']}")
    print("Installed for Codex, Cursor, and Claude. Start a new session to refresh discovery.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
