from typing import List


# [1, 2, 3] -> [1, 3, 2]
# [1, 3, 2] -> [2, 1, 3]

# assume array length is N, then. In the worst case, we'll need to check all elements backwards O(N)
#  find least significant place which can be replaced from its next greater num from right
def next_permutation(nums: List[int]) -> List[int]:
    idx_num_smaller = len(nums) - 1
    for idx in range(len(nums) - 1, 0, -1):
        if nums[idx] > nums[idx - 1]:
            idx_num_smaller = idx - 1
            break
    if idx_num_smaller == len(nums) - 1:
        nums.reverse()
    else:
        nums[idx_num_smaller + 1], nums[idx_num_smaller] = nums[idx_num_smaller], nums[idx_num_smaller + 1]

        nums[idx_num_smaller + 1:] = nums[idx_num_smaller + 1:][::-1]
    return nums
# nums[i] > target_num >= nums[i + 1]
#
# 9, 1, 5, 7, 4, 3, 2, 1  =>  9,1, 7, 1, 2, 3, 4,5
# max_idx = 4
# 9, 1, 4, 5, 7
# 9, 4, 1, 5, 7
print(next_permutation([1, 3, 2]))



# [4, 1, 2, 3] -> [4, 1, 3, 2]
# [4, 1, 3, 2] -> [4, 2, 1, 3]
# [4, 2, 1, 3] -> [4, 2, 3, 1]
# [4, 2, 3, 1] -> [4, 3, 1, 2]
# [4, 3, 1, 2] -> [4, 3, 2, 1]
#
# [9, 1, 5, 7, 4] -> [9, 1, 7, 4, 5] -> [9, 1, 7, 5, 4] -> [9, 4, 1, 5, 7]
# [9, 4, 1, 5, 7] -> [9, 4, 1, 7, 5] -> [9, 4, 5, 1, 7] ->  [9, 4, 5, 7, 1]
# [9, 4, 5, 7, 1] -> [9, 4, 7, 1, 5]
def generate_all_combinations(nums: List[int], taken: List[bool], curr_ans: List[int], res: List[str]):
    if len(curr_ans) == len(nums):
        res.append(",".join([str(el) for el in curr_ans]))
        return
    for idx, el in enumerate(nums):
        if taken[idx]: continue
        taken[idx] = True
        curr_ans.append(el)
        generate_all_combinations(nums, taken, curr_ans, res)
        taken[idx] = False
        curr_ans.pop()


def find_next_permutations(nums: List[int]) -> List[int]:
    res = []
    taken = [False, False, False]
    generate_all_combinations(nums, taken, [], res)
    # res.sort()
    key = ",".join([str(el) for el in nums])

    i = 0
    while i < len(res) and res[i] != key:
        i += 1
    next_str_permutation: str = res[(i + 1) % len(res)]
    return [int(el) for el in next_str_permutation.split(",")]

# print(find_next_permutations([3, 2, 1]))
