import re
import copy
from input import load_input


def puzzle():
    lines = load_input(5)

    starting_stacks = {int(lines[8][i]): [lines[j][i] for j in range(7, -1, -1) if lines[j][i] != " "] for i in range(1, 34, 4)}
    moves = range(10, len(lines))
    regex = re.compile(r"(?:move\s)(?P<MOVE>[\d]+)(?:\sfrom\s)(?P<FROM>[\d]+)(?:\sto\s)(?P<TO>[\d]+)")

    stacks = copy.deepcopy(starting_stacks)
    answer = []

    for i in moves:
        search = regex.search(lines[i])
        n = int(search.group("MOVE"))
        src = int(search.group("FROM"))
        dest = int(search.group("TO"))
        stacks[dest] += [stacks[src].pop() for _ in range(0, n)]

    for crates in stacks.values():
        answer += [crates[-1]]

    print(f"Part 1 answer: {''.join(answer)}")

    stacks = copy.deepcopy(starting_stacks)
    answer = []

    for i in moves:
        search = regex.search(lines[i])
        n = int(search.group("MOVE"))
        src = int(search.group("FROM"))
        dest = int(search.group("TO"))
        stacks[dest] += reversed([stacks[src].pop() for _ in range(0, n)])

    for crates in stacks.values():
        answer += [crates[-1]]

    print(f"Part 2 answer: {''.join(answer)}")


if __name__ == "__main__":
    puzzle()
