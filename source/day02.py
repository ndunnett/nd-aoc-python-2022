import re
from input import load_input


def puzzle():
    input_lines = load_input(2)

    shapes = {
        "A": "rock",
        "B": "paper",
        "C": "scissors",
        "X": "rock",
        "Y": "paper",
        "Z": "scissors",
    }

    shape_scores = {
        "rock": 1,
        "paper": 2,
        "scissors": 3,
    }

    shape_defeats = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper",
    }

    score = 0
    regex = re.compile(r"(?P<OPP>[A-C])(?:\s)(?P<ME>[X-Z])")

    for line in input_lines:
        search = regex.search(line)
        opp = shapes[search.group("OPP")]
        me = shapes[search.group("ME")]

        score += shape_scores[me]

        if opp == me:
            score += 3

        if shape_defeats[me] == opp:
            score += 6

    print(f"Part 1 answer: {score}")

    outcomes = {
        "X": "lose",
        "Y": "draw",
        "Z": "win",
    }

    score = 0

    for line in input_lines:
        search = regex.search(line)
        opp = shapes[search.group("OPP")]
        outcome = outcomes[search.group("ME")]

        match outcome:
            case "lose":
                me = shape_defeats[opp]

            case "draw":
                score += 3
                me = opp

            case "win":
                score += 6
                me = shape_defeats[shape_defeats[opp]]

            case _:
                pass

        score += shape_scores[me]

    print(f"Part 2 answer: {score}")


if __name__ == "__main__":
    puzzle()
