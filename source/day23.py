from functools import reduce
from input import load_input


def puzzle():
    lines = load_input(23)
    elves = set(reduce(lambda a, b: a + b, [[(row, col) for col, element in enumerate(line) if element == "#"] for row, line in enumerate(lines)]))
    movement = [
        [(-1, -1), (-1, 0), (-1, 1)],
        [(1, -1), (1, 0), (1, 1)],
        [(-1, -1), (0, -1), (1, -1)],
        [(-1, 1), (0, 1), (1, 1)]
    ]
    all_moves = set(reduce(lambda a, b: a + b, movement))
    movements = [movement[i:] + movement[:i] for i in range(len(movement))]

    def add_point(a, b):
        return (a[0] + b[0], a[1] + b[1])

    def move_elf(source, destination):
        elves.remove(source)
        elves.add(destination)

    def move_elves():
        proposed_moves = dict()
        unavailable_moves = set()

        for elf in elves:
            if all(add_point(elf, move) not in elves for move in all_moves):
                continue

            for moves in movements[move_elves.iteration % len(movements)]:
                no_neighbours = True

                for move in moves:
                    if add_point(elf, move) in elves:
                        no_neighbours = False
                        break

                if no_neighbours:
                    considered_move = add_point(elf, moves[1])

                    if considered_move in proposed_moves:
                        unavailable_moves.add(considered_move)

                    proposed_moves[considered_move] = elf
                    break

        move_elves.iteration += 1
        _ = [move_elf(elf, move) for move, elf in proposed_moves.items() if move not in unavailable_moves]
        return len(proposed_moves) > 0

    move_elves.iteration = 0

    for _ in range(10):
        move_elves()

    row_min, row_max = (rows := sorted(elf[0] for elf in elves))[0], rows[-1]
    col_min, col_max = (cols := sorted(elf[1] for elf in elves))[0], cols[-1]
    answer = (row_max - row_min + 1) * (col_max - col_min + 1) - len(elves)
    print(f"Part 1 answer: {answer}")

    while move_elves():
        pass

    answer = move_elves.iteration
    print(f"Part 2 answer: {answer}")


if __name__ == "__main__":
    puzzle()
