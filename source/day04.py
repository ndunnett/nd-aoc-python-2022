import re
from input import load_input


def puzzle():
    lines = load_input(4)
    regex = re.compile(r"(?P<A1>[\d]+)(?:[-])(?P<A2>[\d]+)(?:[,])(?P<B1>[\d]+)(?:[-])(?P<B2>[\d]+)")
    answer = 0

    for line in lines:
        search = regex.search(line)

        A1 = int(search.group("A1"))
        A2 = int(search.group("A2"))
        B1 = int(search.group("B1"))
        B2 = int(search.group("B2"))

        if (A2 <= B2 and A1 >= B1) or (A2 >= B2 and A1 <= B1):
            answer += 1

    print(f"Part 1 answer: {answer}")

    answer = 0

    for line in lines:
        search = regex.search(line)

        A1 = int(search.group("A1"))
        A2 = int(search.group("A2"))
        B1 = int(search.group("B1"))
        B2 = int(search.group("B2"))

        if (A1 >= B1 and A1 <= B2) or (A2 >= B1 and A2 <= B2) or (B1 >= A1 and B1 <= A2) or (B2 >= A1 and B2 <= A2):
            answer += 1

    print(f"Part 2 answer: {answer}")


if __name__ == "__main__":
    puzzle()
