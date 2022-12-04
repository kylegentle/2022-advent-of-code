#! /usr/bin/env python3

from dataclasses import dataclass
from typing import Tuple


class Range:
    def __init__(self, lo: str, hi: str) -> None:
        self.low = int(lo)
        self.hi = int(hi)

    def overlaps(self, other: "Range") -> bool:
        return not (
            other.low > self.hi or other.hi < self.low
        )


def main() -> None:
    overlaps = 0
    with open("input.txt", "r") as f:
        for line in f:
            left, right = parse(line)
            if left.overlaps(right) or right.overlaps(left):
                overlaps += 1
    print(overlaps)


def parse(line: str) -> Tuple[Range, Range]:
    parts = line.strip().split(",")
    return Range(*parts[0].split("-")), Range(*parts[1].split("-"))


if __name__ == "__main__":
    main()
