#! /usr/bin/env python3

def main() -> None:
    total_priority = 0

    with open("input.txt", "r") as f:
        for line in f:
            rucksack = line.strip()
            total_priority += priority(dupe_item(rucksack))

    print(total_priority)


def dupe_item(rucksack: str) -> str:
    seen = set()
    midpoint = int(len(rucksack) / 2)

    i = 0
    while i < midpoint:
        seen.add(rucksack[i])
        i += 1

    while i < len(rucksack):
        if rucksack[i] in seen:
            return rucksack[i]
        i += 1

    raise RuntimeError("No dupe found")


def priority(item: str) -> int:
    if item.isupper():
        return ord(item) - ord('A') + 27

    return ord(item) - ord('a') + 1


if __name__ == "__main__":
    main()
