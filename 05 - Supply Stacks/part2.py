#! /usr/bin/env python3

from collections import deque, defaultdict
from typing import Deque, List, Optional


def main() -> None:
    stacks = [deque() for _ in range(9)]

    with open("input.txt", "r") as f:
        for line in f:
            if line.startswith("["):
                build_stacks(stacks, line)

            if not line.strip():
                continue

            if line.startswith("move"):
                move(stacks, line.strip())

    top_crates = [crate for s in stacks if (crate := s.pop())]
    print(''.join(top_crates))


def build_stacks(stacks: List[Deque[str]], line: str) -> List[Deque[str]]:
    vals = parse_crates(line)

    for i, val in enumerate(vals):
        if val: stacks[i].appendleft(val)
    return stacks
    

def parse_crates(line: str) -> List[Optional[str]]:
    parse_val = lambda v: v if v != ' ' else None
    return [parse_val(line[i]) for i in range(1, len(line), 4)]


def move(stacks: List[Deque[str]], instruction: str) -> None:
    words = instruction.split(' ')
    num, src, dest = int(words[1]), int(words[3]), int(words[5])

    to_move = deque()
    while num:
        to_move.appendleft(stacks[src-1].pop())
        num -= 1

    while to_move:
        stacks[dest-1].append(to_move.popleft())


if __name__ == "__main__":
    main()
