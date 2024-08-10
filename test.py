from typing import List



#
def min_of_two_and_m_freq(nums: List[int], m: int) -> List[int]:
    i = 0
    last_idx = 0
    while i < len(nums):
        num_to_count = nums[i]
        ct = 0
        while i < len(nums) and num_to_count == nums[i]:
            nums[last_idx] = nums[i]
            last_idx += 1
            ct += 1
            i += 1
        if ct == m:
            last_idx -= ct
            last_idx += min(2, m)


    while last_idx < len(nums):
        nums[last_idx] = -1
        last_idx += 1
    return nums
print(min_of_two_and_m_freq([1, 1 , 2, 3, 3, 3, 4, 4, 4, 4], 2 ))
