#!/usr/bin/env python3

import drawing_module
import matplotlib.pyplot as plt
import copy

# from itertools import combinations
import pathlib
import numpy as np
import os
import logging
import argparse
from drawing_module import draw_pandas_machine

# m = 6
# k = 5
# processing_arr = [2, 3, 3, 4, 4, 4, 5, 5, 5, 5]
#
#
# processing_arr = sorted(processing_arr)
# num_jobs = len(processing_arr)
# num_machine = m
# machine = [[] for _ in range(m)]
## print(3)
#
## machine[0] = processing_arr
#
## put all jobs on machine 0
# for job, processing_time in enumerate(processing_arr):
#    machine[0].append(processing_time)


animation_arr = []


formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")


def setup_logger(name, log_file, level=logging.DEBUG):
    """To setup as many loggers as you want"""

    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger


# print(machine)
def exchange(arr1, arr2, num1, num2):
    """
    Exchanging num1 from arr1 with num2 from arr2
    False if exchange failed , True if exchange succeed
    """
    if num1 not in arr1:
        return False
    if num2 not in arr2:
        return False
    arr1.remove(num1)
    arr2.remove(num2)
    arr1.append(num2)
    arr2.append(num1)
    return True


def move(arr1, arr2, num):
    """
    Moving num from arr1 to arr2
    If num is not in arr1 returns False
    If the move was successful return True
    arr1 = [1,2,3]
    arr2 = []
    print(move(arr1 , arr2 , 2))
    print(arr1)
    print(arr2)
    >>> True
    >>> [1,3]
    >>>[2]
    """
    if num not in arr1:
        return False
    arr1.remove(num)
    arr2.append(num)
    return True


def evaluate_solution(machine):
    """
    Evaluate Solution , give score to current solution
    machine = [[1,3],[3],[2,2,2]]
    print(evaluate_solution(machine))
    """
    sum_arr = [sum(arr) for arr in machine]
    current_score = max(sum_arr)
    # sub_score_arr = [list(map(lambda a: a * a, arr)) for arr in machine]
    sub_score_arr = map(lambda a: a * a, sum_arr)
    sub_score = sum(sub_score_arr)
    # print(sub_score)
    return current_score, sub_score


def get_highest_bin_index(machine):
    sum_arr = [sum(arr) for arr in machine]
    index_max = np.argmax(sum_arr)
    return index_max


def get_all_possible_pairs_from_list(m):
    """Get all possible pairs from list
    For example
    given
    >>>get_all_possible_pairs_from_list(3)
    test_list = [0,1,2]
    print("The original list : " + str(test_list))
    res = list(combinations(test_list, 2))
    print("All possible pairs : " + str(res))

    : The original list : [0, 1, 2]
    : All possible pairs : [(0, 1), (0, 2), (1, 2)]
    """
    pass


def is_valid(machine, m, k):
    """Checks if the machine is valid"""
    sum_arr = [sum(arr) for arr in machine]
    for index in range(2, m):
        if sum_arr[index] > k:
            return False
    return True


def move_toward_score(machine, min_score, m, k):
    highest_bin_index = get_highest_bin_index(machine)
    for move_to_index in [i for i in range(m) if m != highest_bin_index]:
        for moved_num in sorted(machine[highest_bin_index]):  # reverse=True
            if not move(machine[highest_bin_index], machine[move_to_index], moved_num):
                print("Problem with move")
            if is_valid(machine, m, k):
                step_score = evaluate_solution(machine)
                if step_score == min_score:
                    # print("Successful replace with min")
                    logger2.debug("Successful replaced with min")
                    logger2.debug(machine)
                    clone_machine = copy.deepcopy(machine)
                    animation_arr.append(clone_machine)

                    return machine

            if not move(machine[move_to_index], machine[highest_bin_index], moved_num):
                print("Problem with move")
    print("Failed replaced with min")
    return machine


