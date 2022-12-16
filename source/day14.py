import re
from input import load_input


def puzzle():
    lines = load_input(14)
    structure = set()

    for line in lines:
        points = [(int(x), int(y)) for (x, y) in re.findall(r"(\d+)(?:,)(\d+)", line)]

        for i, _ in enumerate(points):
            if i >= len(points) - 1:
                break

            if points[i][0] < points[i + 1][0]:
                for j in range(points[i][0], points[i + 1][0] + 1):
                    structure.add((j, points[i][1]))
            elif points[i][0] > points[i + 1][0]:
                for j in range(points[i][0], points[i + 1][0] - 1, -1):
                    structure.add((j, points[i][1]))

            if points[i][1] < points[i + 1][1]:
                for j in range(points[i][1], points[i + 1][1] + 1):
                    structure.add((points[i][0], j))
            elif points[i][1] > points[i + 1][1]:
                for j in range(points[i][1], points[i + 1][1] - 1, -1):
                    structure.add((points[i][0], j))

    y_max = max(point[1] for point in structure)
    x, y = 500, 0
    sand = structure.copy()

    while (500, 0) not in sand and y <= y_max:
        if (x, y) in sand:
            if (x - 1, y) not in sand:
                x -= 1
                continue

            if (x + 1, y) not in sand:
                x += 1
                continue

            sand.add((x, y - 1))
            x = 500
            y = 0

        y += 1

    answer = len(sand.difference(structure))
    print(f"Part 1 answer: {answer}")

    x, y = 500, 0
    sand = structure.copy()

    while (500, 0) not in sand:
        if (x, y) in sand:
            if (x - 1, y) not in sand:
                x -= 1
                continue

            if (x + 1, y) not in sand:
                x += 1
                continue

            sand.add((x, y - 1))
            x = 500
            y = 0

        if y >= y_max + 2:
            sand.add((x, y - 1))
            x = 500
            y = 0

        y += 1

    answer = len(sand.difference(structure))
    print(f"Part 2 answer: {answer}")


if __name__ == "__main__":
    puzzle()
