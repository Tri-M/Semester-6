
import random
import math
from copy import copy, deepcopy
def init():

    list = [2, 1, 5, 0, 8, 4, 10, 0, 20, 10]
    return list


def calculateCost(state):

    state1 = deepcopy(state)
    state_len = len(state1)
    num = 0
    i = 0

    while i < state_len:
        j = i + 1

        while j < state_len:

            if state1[j] < state1[i]:
                num = num + 1

            j = j + 1

        i = i + 1

    return num



def simuAnneal(current_state, current_value):

    for i in range(len(current_state)):

        for j in range(i + 1, len(current_state)):
            current_state[i], current_state[j] = current_state[j], current_state[i]
            new_value = calculateCost(current_state)

            if new_value > current_value:
                return simuAnneal(current_state, new_value)

            elif new_value == current_value:
                rand = random.uniform(0, 1)
                delta_e = -1
                prob = math.exp(delta_e)

                if rand <= prob:
                    return simuAnneal(current_state, new_value)

            elif new_value < current_value:
                rand = random.uniform(0, 1)
                delta_e = new_value - current_value
                prob = math.exp(delta_e)

                if rand <= prob:
                    return simuAnneal(current_state, new_value)

    return current_state, None


# goal test
def goalTest(state1):

    if calculateCost(state1) == 0:
        return True

    else:
        return False


# main
state = init()
value3 = calculateCost(state)

while not goalTest(state):

    state, value = simuAnneal(state, value3)

    if value is None:
        break

print("Simulated Annealing:", state)

