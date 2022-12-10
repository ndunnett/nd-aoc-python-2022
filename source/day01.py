from input import load_input


def puzzle():
    input_lines = load_input(1)
    reindeer = []
    current = 0

    for line in input_lines:
        if line.strip() == "":
            reindeer += [current]
            current = 0
        else:
            current += int(line.strip())

    print(f"Part 1 answer: {sorted(reindeer, reverse=True)[0]}")
    print(f"Part 2 answer: {sum(sorted(reindeer, reverse=True)[:3])}")


if __name__ == "__main__":
    puzzle()
