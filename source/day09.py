from input import load_input


def sign(x):
    return int(max(min(x, 1), -1))


class Knot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.visited = {f"{self.x},{self.y}": True}
        self.follower = None

    @property
    def tail(self):
        if self.follower:
            return self.follower.tail
        return self

    def add_follower(self):
        self.tail.follower = Knot()

    def move(self, dx, dy):
        for _ in range(abs(dx)):
            self.x += sign(dx)

        for _ in range(abs(dy)):
            self.y += sign(dy)

        self.visited[f"{self.x},{self.y}"] = True

        if self.follower:
            while not (abs(self.x - self.follower.x) <= 1 and abs(self.y - self.follower.y) <= 1):
                self.follower.move(sign(self.x - self.follower.x), sign(self.y - self.follower.y))

    def command(self, line):
        match line.split(" "):
            case ["U", value]:
                self.move(0, int(value))
            case ["D", value]:
                self.move(0, -int(value))
            case ["R", value]:
                self.move(int(value), 0)
            case ["L", value]:
                self.move(-int(value), 0)


def puzzle():
    lines = load_input(9)
    head = Knot()
    head.add_follower()

    for line in lines:
        head.command(line)

    answer = len(head.tail.visited.keys())
    print(f"Part 1 answer: {answer}")

    head = Knot()

    for _ in range(9):
        head.add_follower()

    for line in lines:
        head.command(line)

    answer = len(head.tail.visited.keys())
    print(f"Part 2 answer: {answer}")


if __name__ == "__main__":
    puzzle()
