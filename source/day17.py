from input import load_input


def puzzle():
    stream = load_input(17)[0]

    def solve(rocks):
        structure = []
        floor = [0] * 7
        stream_index = 0

        for rock in range(rocks):
            match rock % 5:
                case 0: shape = [0b0011110, 0b0000000, 0b0000000, 0b0000000] # _
                case 1: shape = [0b0001000, 0b0011100, 0b0001000, 0b0000000] # +
                case 2: shape = [0b0011100, 0b0000100, 0b0000100, 0b0000000] # _|
                case 3: shape = [0b0010000, 0b0010000, 0b0010000, 0b0010000] # |
                case 4: shape = [0b0011000, 0b0011000, 0b0000000, 0b0000000] # []

            height = max(floor) + 5
            structure += [0b0000000] * (4 + height - len(structure))
            at_rest = False

            while not at_rest:
                height -= 1
                collision = False

                match stream[stream_index]:
                    case "<":
                        for i, line in enumerate(shape):
                            if line & 1 << 6 or line << 1 & structure[height + i]:
                                collision = True
                                break

                        if not collision:
                            for i, line in enumerate(shape):
                                shape[i] <<= 1

                    case ">":
                        for i, line in enumerate(shape):
                            if line & 1 << 0 or line >> 1 & structure[height + i]:
                                collision = True
                                break

                        if not collision:
                            for i, line in enumerate(shape):
                                shape[i] >>= 1

                stream_index = (stream_index + 1) % len(stream)

                if height <= 1:
                    at_rest = True
                else:
                    for i, line in enumerate(shape):
                        if line & structure[height + i - 1]:
                            at_rest = True
                            break

            for i, line in enumerate(shape):
                structure[i + height] |= line

                for j in range(7):
                    if line & 1 << j:
                        floor[j] = max(floor[j], i + height)

        return max(floor)

    print(f"Part 1 answer: {solve(2022)}")

    rocks = 1000000000000
    cycle_length = 5 * (len(stream) + 1)
    cycle_found = False

    while not cycle_found:
        height = 0
        diff = []

        for i in range(6):
            new_height = solve(cycle_length * (i + 1))
            diff += [height - new_height]
            height = new_height

        if sum(diff[1:]) == diff[1] * (len(diff) - 1):
            break

        cycle_length += 1

    remainder = rocks % cycle_length
    number_of_cycles = (rocks - remainder) // cycle_length
    answer = (solve(cycle_length * 2) - solve(cycle_length)) * number_of_cycles + solve(remainder)
    print(f"Part 2 answer: {answer}")


if __name__ == "__main__":
    puzzle()
