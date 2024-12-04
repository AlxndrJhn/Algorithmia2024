import itertools
import os
import re
from collections import defaultdict
from unittest import result

this_folder = "\\".join(__file__.split("\\")[:-1])


def main(filename):
    input_data = open(f"{this_folder}/{filename}", "r").read()

    # Part 1
    ENEMY_TO_POTIONS = {"A": 0, "B": 1, "C": 3, "x": 0, "D": 5}
    result1 = sum(ENEMY_TO_POTIONS[enemy] for enemy in input_data)
    print(f"Part 1 {filename}: ", result1)

    # Part 2
    result2 = 0
    for chunk in [input_data[i : i + 2] for i in range(0, len(input_data), 2)]:
        regular_sum = sum(ENEMY_TO_POTIONS[enemy] for enemy in chunk)
        if "x" in chunk:
            result2 += regular_sum
        else:
            result2 += regular_sum + 2
    print(f"Part 2 {filename}: ", result2)

    # Part 3
    CHUNK_SIZE = 3
    result3 = 0
    for chunk in [
        input_data[i : i + CHUNK_SIZE] for i in range(0, len(input_data), CHUNK_SIZE)
    ]:
        x_count = chunk.count("x")
        monster_count = CHUNK_SIZE - x_count
        regular_sum = sum(ENEMY_TO_POTIONS[enemy] for enemy in chunk)
        if monster_count == 0:
            result3 += 0
        elif monster_count == 1:
            result3 += regular_sum
        elif monster_count == 2:
            result3 += regular_sum + 2
        else:
            result3 += regular_sum + 6
    print(f"Part 3 {filename}: ", result3)

    return result1, result2, result3


if __name__ == "__main__":
    try:
        assert main("input_example.txt") == (5, 11, 17)
        assert main("input_example2.txt") == (22, 28, 38)
        assert main("input_example3.txt") == (16, 22, 30)
        assert main("input.txt") == (1277, 2277, 3281)
        assert main("input2.txt") == (4053, 5653, 7263)
        assert main("input3.txt") == (16377, 22179, 27951)
    except AssertionError:
        print("wrong ❌")
