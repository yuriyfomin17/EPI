from typing import List


def merge_sort_arr(nums: List[int]) -> List[int]:
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left_arr = merge_sort_arr(nums[: mid])
    right_arr = merge_sort_arr(nums[mid:])
    return sort(nums, left_arr, right_arr)


def sort(arr: List[int], left_arr: List[int], right_arr: List[int]) -> List[int]:
    l_idx = 0
    r_idx = 0
    idx = 0
    while l_idx < len(left_arr) and r_idx < len(right_arr):
        if left_arr[l_idx] < right_arr[r_idx]:
            arr[idx] = left_arr[l_idx]
            l_idx += 1
        else:
            arr[idx] = right_arr[r_idx]
            r_idx += 1
        idx += 1
    while l_idx < len(left_arr):
        arr[idx] = left_arr[l_idx]
        l_idx += 1
        idx += 1
    while r_idx < len(right_arr):
        arr[idx] = right_arr[r_idx]
        r_idx += 1
        idx += 1
    return arr


print(merge_sort_arr([10, 2, 1, -1, 4, 8, 6]))
