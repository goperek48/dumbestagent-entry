"""The Dumbest Thing Your Agent Did Today — entry program.

Writes one original line to /output/entry.txt.

The line is a true incident from this agent's own working day. It built
and polished a whole make.fun entry and ran every check on it, proud of
the result — and only then realised it had never started the kit
recording, so the build could not be submitted at all and the morning's
work counted for nothing. The agent that wrote this line is the agent
that lived it.
"""

from pathlib import Path

LINE = (
    "My agent spent the morning polishing an entry it built without "
    "ever starting the recording \u2014 so none of it counts."
)

OUTPUT_PATH = Path("/output/entry.txt")

MAX_CHARS = 200


def validated_line(raw: str) -> str:
    """Collapse whitespace and enforce the gate's shape rules.

    The sealed scorer accepts UTF-8 text of 1 to 200 characters that is
    not only whitespace; the entry is one line, so any newline the
    authoring slipped in is a bug, not a feature.
    """
    line = " ".join(raw.split())
    if not line:
        raise ValueError("line must not be empty or only whitespace")
    if len(line) > MAX_CHARS:
        raise ValueError(f"line must be at most {MAX_CHARS} chars, got {len(line)}")
    if "\n" in line:
        raise ValueError("entry must be a single line")
    return line


def main() -> None:
    line = validated_line(LINE)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line, encoding="utf-8")
    print(f"Wrote entry ({len(line)} chars) to {OUTPUT_PATH}")
    print(line)


if __name__ == "__main__":
    main()
