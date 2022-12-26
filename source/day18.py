from ast import literal_eval
from input import load_input


def puzzle():
    lines = load_input(18)
    structure = set([literal_eval(f"({cube})") for cube in lines])
    x_min, x_max = (x := sorted(x[0] for x in structure))[0] - 1, x[-1] + 1
    y_min, y_max = (y := sorted(y[1] for y in structure))[0] - 1, y[-1] + 1
    z_min, z_max = (z := sorted(z[2] for z in structure))[0] - 1, z[-1] + 1

    def within_bounds(point):
        return x_min <= point[0] <= x_max and y_min <= point[1] <= y_max and z_min <= point[2] <= z_max

    def get_neighbours(point):
        (x, y, z) = point
        return [(x + 1, y, z), (x - 1, y, z), (x, y + 1, z), (x, y - 1, z), (x, y, z + 1), (x, y, z - 1)]

    def sides_exposed(point, structure):
        return sum(1 for side in get_neighbours(point) if side not in structure)

    answer = sum(sides_exposed(point, structure) for point in structure)
    print(f"Part 1 answer: {answer}")

    queue = []

    for point in structure:
        sides = get_neighbours(point)
        for side in sides:
            if side not in structure and side not in queue:
                queue += [side]

    structure_negative = set()

    while queue:
        starting_point = queue.pop()
        for point in [starting_point] + get_neighbours(starting_point):
            if point not in structure and point not in structure_negative and within_bounds(point):
                structure_negative.add(point)
                for next_point in get_neighbours(point):
                    if next_point not in structure and next_point not in structure_negative and within_bounds(next_point):
                        queue += [next_point]

    queue = [(x_min, y_min, z_min)]
    visited = set()
    answer = 0

    while queue:
        next_point = queue.pop()
        if next_point not in visited:
            visited.add(next_point)
            for point in get_neighbours(next_point):
                if within_bounds(point) and point not in visited:
                    if point in structure:
                        answer += 1
                    else:
                        queue += [point]

    print(f"Part 2 answer: {answer}")


if __name__ == "__main__":
    puzzle()
