import re
from ast import literal_eval
from input import load_input


def puzzle():
    lines = load_input(13)

    def compare(left, right):
        if not isinstance(left, list) and not isinstance(right, list):
            if left < right:
                return True

            if left > right:
                return False

        if not isinstance(left, list):
            left = [left]

        if not isinstance(right, list):
            right = [right]

        for i in range(min(len(left), len(right))):
            if left[i] != right[i]:
                return compare(left[i], right[i])

        return len(left) < len(right)

    answer = 0
    groups = re.findall(r"(\[.*\])(?:\n)(\[.*\])", "".join(lines))

    for i, (left, right) in enumerate(groups):
        if compare(literal_eval(left), literal_eval(right)):
            answer += i + 1

    print(f"Part 1 answer: {answer}")

    packets = [literal_eval(line.strip()) for line in lines if len(line.strip()) > 0] + [[[2]], [[6]]]
    two, six = 0, 0

    for i in range(len(packets)):
        no_change = True

        for j in range(len(packets) - i - 1):
            if not compare(packets[j], packets[j + 1]):
                packets[j], packets[j + 1] = packets[j + 1], packets[j]
                no_change = False

        if no_change:
            break

    for i, packet in enumerate(packets):
        if packet == [[2]]:
            two = i + 1
        elif packet == [[6]]:
            six = i + 1

    print(f"Part 2 answer: {two * six}")


if __name__ == "__main__":
    puzzle()
