#! /usr/bin/env python3

from collections import deque
from typing import Deque

SEGMENT_SIZE: int = 4


def main() -> None:
    position = 0
    segment = deque(maxlen=SEGMENT_SIZE)

    with open("input.txt", "r") as f:
        for line in f:
            for c in line.strip():
                segment.append(c)
                position += 1

                if len(set(segment)) == SEGMENT_SIZE:
                    return print(position)


if __name__ == "__main__":
    main()
