#!/usr/bin/python3
""" 0-lockboxes.py """

def canUnlockAll(boxes):
    """ start of code """
    visited = set()
    visited.add(0)

    stack = [0]

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if key not in visited and key < len(boxes):
                stack.append(key)
                visited.add(key)

    return len(visited) == len(boxes)

if __name__ == "__main__":
    boxes1 = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes1))

    boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes2))

    boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes3))
