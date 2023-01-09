from copy import deepcopy
from input import load_input


def puzzle():
    lines = load_input(24)
    height = len(lines) - 2
    width = len(lines[0]) - 2
    start = (-1, 0)
    goal = (height, width - 1)

    moves = {
        ">": (0, 1),
        "<": (0, -1),
        "v": (1, 0),
        "^": (-1, 0)
    }

    blizzards = dict()

    for row, line in enumerate(lines):
        for col, element in enumerate(line):
            if col > 0 and col <= width and row > 0 and row <= height:
                blizzards[(row - 1, col - 1)] = [element] if element in moves else []

    def get_neighbours(point):
        neighbours = [point] if is_valid_move(point) else []

        for move in moves.values():
            next_point = (point[0] + move[0], point[1] + move[1])

            if is_valid_move(next_point):
                neighbours.append(next_point)

        return neighbours

    def is_valid_move(point):
        if point in [start, goal]:
            return True

        if point not in blizzards or len(blizzards[point]) > 0:
            return False

        return True

    def move_to_goal():
        positions = [start]
        time = 0

        while True:
            time += 1
            next_positions = []

            for point, elements in deepcopy(blizzards).items():
                for element in elements:
                    blizzards[point].remove(element)
                    blizzards[((point[0] + moves[element][0]) % height, (point[1] + moves[element][1]) % width)].append(element)

            for _point in positions:
                for point in get_neighbours(_point):
                    if point == goal:
                        return time

                    next_positions.append(point)

            positions = list(set(next_positions))

            if not positions:
                positions.append(start)

    answer = move_to_goal()
    print(f"Part 1 answer: {answer}")

    start, goal = goal, start
    answer += move_to_goal()
    start, goal = goal, start
    answer += move_to_goal()
    print(f"Part 2 answer: {answer}")


if __name__ == "__main__":
    puzzle()
