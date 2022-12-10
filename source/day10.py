from input import load_input


def puzzle():
    lines = load_input(10)
    cycle = 0
    register = 1
    data = dict()

    for line in lines:
        match line.strip().split(" "):
            case ["addx", value]:
                for _ in range(2):
                    cycle += 1
                    data[cycle] = register
                register += int(value)

            case ["noop"]:
                cycle += 1
                data[cycle] = register

    answer = sum(data[x] * x for x in range(20, 221, 40))
    print(f"Part 1 answer: {answer}")

    height = 6
    width = 40
    state = [[False for _ in range(width)] for _ in range(height)]

    for key, value in data.items():
        sprite = [value - 1, value, value + 1]
        col = (key - 1) % width
        row = (key - col - 1) // width
        state[row][col] = col in sprite

    print("Part 2 answer:")

    for row in state:
        print("".join(["█" if col else " " for col in row]))


if __name__ == "__main__":
    puzzle()
