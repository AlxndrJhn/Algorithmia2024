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
    # process in chunks of two characters at a time
    for chunk in [input_data[i : i + 2] for i in range(0, len(input_data), 2)]:
        regular_sum = sum(ENEMY_TO_POTIONS[enemy] for enemy in chunk)
        if "x" in chunk:
            result2 += regular_sum
        else:
            result2 += regular_sum + 2
    print(f"Part 2 {filename}: ", result2)
    return result1, result2


if __name__ == "__main__":
    try:
        assert main("input_example.txt") == (5, 11)
        assert main("input_example2.txt") == (22, 28)
        assert main("input.txt") == (1277, 2277)
        assert main("input2.txt") == (4053, 5653)
    except AssertionError:
        print("wrong ❌")
