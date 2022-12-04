#! /usr/bin/env python3

from typing import Tuple

SCORE = {
    "rock": 1,
    "paper": 2,
    "scissors": 3,
}
OPPONENT_WINS = {
   ("rock", "scissors"),
   ("scissors", "paper"),
   ("paper", "rock"),
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
    opp_play, my_play = decode(line)
    base_score = SCORE[my_play]

    if opp_play == my_play:
        return base_score + DRAW_BONUS

    if (opp_play, my_play) in OPPONENT_WINS:
        return base_score

    return base_score + WIN_BONUS
    

def decode(line: str) -> Tuple[str, str]:
    plays = line.split(" ")
    return decode_play(plays[0]), decode_play(plays[1])


def decode_play(play: str) -> str:
    match play:
        case "A" | "X":
            return "rock"
        case "B" | "Y":
            return "paper"
        case "C" | "Z":
            return "scissors"


if __name__ == "__main__":
    main()
