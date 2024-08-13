from typing import List


# 6, 2, 1, 5, 4, 3, 0

# 6, 2, 3, 0, 1, 4, 5

# 6, 2, 3, 5, 4, 1, 0
def next_permutation(perm: List[int]) -> List[int]:
    # TODO - you fill in here.

    inversion_point = len(perm) - 2
    while inversion_point >= 0 and perm[inversion_point] >= perm[inversion_point + 1]:
        inversion_point -= 1
    if inversion_point == -1:
        return []
    first_greatest_element = len(perm) - 1
    for i in reversed(range(len(perm))):
        if perm[i] > perm[inversion_point]:
            first_greatest_element = i
            break
    perm[inversion_point], perm[first_greatest_element] = perm[first_greatest_element], perm[inversion_point]
    perm[inversion_point + 1:] = reversed(perm[inversion_point + 1:])
    return perm


def previous_permutation(perm: List[int]) -> List[int]:
    inversion_point = len(perm) - 2
    while inversion_point >= 0 and perm[inversion_point] <= perm[inversion_point + 1]:
        inversion_point -= 1
    if inversion_point == -1:
        return []
    perm[inversion_point + 1:] = reversed(perm[inversion_point + 1:])
    first_smallest_element = inversion_point + 1
    for i in range(inversion_point + 1, len(perm)):
        if perm[inversion_point] >= perm[i]:
            first_smallest_element = i
            break
    perm[inversion_point], perm[first_smallest_element] = perm[first_smallest_element], perm[inversion_point]
    return perm


print(previous_permutation([6, 2, 3, 0, 1, 4, 5]))
print(previous_permutation([3, 2, 1]))
