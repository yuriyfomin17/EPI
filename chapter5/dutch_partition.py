from typing import List


# // Time Complexity is O(n)
# // Space Complexity is O (n)
def partition_by_pivot(nums: List[int], pivot: int):
    pivot_num = nums[pivot]
    num_less = []
    num_bigger = []
    same = []
    for el in nums:
        if el == pivot_num:
            same.append(el)
        elif el < pivot_num:
            num_less.append(el)
        elif el > pivot_num:
            num_bigger.append(el)
    return num_less + same + num_bigger


def partition_by_pivot_optimized(nums: List[int], pivot: int):
    pivot_num = nums[pivot]
    swap_marker = -1

    for curr_idx in range(pivot + 1):
        if nums[curr_idx] > pivot_num:
            continue
        swap_marker += 1
        nums[curr_idx], nums[swap_marker] = nums[swap_marker], nums[curr_idx]

    return arr

arr = [0, 1, 2, 0, 2, 1, 1]
print(partition_by_pivot_optimized(arr, 3))

print(partition_by_pivot_optimized(arr, 2))
