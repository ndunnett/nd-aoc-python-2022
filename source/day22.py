import re
from functools import cache, reduce
from input import load_input


def puzzle():
    lines = load_input(22)

    def is_number(x):
        try:
            int(x)
            return True
        except ValueError:
            return False

    path = list(map(lambda x: x if not is_number(x) else int(x), re.findall(r"\d+|[RL]", lines[-1])))
    board = reduce(lambda a, b: a | b, [{(y, x): element for x, element in enumerate(line) if element != " "} for y, line in enumerate(lines[:-2])])

    heading = "E"
    starting_row = min(y for (y, _) in board)
    starting_col = min(x for (y, x) in board if y == starting_row)
    location = (starting_row, starting_col)

    heading_change = {
        "E": {"L": "N", "R": "S"},
        "S": {"L": "E", "R": "W"},
        "W": {"L": "S", "R": "N"},
        "N": {"L": "W", "R": "E"}
    }

    heading_score = {
        "E": 0,
        "S": 1,
        "W": 2,
        "N": 3
    }

    @cache
    def get_col_bounds(row):
        return (min(x for (y, x) in board if y == row), max(x for (y, x) in board if y == row))

    @cache
    def get_row_bounds(col):
        return (min(y for (y, x) in board if x == col), max(y for (y, x) in board if x == col))

    for movement in path:
        if isinstance(movement, int):
            for _ in range(movement):
                y, x = location
                match heading:
                    case "E":
                        (left_col, right_col) = get_col_bounds(y)
                        next_location = (y, left_col if x == right_col else x + 1)
                    case "W":
                        (left_col, right_col) = get_col_bounds(y)
                        next_location = (y, right_col if x == left_col else x - 1)
                    case "S":
                        (top_row, bot_row) = get_row_bounds(x)
                        next_location = (top_row if y == bot_row else y + 1, x)
                    case "N":
                        (top_row, bot_row) = get_row_bounds(x)
                        next_location = (bot_row if y == top_row else y - 1, x)

                if board[next_location] == ".":
                    location = next_location
        else:
            heading = heading_change[heading][movement]

    answer = 1000 * (location[0] + 1) + 4 * (location[1] + 1) + heading_score[heading]
    print(f"Part 1 answer: {answer}")

    heading = "E"
    location = (starting_row, starting_col)
    edge_length = int((len(board) / 6) ** 0.5)

    transition_1_E = {(i, edge_length * 3 - 1): ((edge_length * 3 - i - 1, edge_length * 2 - 1), "W") for i in range(edge_length)}
    transition_4_E = {(edge_length * 3 - i - 1, edge_length * 2 - 1): ((i, edge_length * 3 - 1), "W") for i in range(edge_length)}
    transition_2_E = {(edge_length + i, edge_length * 2 - 1): ((edge_length - 1, edge_length * 2 + i), "N") for i in range(edge_length)}
    transition_1_S = {(edge_length - 1, edge_length * 2 + i): ((edge_length + i, edge_length * 2 - 1), "W") for i in range(edge_length)}
    transition_5_E = {(edge_length * 3 + i, edge_length - 1): ((edge_length * 3 - 1, edge_length + i), "N") for i in range(edge_length)}
    transition_4_S = {(edge_length * 3 - 1, edge_length + i): ((edge_length * 3 + i, edge_length - 1), "W") for i in range(edge_length)}
    transition_0_W = {(i, edge_length): ((edge_length * 3 - i - 1, 0), "E") for i in range(edge_length)}
    transition_3_W = {(edge_length * 3 - i - 1, 0): ((i, edge_length), "E") for i in range(edge_length)}
    transition_2_W = {(edge_length + i, edge_length): ((edge_length * 2, i), "S") for i in range(edge_length)}
    transition_3_N = {(edge_length * 2, i): ((edge_length + i, edge_length), "E") for i in range(edge_length)}
    transition_5_W = {(edge_length * 3 + i, 0): ((0, edge_length + i), "S") for i in range(edge_length)}
    transition_0_N = {(0, edge_length + i): ((edge_length * 3 + i, 0), "E") for i in range(edge_length)}
    transition_5_S = {(edge_length * 4 - 1, i): ((0, edge_length * 2 + i), "S") for i in range(edge_length)}
    transition_1_N = {(0, edge_length * 2 + i): ((edge_length * 4 - 1, i), "N") for i in range(edge_length)}

    transitions = {
        "E": transition_1_E | transition_2_E | transition_4_E | transition_5_E,
        "W": transition_0_W | transition_2_W | transition_3_W | transition_5_W,
        "S": transition_1_S | transition_4_S | transition_5_S,
        "N": transition_0_N | transition_1_N | transition_3_N
    }

    for movement in path:
        if isinstance(movement, int):
            for _ in range(movement):
                y, x = location
                next_heading = heading

                match heading:
                    case "E":
                        if location in transitions[heading]:
                            next_location, next_heading = transitions[heading][location]
                        else:
                            next_location = (y, x + 1)
                    case "W":
                        if location in transitions[heading]:
                            next_location, next_heading = transitions[heading][location]
                        else:
                            next_location = (y, x - 1)
                    case "S":
                        if location in transitions[heading]:
                            next_location, next_heading = transitions[heading][location]
                        else:
                            next_location = (y + 1, x)
                    case "N":
                        if location in transitions[heading]:
                            next_location, next_heading = transitions[heading][location]
                        else:
                            next_location = (y - 1, x)

                if board[next_location] == ".":
                    location = next_location
                    heading = next_heading
        else:
            heading = heading_change[heading][movement]

    answer = 1000 * (location[0] + 1) + 4 * (location[1] + 1) + heading_score[heading]
    print(f"Part 2 answer: {answer}")


if __name__ == "__main__":
    puzzle()
