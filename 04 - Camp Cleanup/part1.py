#! /usr/bin/env python3

from dataclasses import dataclass
from typing import Tuple


class Range:
    def __init__(self, lo: str, hi: str) -> None:
        self.low = int(lo)
        self.hi = int(hi)

    def contains(self, other: "Range") -> bool:
        return self.low <= other.low and self.hi >= other.hi


def main() -> None:
    fully_contained = 0
    with open("input.txt", "r") as f:
        for line in f:
            left, right = parse(line)
            if left.contains(right) or right.contains(left):
                fully_contained += 1
    print(fully_contained)


def parse(line: str) -> Tuple[Range, Range]:
    parts = line.strip().split(",")
    return Range(*parts[0].split("-")), Range(*parts[1].split("-"))


if __name__ == "__main__":
    main()
