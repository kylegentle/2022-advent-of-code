#! /usr/bin/env python3

from functools import reduce
from itertools import islice
from typing import List


GROUP_SIZE = 3


def main() -> None:
    total_priority = 0

    with open("input.txt", "r") as f:
        while True:
            group = [line.strip() for line in islice(f, GROUP_SIZE)]
            if not group:
                break

            total_priority += priority(get_badge(group))

    print(total_priority)


def get_badge(group: List[str]) -> str:
    return reduce(lambda x, y: set(x).intersection(set(y)), group).pop()


def priority(item: str) -> int:
    if item.isupper():
        return ord(item) - ord('A') + 27

    return ord(item) - ord('a') + 1


if __name__ == "__main__":
    main()
