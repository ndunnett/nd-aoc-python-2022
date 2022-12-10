from input import load_input


def puzzle():
    lines = load_input(8)
    visibility = [[False for _ in range(len(lines[0].strip()))] for _ in range(len(lines))]
    lines = [[int(lines[i][j]) for j in range(len(lines[0].strip()))] for i in range(len(lines))]

    def rotate_matrix(matrix):
        return [[matrix[len(row) - 1 - j][i] for j, _ in enumerate(row)] for i, row in enumerate(matrix)]

    def check_visibility():
        for i, row in enumerate(lines):
            current = -1
            for j, col in enumerate(row):
                if col > current:
                    current = col
                    visibility[i][j] = True

    for _ in range(4):
        check_visibility()
        lines = rotate_matrix(lines)
        visibility = rotate_matrix(visibility)

    answer = sum([sum([1 for col in row if col]) for row in visibility])
    print(f"Part 1 answer: {answer}")

    def scenic_score(x, y):
        down, up, right, left = 0, 0, 0, 0

        for _y in range(y + 1, len(lines)):
            down += 1
            if lines[_y][x] >= lines[y][x]:
                break

        for _y in range(y - 1, 0 - 1, -1):
            up += 1
            if lines[_y][x] >= lines[y][x]:
                break

        for _x in range(x + 1, len(lines)):
            right += 1
            if lines[y][_x] >= lines[y][x]:
                break

        for _x in range(x - 1, 0 - 1, -1):
            left += 1
            if lines[y][_x] >= lines[y][x]:
                break

        return down * up * right * left

    answer = max(max(scenic_score(i, j) for j in range(len(lines[0]))) for i in range(len(lines)))
    print(f"Part 2 answer: {answer}")


if __name__ == "__main__":
    puzzle()
