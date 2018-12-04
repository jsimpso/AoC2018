#!/usr/bin env python


def part1(puzzle_input):
    return sum(puzzle_input)


def part2(puzzle_input):
    results = [0]
    i = 0
    while True:
        for x in puzzle_input:
            i += x
            if i not in results:
                results.append(i)
            else:
                return i


if __name__ == "__main__":
    puzzle_input = list()
    with open('input/day1.txt') as openfile:
        x = openfile.read()
        for num in x.split("\n"):
            puzzle_input.append(int(num))
    print("Part 1 solution: {part_one}".format(part_one=part1(puzzle_input)))
    print("Part 2 solution: {part_two}".format(part_two=part2(puzzle_input)))
