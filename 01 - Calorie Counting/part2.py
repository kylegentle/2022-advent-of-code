#! /usr/bin/env python3

from heapq import heappush, heappop


def main() -> None:
    top3 = []

    with open("input.txt", "r") as f:
        cals_this_elf = 0

        for line in f:
            if not line.strip():
                if len(top3) < 3:
                    heappush(top3, cals_this_elf)

                elif cals_this_elf > top3[0]:
                    heappop(top3)
                    heappush(top3, cals_this_elf)

                cals_this_elf = 0
                continue

            cals_this_elf += int(line)

    print(sum(top3))


if __name__ == "__main__":
    main()
