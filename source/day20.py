from input import load_input


def puzzle():
    lines = load_input(20)

    def decrypt(mix_iterations, key):
        encrypted = [(i, int(line) * key) for i, line in enumerate(lines)]
        mixed = encrypted.copy()
        zero = (0, 0)

        for _ in range(mix_iterations):
            for (i, n) in encrypted:
                current_index = mixed.index((i, n))
                mixed.remove((i, n))
                new_index = (current_index + n + len(mixed)) % len(mixed)
                mixed.insert(new_index, (i, n))

                if n == 0:
                    zero = (i, n)

        return sum(mixed[(mixed.index(zero) + i) % len(mixed)][1] for i in [1000, 2000, 3000])

    answer = decrypt(1, 1)
    print(f"Part 1 answer: {answer}")

    answer = decrypt(10, 811589153)
    print(f"Part 2 answer: {answer}")


if __name__ == "__main__":
    puzzle()
