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


def m_times_appearance(nums: List[int], m: int) -> List[int]:
    fast_idx = 0
    slow_idx = 0
    while fast_idx < len(nums):
        num_to_count = nums[fast_idx]
        fast_idx, num_count = count_numbers(nums, fast_idx)
        if num_count == m:
            nums[slow_idx] = num_to_count
            slow_idx += 1
            nums[slow_idx] = num_to_count
            slow_idx += 1
        else:
            while num_count:
                nums[slow_idx] = num_to_count
                slow_idx += 1
                num_count -= 1

    return nums


print(m_times_appearance([1, 2, 2, 3, 3, 3, 4, 4, 4, 4], 3))
