from collections import deque


def best_list_pureness(list, rotations):
    queue = deque(list)
    counter = 0
    best_pureness = 0
    best_rotation = 0

    while not counter > rotations:
        current_pureness = 0

        for idx in range(len(queue)):
            current_pureness += queue[idx] * idx

        if current_pureness > best_pureness:
            best_pureness = current_pureness
            best_rotation = counter

        counter += 1
        queue.rotate()

    return f"Best pureness {best_pureness} after {best_rotation} rotations"

# Test Codes

# test = ([4, 3, 2, 6], 4)
# result = best_list_pureness(*test)
# print(result)

# test = ([7, 9, 2, 5, 3, 4], 3)
# result = best_list_pureness(*test)
# print(result)

# test = ([1, 2, 3, 4, 5], 10)
# result = best_list_pureness(*test)
# print(result)