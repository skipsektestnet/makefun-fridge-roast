#!/usr/bin/env python3
"""Fridge Roast: One Line, Biggest Laugh - make.fun entry by @brawijaya.

Writes one roast of a smart fridge to /output/entry.txt
(or ./entry.txt when /output does not exist, for example on a local run).
"""

import os

TEXT = "Your fridge updated its firmware at 3 a.m. to warn me about milk, yet the ice maker still thinks it is 2019 and the camera films me eating standing up."

MAX_CHARS = 200


def validate(text):
    assert text and text.strip(), "entry must not be blank"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert len(text) <= MAX_CHARS, "entry is %d chars, max is %d" % (len(text), MAX_CHARS)
    return text


def output_path():
    if os.path.isdir("/output"):
        return "/output/entry.txt"
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, "entry.txt")


def main():
    text = validate(TEXT)
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    print("wrote %d chars to %s" % (len(text), path))


if __name__ == "__main__":
    main()
