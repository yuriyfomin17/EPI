from typing import List


def sort_seq(nums: List[int], start: int, end: int):
    pivot_num = nums[end]
    swap_marker = start - 1
    for curr_idx in range(start, end + 1):
        if nums[curr_idx] > pivot_num:
            continue
        swap_marker += 1
        if nums[swap_marker] > nums[curr_idx]:
            nums[curr_idx], nums[swap_marker] = nums[swap_marker], nums[curr_idx]

    return swap_marker


def quick_sort(nums: List[int], start: int, end: int):
    if start >= end:
        return
    next_pivot = sort_seq(nums, start, end)
    quick_sort(nums, start, next_pivot - 1)
    quick_sort(nums, next_pivot + 1, end)


arr = [3, 2, 5, 0, 1, 8, 7, 6, 9, 4]
quick_sort(arr, 0, len(arr) - 1)
print(arr)
