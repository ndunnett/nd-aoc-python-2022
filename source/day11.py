import re
from functools import reduce
from input import load_input


class Monkey:
    def __init__(self, string, relief):
        self.items = [int(match.strip()) for match in re.search(r"(?:Starting items:)(.*)", string).group(1).split(",")]
        self.relief = relief
        self.factors = [self.relief]
        self.operation = re.search(r"(?:Operation: new = )(.*)", string).group(1).strip().split(" ")

        match self.operation:
            case [_, _, "old"]: pass
            case [_, "*", factor]: self.factors += [int(factor)]
            case _: pass

        self.test = int(re.search(r"(?:Test: divisible by)(.*)", string).group(1))
        self.factors += [self.test]
        self.true = int(re.search(r"(?:If true: throw to monkey)(.*)", string).group(1))
        self.false = int(re.search(r"(?:If false: throw to monkey)(.*)", string).group(1))
        self.inspections = 0

    def operate(self, item):
        match self.operation:
            case ["old", "*", "old"]: return item * item
            case ["old", "+", "old"]: return item + item
            case ["old", "*", x]: return item * int(x)
            case ["old", "+", x]: return item + int(x)

    def inspect_item(self, item, modulus):
        self.inspections += 1
        worry = self.operate(item) // self.relief % modulus
        return (worry, self.true if worry % self.test == 0 else self.false)


def puzzle():
    lines = load_input(11)
    monkeys = [Monkey(match.strip(), 3) for match in re.split(r"Monkey [\d]+:", "".join(lines)) if match]
    modulus = reduce(lambda x, y: x * y, [factor for factors in [monkey.factors for monkey in monkeys] for factor in factors])

    for _ in range(20):
        for monkey in monkeys:
            for item in monkey.items:
                (worry, throw_to) = monkey.inspect_item(item, modulus)
                monkeys[throw_to].items += [worry]
            monkey.items.clear()

    inspections = sorted([monkey.inspections for monkey in monkeys], reverse=True)
    answer = inspections[0] * inspections[1]
    print(f"Part 1 answer: {answer}")

    monkeys = [Monkey(match.strip(), 1) for match in re.split(r"Monkey [\d]+:", "".join(lines)) if match]

    for _ in range(10000):
        for monkey in monkeys:
            for item in monkey.items:
                (worry, throw_to) = monkey.inspect_item(item, modulus)
                monkeys[throw_to].items += [worry]
            monkey.items.clear()

    inspections = sorted([monkey.inspections for monkey in monkeys], reverse=True)
    answer = inspections[0] * inspections[1]
    print(f"Part 2 answer: {answer}")


if __name__ == "__main__":
    puzzle()
