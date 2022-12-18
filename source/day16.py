import re
from functools import cache
from input import load_input


def puzzle():
    lines = load_input(16)
    regex = re.compile(r"\s(\w\w)\s.*=(\d+).*valves?\s(.*)")
    search_results = [regex.search(line).groups() for line in lines]
    rates = {search[0]: int(search[1]) for search in search_results if int(search[1]) > 0}
    neighbours = {search[0]: set(search[2].split(", ")) for search in search_results}
    valves = neighbours.keys()

    @cache
    def dijkstra(source, destination):
        visited = set(source)
        distance = {valve: 2 ** 30 for valve in valves} | {source: 0}
        path = {valve: [] for valve in valves}
        position = source

        while len(visited) < len(valves):
            for neighbour in neighbours[position]:
                if neighbour not in visited and distance[position] + 1 < distance[neighbour]:
                    distance[neighbour] = distance[position] + 1
                    path[neighbour] = path[position] + [neighbour]

            if position == destination:
                break

            visited.add(position)
            min_distance = 2 ** 30

            for valve in valves:
                if distance[valve] < min_distance and valve not in visited:
                    min_distance = distance[valve]
                    position = valve

        return len(path[destination])

    @cache
    def valve_index(valve):
        return sum(2 ** i for i, _valve in enumerate(rates.keys()) if _valve == valve)

    def find_paths(last_valve, opened, current_flow, time, result):
        if opened in result:
            result[opened] = max(result[opened], current_flow)
        else:
            result[opened] = current_flow

        for valve, rate in rates.items():
            if opened & valve_index(valve) or valve == last_valve:
                continue

            time_left = time - dijkstra(last_valve, valve) - 1

            if time_left > 0:
                find_paths(valve, opened | valve_index(valve), current_flow + rate * time_left, time_left, result)

        return result

    paths = find_paths("AA", 0, 0, 30, {})
    answer = max(paths.values())
    print(f"Part 1 answer: {answer}")

    paths = find_paths("AA", 0, 0, 26, {})
    answer = max(flow_1 + flow_2 for state_1, flow_1 in paths.items() for state_2, flow_2 in paths.items() if not state_1 & state_2)
    print(f"Part 2 answer: {answer}")


if __name__ == "__main__":
    puzzle()
