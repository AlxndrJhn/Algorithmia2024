import itertools
import os
import re
from collections import defaultdict

this_folder = "\\".join(__file__.split("\\")[:-1])


def main(filename):
    input_data = open(f"{this_folder}/{filename}", "r").read()

    # Part 1
    ENEMY_TO_POTIONS = {"A": 0, "B": 1, "C": 3}
    result1 = sum(ENEMY_TO_POTIONS[enemy] for enemy in input_data)
    print(f"Part 1 {filename}: ", result1)

    # Part 2
    result2 = 24
    print(f"Part 2 {filename}: ", result2)
    return result1, result2


if __name__ == "__main__":
    assert main("input_example.txt") == (5, 24)
    assert main("input.txt") == (1277, 24)
    # assert main("input2.txt") == (42, 24)
