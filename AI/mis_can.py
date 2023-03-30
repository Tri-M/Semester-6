# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 09:10:33 2023

@author: 20pw39
"""

# Initial state
state = (3, 3, 1) # (missionaries_left, cannibals_left, boat_left)
# 1 boat position indicates boat is on left side 
# 0 boat position indicates boat is on right side


def checkSafe(state):
    m, c, b = state
    if m < c and m != 0:
        return False
    if (3-m) < (3-c) and (3-m) != 0:
        return False
    return True


def genNext(state):
    m, c, b = state
    if b == 1:
        for i in range(3):
            for j in range(3):
                if i + j <= 2 and i + j > 0:
                    new_m = m - i
                    new_c = c - j
                    if new_m >= 0 and new_c >= 0 and checkSafe((new_m, new_c, 0)):
                        yield (new_m, new_c, 0)
    else:
        for i in range(3):
            for j in range(3):
                if i + j <= 2 and i + j > 0:
                    new_m = m + i
                    new_c = c + j
                    if new_m <= 3 and new_c <= 3 and checkSafe((new_m, new_c, 1)):
                        yield (new_m, new_c, 1)


def dfs(state, vis):
    if state == (0, 0, 0):
        return True
    vis.append(state)
    for next_state in genNext(state):
        if next_state not in vis:
            if dfs(next_state, vis):
                print(next_state)
                return True
    return False

vis = []
if dfs(state, vis):
    print("Solution found!")
else:
    print("No solution found. ;-; ")
