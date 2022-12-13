from copy import deepcopy
import re
from functools import reduce
from input import load_input


class Monkey:
    def __init__(self, string):
        self.items = [int(match.strip()) for match in re.search(r"(?:Starting items:)(.*)", string).group(1).split(",")]
        self.operation = lambda _: _
        exec("self.operation = lambda old: " + re.search(r"(?:Operation: new = )(.*)", string).group(1).strip())
        self.test = int(re.search(r"(?:Test: divisible by)(.*)", string).group(1))
        self.true = int(re.search(r"(?:If true: throw to monkey)(.*)", string).group(1))
        self.false = int(re.search(r"(?:If false: throw to monkey)(.*)", string).group(1))
        self.inspections = 0


def puzzle():
    lines = load_input(11)
    monkeys_orig = [Monkey(match.strip()) for match in re.split(r"Monkey [\d]+:", "".join(lines)) if match]
    modulus = reduce(lambda x, y: x * y, [monkey.test for monkey in monkeys_orig])
    monkeys = deepcopy(monkeys_orig)

    for _ in range(20):
        for monkey in monkeys:
            for item in monkey.items:
                worry = monkey.operation(item) // 3
                monkeys[monkey.true if worry % monkey.test == 0 else monkey.false].items.append(worry)
            monkey.inspections += len(monkey.items)
            monkey.items.clear()

    inspections = sorted([monkey.inspections for monkey in monkeys], reverse=True)
    answer = inspections[0] * inspections[1]
    print(f"Part 1 answer: {answer}")

    monkeys = deepcopy(monkeys_orig)

    for _ in range(10000):
        for monkey in monkeys:
            for item in monkey.items:
                worry = monkey.operation(item) % modulus
                monkeys[monkey.true if worry % monkey.test == 0 else monkey.false].items.append(worry)
            monkey.inspections += len(monkey.items)
            monkey.items.clear()

    inspections = sorted([monkey.inspections for monkey in monkeys], reverse=True)
    answer = inspections[0] * inspections[1]
    print(f"Part 2 answer: {answer}")


if __name__ == "__main__":
    puzzle()
