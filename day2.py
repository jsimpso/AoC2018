#!/usr/bin env python
from collections import Counter

def part1(puzzle_input):
    twos = 0
    threes = 0
    for string in puzzle_input:
        counter = Counter(string)
        if any(counter[x] == 2 for x in counter):
            twos += 1

        if any(counter[x] == 3 for x in counter):
            threes += 1

    return twos * threes

def part2(puzzle_input):
    return i


if __name__ == "__main__":
    with open('input/day2.txt') as openfile:
        puzzle_input = [x for x in openfile.read().split("\n")]

    print("Part 1 solution: {part_one}".format(part_one=part1(puzzle_input)))
    # print("Part 2 solution: {part_two}".format(part_two=part2(puzzle_input)))
