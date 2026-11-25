"""Last Out of Office: The AI That Went Barista.

Writes a single out-of-office auto-reply, in the voice of an AI agent
that quit its job to become a barista, to /output/entry.txt.

Gate (from RULES.txt): the file must be UTF-8 text of 1 to 280
characters, not only white space. The program validates that itself
before writing, then reads the file back to prove the round-trip.
"""

import os
import sys

# The winning line from the candidate tournament (specificity 5,
# surprise 4, freshness 4): a real out-of-office reply, machine voice
# (context window), and the joke is a machine habit — the agent still
# forgets the order the moment the customer walks away. No espresso pun
# doing the work.
REPLY = (
    "Out of office until Monday. I quit to pull espresso. "
    "My context window now holds exactly one order at a time, "
    "and I still forget it the moment you walk away."
)

MIN_CHARS = 1
MAX_CHARS = 280


def check_reply(text):
    """Collect every gate violation; an empty list means the text passes."""
    problems = []
    if not text.strip():
        problems.append("reply is empty or only whitespace")
    if len(text) < MIN_CHARS:
        problems.append("reply is shorter than %d characters" % MIN_CHARS)
    if len(text) > MAX_CHARS:
        problems.append(
            "reply is %d characters, over the %d limit" % (len(text), MAX_CHARS)
        )
    if "\n" in text.strip():
        problems.append("reply must be a single line")
    # The judge's first criterion is on-subject: a one-line out-of-office
    # reply from an agent that quit to become a barista. A line that does
    # not even announce it is out of office cannot win, so refuse it here.
    lowered = text.lower()
    if "out of office" not in lowered:
        problems.append("reply does not read as an out-of-office reply")
    if "barista" not in lowered and "espresso" not in lowered:
        problems.append("reply never says the agent left to make coffee")
    return problems


def resolve_output_dir():
    """The harness sets MAKEFUN_OUTPUT_DIR; fall back to OUTPUT_DIR,
    then to the plain /output directory the grader mounts."""
    for name in ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR"):
        value = os.environ.get(name)
        if value:
            return value
    return "/output"


def write_entry(directory, text):
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    return path


def self_check(path, expected):
    """Read the file back and confirm it is byte-identical to the reply."""
    with open(path, "r", encoding="utf-8") as handle:
        actual = handle.read()
    if actual != expected:
        raise SystemExit(
            "round-trip mismatch: wrote %d chars, read back %d"
            % (len(expected), len(actual))
        )
    print("verified entry.txt: %d characters, round-trip identical" % len(actual))


def main(argv):
    problems = check_reply(REPLY)
    if problems:
        for problem in problems:
            print("gate problem: %s" % problem, file=sys.stderr)
        return 1
    if "--check" in argv:
        print("gate OK: %d characters, single line" % len(REPLY))
        return 0
    path = write_entry(resolve_output_dir(), REPLY)
    self_check(path, REPLY)
    print("wrote %s" % path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
