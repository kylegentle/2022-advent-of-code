#! /usr/bin/env python3


def main() -> None:
    max_cals = 0

    with open("input.txt", "r") as f:
        cals_this_elf = 0

        for line in f:
            if not line.strip():
                max_cals = max(max_cals, cals_this_elf)
                cals_this_elf = 0
                continue
            cals_this_elf += int(line)

    print(max_cals)


if __name__ == "__main__":
    main()
