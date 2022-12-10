from input import load_input


class Node:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.children = []
        self.type = "node"

    @property
    def total_size(self):
        return self.size + sum(child.total_size for child in self.children)

    def add_file(self, path, name, size):
        if len(path) == 0:
            self.children += [File(name, size)]
            return

        next_path = path.copy()
        directory = next_path.pop(0)

        for child in self.children:
            if child.name == directory:
                child.add_file(next_path, name, size)
                return

    def add_dir(self, path, name):
        if len(path) == 0:
            self.children += [Dir(name)]
            return

        next_path = path.copy()
        directory = next_path.pop(0)

        for child in self.children:
            if child.name == directory:
                child.add_dir(next_path, name)
                return

    def __str__(self):
        return f"{self.name} ({self.type}{f', size={self.size}' if self.size > 0 else ''})"

    def print(self, indent=0):
        print(f"{''.join('  ' for _ in range(indent))}- {str(self)}")
        for child in self.children:
            child.print(indent=indent + 1)


class File(Node):
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.children = []
        self.type = "file"


class Dir(Node):
    def __init__(self, name):
        self.name = name
        self.size = 0
        self.children = []
        self.type = "dir"


class Root(Node):
    def __init__(self, name="/"):
        self.name = name
        self.size = 0
        self.children = [Dir(name)]
        self.type = "root"

    def add_file(self, path, name, size):
        next_path = path.copy()
        next_path.pop(0)
        self.children[0].add_file(next_path, name, size)

    def add_dir(self, path, name):
        next_path = path.copy()
        next_path.pop(0)
        self.children[0].add_dir(next_path, name)

    def print(self, indent=0):
        self.children[0].print(indent)


def puzzle():
    lines = load_input(7)
    root = Root()
    commands = []
    current = dict()

    for line in lines:
        tokens = line.split()

        if tokens[0] == "$":
            if current:
                commands += [current]

            current = {
                "cmd": tokens[1],
                "arg": None if len(tokens) < 3 else tokens[2],
                "out": []
            }

        else:
            current["out"] += [tokens]

    if current:
        commands += [current]

    location = []

    for command in commands:
        match command["cmd"]:
            case "cd":
                if command["arg"] == "..":
                    location.pop()
                else:
                    location += [command["arg"]]

            case "ls":
                for output in command["out"]:
                    if output[0] == "dir":
                        root.add_dir(location, output[1])
                    else:
                        root.add_file(location, output[1], int(output[0]))

    def get_dir_sizes(node):
        dir_sizes = 0

        for child in node.children:
            dir_sizes += get_dir_sizes(child)

        if node.total_size <= 100000 and node.type == "dir":
            dir_sizes += node.total_size

        return dir_sizes

    answer = get_dir_sizes(root)
    print(f"Part 1 answer: {answer}")

    disk_size = 70000000
    space_needed = 30000000

    def find_dir_to_delete(node, deficit):
        answer = disk_size

        for child in node.children:
            size = find_dir_to_delete(child, deficit)

            if size >= deficit and size < answer:
                answer = size

        if node.total_size >= deficit and node.total_size < answer and node.type == "dir":
            answer = node.total_size

        return answer

    answer = find_dir_to_delete(root, root.total_size + space_needed - disk_size)
    print(f"Part 2 answer: {answer}")


if __name__ == "__main__":
    puzzle()
