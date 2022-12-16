import re
from input import load_input


def puzzle():
    lines = load_input(15)
    regex = re.compile(r"-?\d+")
    
    row = 2000000
    coverage = set()
    beacons = set()

    for line in lines:
        sx, sy, bx, by = map(int, regex.findall(line))

        if by == row:
            beacons.add(bx)

        distance = abs(sx - bx) + abs(sy - by)

        if sy >= row - distance and sy <= row + distance:
            for i in range(sx - distance, sx + distance + 1):
                if abs(sx - i) + abs(sy - row) <= distance:
                    coverage.add(i)

    answer = len(coverage.difference(beacons))
    print(f"Part 1 answer: {answer}")

    answer = 0
    limit = 4000000

    for i in range(limit + 1):
        ranges = []

        for line in lines:
            sx, sy, bx, by = map(int, regex.findall(line))
            difference = abs(sx - bx) + abs(sy - by) - abs(i - sy)

            if difference >= 0:
                ranges += [(sx - difference, sx + difference)]

        ranges.sort()
        coverage = ranges[0]

        for j in range(1, len(ranges)):
            (x_low, x_high) = ranges[j]

            if x_low <= coverage[1]:
                coverage = (coverage[0], max(coverage[1], x_high))
            else:
                answer = (coverage[1] + 1) * limit + i
                break

        if answer != 0:
            break

    print(f"Part 2 answer: {answer}")


if __name__ == "__main__":
    puzzle()
