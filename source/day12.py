# from input import load_input


def puzzle():
    # lines = load_input(12)

    lines = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi""".splitlines()

    def back_track(moves, x, y):
        current = ord(lines[y][x])

        if current == ord("E"):
            return moves

        if current == ord("S"):
            current = 999

        candidates = []

        if y > 0:
            index = (x, y - 1)
            value = ord(lines[index[1]][index[0]])

            if value == ord("E"):
                value = ord("z")

            if value <= current + 1 and index not in moves:
                candidates += [index]

        if y < len(lines) - 1:
            index = (x, y + 1)
            value = ord(lines[index[1]][index[0]])

            if value == ord("E"):
                value = ord("z")

            if value <= current + 1 and index not in moves:
                candidates += [index]

        if x > 0:
            index = (x - 1, y)
            value = ord(lines[index[1]][index[0]])

            if value == ord("E"):
                value = ord("z")

            if value <= current + 1 and index not in moves:
                candidates += [index]

        if x < len(lines[0]) - 1:
            index = (x + 1, y)
            value = ord(lines[index[1]][index[0]])

            if value == ord("E"):
                value = ord("z")

            if value <= current + 1 and index not in moves:
                candidates += [index]

        valid_paths = []

        for candidate in candidates:
            path = back_track(moves + [candidate], candidate[0], candidate[1])

            if path:
                valid_paths += [path]

        if valid_paths:
            return sorted(valid_paths, reverse=True)[0]

        return None

    current_x = 0
    current_y = 0

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "S":
                current_x = x
                current_y = y

    answer = back_track([(current_x, current_y)], current_x, current_y)
    print(f"Part 1 answer: {len(answer[1:])}")

    answer = 0
    print(f"Part 2 answer: {answer}")


if __name__ == "__main__":
    puzzle()
