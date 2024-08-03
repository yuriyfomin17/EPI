from typing import List


def even_number_first_odd_last(nums: List[int]) -> List[int]:
    odd_idx = len(nums) - 1
    even_idx = 0
    while even_idx < odd_idx:
        if nums[even_idx] % 2 == 0:
            even_idx += 1
        else:
            nums[even_idx], nums[odd_idx] = nums[odd_idx], nums[even_idx]
            odd_idx -= 1
    return nums

print(even_number_first_odd_last([3, 4, 5, 9, 8, 10, 6]))