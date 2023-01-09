from input import load_input


def puzzle():
    lines = load_input(25)

    snafu = {
        "=": -2,
        "-": -1,
        "0": 0,
        "1": 1,
        "2": 2
    }

    value = sum(sum(snafu[digit] * 5 ** power for power, digit in enumerate(reversed(line))) for line in lines)
    answer = ""

    while value > 0:
        value += 2
        answer = list(snafu.keys())[value % 5] + answer
        value //= 5

    print(f"Part 1 answer: {answer}")


if __name__ == "__main__":
    puzzle()
