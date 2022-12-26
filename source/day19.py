import re
from input import load_input


def puzzle():
    lines = load_input(19)
    regex = re.compile(r"Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.")
    blueprints = [tuple(map(int, x)) for x in [regex.search(line).groups() for line in lines]]

    def simulate(blueprint, time):
        _, ore_ore_cost, clay_ore_cost, obs_ore_cost, obs_clay_cost, geo_ore_cost, geo_obs_cost = blueprint
        states = [(1, 1, 0, 0, 0, 0, 0, 0, 0)]
        visited = dict()
        best_geo = 0

        max_ore = (ore_ore_cost + clay_ore_cost + obs_ore_cost + geo_ore_cost) * 1.5
        max_clay = obs_clay_cost * 1.5
        max_obs = geo_obs_cost * 1.5

        while states:
            state = states.pop(0)
            time_left, ore_bots, clay_bots, obs_bots, geo_bots, ore, clay, obs, geo = state

            ore = min(ore, max_ore)
            clay = min(clay, max_clay)
            obs = min(obs, max_obs)

            key = (time_left, ore_bots, clay_bots, obs_bots, geo_bots)
            value = (ore, clay, obs, geo)

            if key in visited:
                if all(a <= b for a, b in zip(value, visited[key])):
                    continue

            if time_left >= time + 1:
                if geo > best_geo:
                    best_geo = geo
                continue

            visited[key] = value
            possible_states = []

            if ore >= geo_ore_cost and obs >= geo_obs_cost:
                next_state = time_left + 1, ore_bots, clay_bots, obs_bots, geo_bots + 1, ore - geo_ore_cost, clay, obs - geo_obs_cost, geo
                possible_states.append(next_state)

            if ore >= obs_ore_cost and clay >= obs_clay_cost and geo_bots < 7:
                next_state = time_left + 1, ore_bots, clay_bots, obs_bots + 1, geo_bots, ore - obs_ore_cost, clay - obs_clay_cost, obs, geo
                possible_states.append(next_state)

            if ore >= clay_ore_cost and geo_bots < 1:
                next_state = time_left + 1, ore_bots, clay_bots + 1, obs_bots, geo_bots, ore - clay_ore_cost, clay, obs, geo
                possible_states.append(next_state)

            if ore >= ore_ore_cost and geo_bots < 1:
                next_state = time_left + 1, ore_bots + 1, clay_bots, obs_bots, geo_bots, ore - ore_ore_cost, clay, obs, geo
                possible_states.append(next_state)

            if ore < max_ore:
                next_state = time_left + 1, ore_bots, clay_bots, obs_bots, geo_bots, ore, clay, obs, geo
                possible_states.append(next_state)

            for next_state in possible_states:
                _time_left, _ore_bots, _clay_bots, _obs_bots, _geo_bots, _ore, _clay, _obs, _geo = next_state
                states.append((_time_left, _ore_bots, _clay_bots, _obs_bots, _geo_bots, _ore + ore_bots, _clay + clay_bots, _obs + obs_bots, _geo + geo_bots))

        return best_geo

    answer = sum(blueprint[0] * simulate(blueprint, 24) for blueprint in blueprints)
    print(f"Part 1 answer: {answer}")

    answer = simulate(blueprints[0], 32) * simulate(blueprints[1], 32) * simulate(blueprints[2], 32)
    print(f"Part 2 answer: {answer}")


if __name__ == "__main__":
    puzzle()
