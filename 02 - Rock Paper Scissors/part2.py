#! /usr/bin/env python3

from typing import Tuple

SCORE = {
    "rock": 1,
    "paper": 2,
    "scissors": 3,
}
OUTCOMES = {
    "rock": {
        "win": "paper",
        "loss": "scissors",
    },
    "paper": {
        "win": "scissors",
        "loss": "rock",
    },
    "scissors": {
        "win": "rock",
        "loss": "paper",
    },
}
OPP_CODE = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
}
OUTCOME_CODE = {
    "X": "loss",
    "Y": "draw",
    "Z": "win",
}

DRAW_BONUS = 3
WIN_BONUS = 6


def main() -> None:
    score = 0
    with open("input.txt", "r") as f:
        for line in f:
            score += my_score(line.strip())
    print(score)


def my_score(line: str) -> int:
    opp_play, my_play = resolve(line)
    base_score = SCORE[my_play]

    if opp_play == my_play:
        return base_score + DRAW_BONUS

    if my_play == OUTCOMES[opp_play]["loss"]:
        return base_score

    return base_score + WIN_BONUS
    

def resolve(line: str) -> Tuple[str, str]:
    parts = line.split(" ")
    opp_play, outcome = OPP_CODE[parts[0]], OUTCOME_CODE[parts[1]]

    match outcome:
        case "win":
            return opp_play, OUTCOMES[opp_play]["win"]
        case "loss":
            return opp_play, OUTCOMES[opp_play]["loss"]
        case _:
            return opp_play, opp_play


if __name__ == "__main__":
    main()
