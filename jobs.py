# import jobs
"""The variable __jobs = [(0,1),(1,10) , (2,131)] has (job_num,job_weight)"""

import copy


class Jobs:
    def __init__(self, jobs_arr, m):
        self.__jobs = list(enumerate(jobs_arr))
        self.__machine = [{} for i in range(m)]
        self.__machine[0].update(self.__jobs)
        # self.__machine = [[] for i in range(m - 1)]
        # self.__machine.insert(0, copy.deepcopy(self.__jobs))

    def get_key_by_value(self, current_machine, current_value):
        for key, value in current_machine.items():
            if value == current_value:
                return key
        print("Error with job.py file get_key_by_value")
        raise IndexError

    def move(self, from_machine, to_machine, job_weight_to_move):
        if job_weight_to_move not in self.__machine[from_machine].values():
            return False
        key_to_move = self.get_key_by_value(
            self.__machine[from_machine], job_weight_to_move
        )
        del self.__machine[from_machine][key_to_move]
        self.__machine[to_machine].update([(key_to_move, job_weight_to_move)])
        return True

    def exchange(self, machine1, machine2, job1_weight, job2_weight):
        if job1_weight not in self.__machine[machine1].values():
            return False
        if job2_weight not in self.__machine[machine2].values():
            return False
        key_to_move1 = self.get_key_by_value(
            self.__machine[machine1], job1_weight
        )
        key_to_move2 = self.get_key_by_value(
            self.__machine[machine2], job2_weight
        )
        del self.__machine[machine1][key_to_move1]
        del self.__machine[machine2][key_to_move2]
        self.__machine[machine1].update([(key_to_move2, job2_weight)])
        self.__machine[machine2].update([(key_to_move1, job1_weight)])
        return True

    def __str__(self):
        returned_string = ""
        for data in self.__machine:
            returned_string += '\n'
            returned_string += str(data)
        return returned_string
        #return str(self.__machine)

    def __repr__(self):
        return str(self.__machine)
