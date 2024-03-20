#!/usr/bin/python3
"""0-minoperations.py"""
from collections import deque


def minOperations(n: int) -> int:
    """calculates the fewest number of operations needed to result `n` H characters in the file"""

    if not type(n) is int:
        return 0

    if n <= 1:
        return 0

    state = {'characters': 2, 'toPaste': 1, 'operations': 2}

    states_queue = deque()

    states_queue.appendleft(state)

    currently_copied = 1

    solution = n

    while len(states_queue) > 0:
        current_state = states_queue.popleft()

        characters = current_state['characters']
        toPaste = current_state['toPaste']
        operations = current_state['operations']

        if operations > solution:
            break

        if characters + toPaste <= n:
            new_state = {
                'characters': characters + toPaste,
                'toPaste': toPaste,
                'operations': operations + 1
            }

            if new_state['operations'] < solution:
                if new_state['characters'] == n:
                    solution = new_state['operations']
                else:
                    states_queue.append(new_state)

        if toPaste == currently_copied and characters * 2 <= n:
            new_state = {
                'characters': characters * 2,
                'toPaste': characters,
                'operations': operations + 2
            }

            if new_state['operations'] < solution:
                if new_state['characters'] == n:
                    solution = new_state['operations']
                else:
                    states_queue.append(new_state)

    return solution
