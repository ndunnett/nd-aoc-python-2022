from input import load_input


def puzzle():
    rucksacks = load_input(3)
    priorities = 0

    def get_priority(letter):
        if letter.islower():
            return ord(letter) - ord("a") + 1
        return ord(letter) - ord("A") + 27

    for rucksack in rucksacks:
        for letter in rucksack:
            if letter in rucksack[:int(len(rucksack) / 2)] and letter in rucksack[int(len(rucksack) / 2):]:
                priorities += get_priority(letter)
                break

    print(f"Part 1 answer: {priorities}")

    priorities = 0

    for i in range(0, len(rucksacks), 3):
        for letter in rucksacks[i]:
            if letter in rucksacks[i + 1] and letter in rucksacks[i + 2]:
                priorities += get_priority(letter)
                break

    print(f"Part 2 answer: {priorities}")


if __name__ == "__main__":
    puzzle()
