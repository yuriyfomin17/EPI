from typing import List


# A = [a, b, c, d] P = [2, 0, 1, 3]
# 0
# A = [c, b, a, d] P = [1, 0, 2, 3]
#
# A = [b, c, a, d] p = [0, 1, 2, 3]

# Time complexity is O(N), since with each iteration it moves at least one element
# to its permuted location
# Space Complexity is O(N) since permutation array is modified
def apply_permutation(nums: List[str], permutation: List[int]):
    for i in range(len(nums)):
        while i != permutation[i]:
            next_idx = permutation[i]
            nums[i], nums[next_idx] = nums[next_idx], nums[i]
            permutation[i], permutation[next_idx] = permutation[next_idx], permutation[i]
    print(nums, permutation)


# apply_permutation(['a', 'b', 'c', 'd'], [2, 0, 1, 3])

# A = [a, b, c, d] P = [2, 0, 1, 3]
# 0
# A = [_, b, a, d] => c in variable
# A = [_, c, a, d] => b in variable
# A = [b, c, a, d]
# Time complexity is O(N) and space complexity is O(1)
def apply_permutation_optimized(nums: List[str], permutation: List[int]):
    for i in range(len(nums)):
        start_idx = i
        variable = nums[i]
        while permutation[start_idx] >= 0:
            next_idx = permutation[start_idx]
            next_variable = nums[next_idx]
            nums[next_idx] = variable

            variable = next_variable

            permutation[start_idx] = -1
            start_idx = next_idx

    print(nums)


apply_permutation_optimized(['a', 'b', 'c', 'd'], [2, 0, 1, 3])
