#!/usr/bin/env python3

from itertools import combinations
import itertools
import drawing_module
import matplotlib.pyplot as plt
import copy

# from itertools import combinations
import pathlib
import numpy as np
import os
import logging
import time
import argparse
from drawing_module import draw_pandas_machine
import jobs

animation_arr = []


def static_vars(**kwargs):
    def decorate(func):
        for k in kwargs:
            setattr(func, k, kwargs[k])
        return func

    return decorate


#
# formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
#
#
# def setup_logger(name, log_file, level=logging.DEBUG):
#    """To setup as many loggers as you want"""
#
#    handler = logging.FileHandler(log_file)
#    handler.setFormatter(formatter)
#    logger = logging.getLogger(name)
#    logger.setLevel(level)
#    logger.addHandler(handler)
#
#    return logger


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
    sum_arr = [len(arr) for arr in machine]
    for index in range(2, m):
        if sum_arr[index] > k:
            return False
    return True


@static_vars(total_steps_taken=0)
def send_data_to_logger(
        machine, from_machine_index, to_machine_index,
        moved_num, machine_with_id, type_of_action
):
    logger2.debug(
        "--------------------------------------------------------------")
    if type_of_action == "exchange":
        logger2.debug("The type of action is exchange")
    if type_of_action == "move":
        logger2.debug("The type of action is move")

    logger2.debug("Successful replaced with min")
    send_data_to_logger.total_steps_taken += 1
    logger2.debug("This is step number:  " +
                  str(send_data_to_logger.total_steps_taken))
    logger2.debug("Current Machine distrbute jobs :")
    logger2.debug(machine)
    sum_of_each_machine = [sum(any_machine) for any_machine in machine]
    logger2.debug("Current Machine distrbute sum :")
    logger2.debug(sum_of_each_machine)
    number_of_jobs_per_machine = [len(any_machine) for any_machine in machine]
    logger2.debug("How many jobs each machine has :")
    logger2.debug(number_of_jobs_per_machine)
    logger2.debug("Current move from machine: " + str(from_machine_index))
    logger2.debug("To machine: " + str(to_machine_index))
    logger2.debug("The Moved job has a weight of " + str(moved_num))
    current_score, sub_score = evaluate_solution(machine)
    logger2.debug("The Maximum machine has total weight of: " +
                  str(current_score))
    logger2.debug("The machines has subscore squares of : " + str(sub_score))
    logger2.debug("Current machines")
    logger2.debug(str(machine_with_id))


def move_toward_score(machine, min_score, m, k, machine_with_id):
    highest_bin_index = get_highest_bin_index(machine)
    for move_to_index in [i for i in range(m) if m != highest_bin_index]:
        for moved_num in sorted(machine[highest_bin_index]):  # reverse=True
            if not move(machine[highest_bin_index], machine[move_to_index], moved_num):
                print("Problem with move")
            if is_valid(machine, m, k):
                step_score = evaluate_solution(machine)
                # print(machine_with_id)
                # print(machine)
                if step_score == min_score:
                    send_data_to_logger(
                        machine,
                        highest_bin_index,
                        move_to_index,
                        moved_num,
                        machine_with_id,
                        "move",
                    )
                    machine_with_id.move(
                        highest_bin_index, move_to_index, moved_num)
                    clone_machine = copy.deepcopy(machine)
                    animation_arr.append(clone_machine)

                    return machine

            if not move(machine[move_to_index], machine[highest_bin_index], moved_num):
                print("Problem with move")
    print("Failed replaced with min")
    return machine


def local_search_example1(machine, m, k, machine_with_id):
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
    move_toward_score(machine, min_score, m, k, machine_with_id)
    local_search_example1(machine, m, k, machine_with_id)


def exchange_search_sol(machine, m, k, machine_with_id):
    """
    Exchanges jobs between machines , return the new machines split and True if changed
    False if didn't change anything
    Example of usage:
    exchange_search_sol([[1,2,3],[3,4,4]],2,4,[])
    output:
    ([[1, 2, 3], [4, 4, 3]], True)
    exchange_search_sol([[1,2,3],[1,2,3],[3,4],[5,6]],4,2,[])
    output:
    ([[3, 1, 5], [1, 2, 3], [3, 4], [6, 2]], True)
    """
    current_score = evaluate_solution(machine)
    min_score = evaluate_solution(machine)
    for machine1, machine2 in combinations(range(len(machine)), 2):
        for job1, job2 in itertools.product(machine[machine1], machine[machine2]):
            if not exchange(machine[machine1], machine[machine2], job1, job2):
                print("Fail to move ")
            if is_valid(machine, m, k):
                step_score = evaluate_solution(machine)
                if step_score < min_score:
                    print("Found minimum with exchange")
                    print(machine)
                    min_score = step_score
            if not exchange(machine[machine1], machine[machine2], job2, job1):
                print("Fail to move ")
    if min_score == current_score:
        return machine, False
    machine = exchange_toward_score(machine, min_score, m, k, machine_with_id)
    return machine, True
    # exchange_search_sol(machine, m, k, machine_with_id)


