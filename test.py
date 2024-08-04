from typing import List


def dutch_flag_partition(nums: List[int], pivot: int):
    pivot_num = nums[pivot]

    low = 0
    for curr_idx in range(len(nums)):
        if pivot_num > nums[curr_idx]:
            nums[curr_idx], nums[low] = nums[low], nums[curr_idx]
            low += 1
    high = len(nums) - 1
    for curr_idx in reversed(range(len(nums))):
        if pivot_num < nums[curr_idx]:
            nums[curr_idx], nums[high] = nums[high], nums[curr_idx]
            high -= 1


arr = [0, 1, 2, 0, 2, 1, 1]
dutch_flag_partition(arr, 2)
print(arr)


