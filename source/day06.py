from input import load_input


def puzzle():
    lines = load_input(6)

    def get_unique_packet(signal, length):
        packet = []

        for i, char in enumerate(signal):
            packet += [char]

            if len(packet) > length:
                packet = packet[-length:]

            if len(packet) == length and len(set(packet)) == length:
                return i + 1

        return 0

    answer = get_unique_packet(lines[0], 4)
    print(f"Part 1 answer: {answer}")

    answer = get_unique_packet(lines[0], 14)
    print(f"Part 2 answer: {answer}")


if __name__ == "__main__":
    puzzle()