def local_search_example1(machine, m, k):
    current_score = evaluate_solution(machine)
    min_score = evaluate_solution(machine)
    highest_bin_index = get_highest_bin_index(machine)
    # Search for the solution
    for move_to_index in [i for i in range(m) if m != highest_bin_index]:
        for moved_num in sorted(machine[highest_bin_index]):  # reverse=True
            if not move(machine[highest_bin_index], machine[move_to_index], moved_num):
                print("Problem with move")
            if is_valid(machine, m, k):
                step_score = evaluate_solution(machine)
                if step_score < min_score:
                    # print("Found min! ")
                    #
                    logger1.debug("Found min!")
                    logger1.debug(machine)
                    min_score = step_score
            if not move(machine[move_to_index], machine[highest_bin_index], moved_num):
                print("Problem with move")
    if min_score == current_score:  # There was no local solution with improvements
        return machine
    # The actual move
    move_toward_score(machine, min_score, m, k)
    local_search_example1(machine, m, k)


# m = 4
# machine = [[3, 2, 2, 4, 3, 7], [], [], []]
# local_search_example1(machine)
# print(machine)


def create_instance(
    name_directory, input_path, visualize_simple_bool, create_animation_flag
):
    """
    example of input_path is "test/input/input.py"
    """
    # m = 6
    # k = 5
    # processing_arr = [2, 3, 3, 4, 4, 4, 5, 5, 5, 5]

    import types
    import importlib.machinery

    loader = importlib.machinery.SourceFileLoader("input", input_path)
    input_mod = types.ModuleType(loader.name)
    loader.exec_module(input_mod)

    m = input_mod.m
    k = input_mod.k
    processing_arr = input_mod.processing_arr

    processing_arr = sorted(processing_arr)
    num_jobs = len(processing_arr)
    num_machine = m
    machine = [[] for _ in range(m)]

    pathlib.Path(name_directory + "/output").mkdir(parents=True, exist_ok=True)
    # print(3)

    # machine[0] = processing_arr

    # put all jobs on machine 0
    for job, processing_time in enumerate(processing_arr):
        machine[0].append(processing_time)

    local_search_example1(machine, m, k)
    print(machine)
    score, _ = evaluate_solution(machine)
    print(score)

    # pathlib.Path(name_directory + "/output").mkdir(parents=True, exist_ok=True)
    output_path_file = name_directory + "/output" + "/output_score.txt"

    output_cursor = open(output_path_file, "w+")
    output_cursor.write(str("Current Solution: ") + str(machine))
    output_cursor.write("\n")
    output_cursor.write("Current Score: " + str(score))
    output_cursor.close()
    if visualize_simple_bool:
        draw_pandas_machine(machine)
        plt.savefig(name_directory + "/output" + "/final_schedule_solution.png")
        plt.show()
    if create_animation_flag:
        file_address = name_directory + "/output" + "/animation"
        pathlib.Path(file_address).mkdir(parents=True, exist_ok=True)
        drawing_module.create_animation(file_address, animation_arr)


def dir_path(string):
    if os.path.exists(string):
        return string
    else:
        raise NotADirectoryError(string)


# name = "test"
# name_directory = "test"

# logging.basicConfig(
#    level=logging.DEBUG,
#    format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
#    datefmt="%m-%d %H:%M",
#    filename="myapp.log",
#    filemode="w",
# )


parser = argparse.ArgumentParser("simple_example")
parser.add_argument(
    "--animation_flag",
    action="store_true",
    help="For animation add the --animation_flag flag ! ",
)
parser.add_argument(
    "--visualize_simple",
    action="store_true",
    help="For visualizing add the --visualize_simple flag ! ",
)
parser.add_argument(
    "--input_path",
    type=dir_path,
    help='path to input file for example "test/input/input.py" \n the input.py should have the format \n \
        m = 6 \n \
        k=5 \n processing_arr = [2, 3, 3, 4, 4, 4, 5, 5, 5, 5]',
    default="test/input/input.py",
)
parser.add_argument(
    "--output_dir",
    help="A path to put all the output files ",
    default="test",
    # type=dir_path,
)
args = parser.parse_args()
name = args.output_dir
logger1 = setup_logger(
    "myapp.area1", name + "/output/" + "finding_minimum_with_local_search.log"
)
# logger1 = logging.getLogger("myapp.area1")
logger2 = setup_logger(
    "myapp.area2",
    name + "/output/" + "after_finding_the_smallest_do_the_replacement.log",
)
# logger2 = logging.getLogger("myapp.area2")
# print(args.input_path)

# if args.visualize_simple:
#    print("Barak")

create_instance(
    args.output_dir, args.input_path, args.visualize_simple, args.animation_flag
)
