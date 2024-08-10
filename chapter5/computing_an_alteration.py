from typing import List


# Time complexity is O(N* log N)
def compute_an_alteration(nums: List[int]) -> List[int]:
    nums.sort()
    if len(nums) <= 2:
        return nums
    for i in range(len(nums) // 2):
        nums[i], nums[-2 - i] = nums[-2 - i], nums[i]
        nums[i + 1], nums[-1 - i] = nums[-1 - i], nums[i + 1]
    return nums


# 0  1  2  3  4  5  6
# 3, 2, 6, 1, 5, 7, 8
# 0
# 2, 3
# 1
# 3, 2 , 6, 1, 5, 7, 8
# 2
# 3, 2 ,6, 1, 5, 7, 8
# 3
# 3, 2 ,6, 1, 5, 7, 8
# 4
# 3, 2 ,6, 1, 7, 5, 8
# Time complexity is O(N)
def compute_an_alteration_optimized(nums: List[int]) -> List[int]:
    for i in range(len(nums)):
        nums[i: i + 2] = sorted(nums[i: i + 2], reverse=bool(i % 2))
    return nums


def compute_an_alteration_optimized_without_sorted(nums: List[int]) -> List[int]:
    for i in range(len(nums)):
        if i + 1 < len(nums):
            min_num = min(nums[i], nums[i + 1])
            max_num = max(nums[i], nums[i + 1])
            if i % 2 != 0:
                nums[i] = max_num
                nums[i + 1] = min_num
            else:
                nums[i] = min_num
                nums[i + 1] = max_num
    return nums


print(compute_an_alteration_optimized([3, 2, 6, 1, 5, 7, 8]))
print(compute_an_alteration_optimized_without_sorted([3, 2, 6, 1, 5, 7, 8]))