def exchange_toward_score(machine, min_score, m, k, machine_with_id):
    current_score = evaluate_solution(machine)
    machine_step = copy.deepcopy(machine)
    for machine1, machine2 in combinations(range(len(machine)), 2):
        for job1, job2 in itertools.product(machine[machine1], machine[machine2]):
            if not exchange(machine[machine1], machine[machine2], job1, job2):
                print("Fail to move ")
            if is_valid(machine, m, k):
                step_score = evaluate_solution(machine)
                if step_score == min_score:
                    send_data_to_logger(
                        machine,
                        machine1,  # Number of machine to exchange
                        machine2,  # number of machine to exchange
                        (job1, job2),
                        machine_with_id,
                        "exchange",
                    )
                    print("Replace minimum with exchange")
                    print(machine)
                    min_score = step_score
                    machine_with_id.exchange(machine1, machine2, job1, job2)
                    clone_machine = copy.deepcopy(machine)
                    animation_arr.append(clone_machine)
                    print("Job1 is :", job1)
                    print("Job2 is :", job2)
                    return machine

            if not exchange(machine[machine1], machine[machine2], job2, job1):
                print("Fail to move ")

# m = 4
# machine = [[3, 2, 2, 4, 3, 7], [], [], []]
# local_search_example1(machine)
# print(machine)


def create_instance(
    name_directory,
    input_path,
    visualize_simple_bool,
    create_animation_flag,
    logger1_temp,
    logger2_temp,
):
    """
    example of input_path is "test/input/input.py"
    """
    # m = 6
    # k = 5
    # processing_arr = [2, 3, 3, 4, 4, 4, 5, 5, 5, 5]
    global logger1
    global logger2
    logger1 = logger1_temp
    logger2 = logger2_temp

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
    machine_with_id = jobs.Jobs(processing_arr, m)

    start_time = time.time()
    local_search_example1(machine, m, k, machine_with_id)

    keep_exchanging = True
    while keep_exchanging:
        machine, keep_exchanging = exchange_search_sol(machine, m, k, machine_with_id)

    end_time = time.time()
    print(machine)
    score, _ = evaluate_solution(machine)
    print(score)

    # pathlib.Path(name_directory + "/output").mkdir(parents=True, exist_ok=True)
    output_path_file = name_directory + "/output" + "/output_score.txt"

    output_cursor = open(output_path_file, "w+")
    output_cursor.write(str("Current Solution: ") + str(machine))
    output_cursor.write("\n")
    output_cursor.write("Current Score: " + str(score))
    output_cursor.write("\n")
    average_weight_to_machines = sum(processing_arr) / m
    average_weight_to_jobs = sum(processing_arr) / len(processing_arr)
    output_cursor.write(
        "Average weight per machine:  " + str(average_weight_to_machines)
    )
    output_cursor.write("\n")
    output_cursor.write("Average weight per job:  " +
                        str(average_weight_to_jobs))
    output_cursor.write("\n")
    output_cursor.write(
        "Sum of weights of all the jobs:  " + str(sum(processing_arr)))
    output_cursor.write("\n")
    output_cursor.write("The Total time taken is: " +
                        str(end_time - start_time))
    output_cursor.write("\n")
    output_cursor.write("The machine solution with Job ID is : ")
    output_cursor.write(str(machine_with_id))
    output_cursor.write("\n")

    with open(input_path) as f:
        for line in f:
            output_cursor.write(line)
    output_cursor.close()
    if visualize_simple_bool:
        draw_pandas_machine(machine)
        plt.savefig(name_directory + "/output" +
                    "/final_schedule_solution.png")
        plt.show()
    if create_animation_flag:
        file_address = name_directory + "/output" + "/animation"
        pathlib.Path(file_address).mkdir(parents=True, exist_ok=True)
        drawing_module.create_animation(file_address, animation_arr, k)
