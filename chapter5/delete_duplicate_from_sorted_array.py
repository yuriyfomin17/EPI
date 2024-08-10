from typing import List


def delete_duplicate_from_sorted_array(nums: List[int]) -> List[int]:
    stack = []
    i = 0
    while i < len(nums):
        if len(stack) == 0 or stack[-1] != nums[i]:
            stack.append(nums[i])
        i += 1
    return stack


# Time Complexity is O(N) and space complexity is O(1)

def delete_duplicated_from_sorted_array_optimized(nums: List[int]) -> List[int]:
    last_idx = 0
    i = 1
    while i < len(nums) and last_idx < len(nums):
        if nums[last_idx] != nums[i]:
            last_idx += 1
            nums[last_idx] = nums[i]
        i += 1
    last_idx += 1
    while last_idx < len(nums):
        nums[last_idx] = -1
        last_idx += 1
    return nums


# arr = [1, 1, 2]
# print(delete_duplicated_from_sorted_array_optimized(arr))


def remove_key_from_array(nums: List[int], key: int) -> int:
    last_idx = 0
    i = 0
    while i < len(nums) and last_idx < len(nums):
        if nums[i] != key:
            nums[last_idx] = nums[i]
            last_idx += 1

        i += 1
    while last_idx < len(nums):
        nums[last_idx] = -1
        last_idx += 1
    return last_idx


def count_numbers(nums: List[int], start_idx: int):
    num_to_count = nums[start_idx]
    i = start_idx
    ct = 0
    while i < len(nums) and num_to_count == nums[i]:
        ct += 1
        i += 1
    return i, ct


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


print(min_of_two_and_m_freq([1, 2, 2, 3, 3, 3, 4, 4, 4, 4], 3))
