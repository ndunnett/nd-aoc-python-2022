from copy import deepcopy
from functools import reduce
from input import load_input


class Node:
    def __init__(self, x, y, char):
        self.x = x
        self.y = y
        self.char = char
        self.dist = 10**10
        self.visited = False

        if char == "E":
            self.value = ord("z") - ord("a")
        elif char == "S":
            self.value = ord("z") - ord("a")
        else:
            self.value = ord(char) - ord("a")


def puzzle():
    lines = load_input(12)
    nodes = reduce(lambda a, b: a + b, [[Node(x, y, char) for x, char in enumerate(line)] for y, line in enumerate(lines)], [])

    def index_in_limits(index):
        return index[0] >= 0 and index[0] < len(lines[0]) and index[1] >= 0 and index[1] < len(lines)

    def next_node(nodes):
        min_dist = 10**10
        min_node = None

        for node in nodes:
            if node.dist < min_dist and not node.visited:
                min_dist = node.dist
                min_node = node

        return min_node

    def dijkstra(nodes, start_char, target_char):
        paths = []

        for _node in nodes:
            if _node.char == start_char:
                for __node in nodes:
                    __node.dist = 10**10
                    __node.visited = False

                node = _node
                target = None

                for _node in nodes:
                    if _node.char == target_char:
                        target = _node

                node.dist = 0

                for _ in range(len(nodes)):
                    node.visited = True
                    indices = [index for index in [(node.x, node.y - 1), (node.x, node.y + 1), (node.x - 1, node.y), (node.x + 1, node.y)] if index_in_limits(index)]
                    neighbours = [neighbour for neighbour in [nodes[index[0] + index[1] * len(lines[0])] for index in indices] if neighbour.value <= node.value + 1]

                    for neighbour in neighbours:
                        if not neighbour.visited and node.dist + 1 < neighbour.dist:
                            neighbour.dist = node.dist + 1

                    node = next_node(nodes)

                    if not node or target.visited:
                        break

                paths += [target.dist]

        return min(paths)

    answer = dijkstra(deepcopy(nodes), "S", "E")
    print(f"Part 1 answer: {answer}")

    answer = dijkstra(deepcopy(nodes), "a", "E")
    print(f"Part 2 answer: {answer}")


if __name__ == "__main__":
    puzzle()
