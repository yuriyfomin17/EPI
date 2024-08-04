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


# time complexity O(n), space complexity O(1)

def partition_by_pivot_optimized_two_pass(nums: List[int], pivot: int):
    pivot_num = nums[pivot]
    smaller = 0
    for i in range(len(nums)):
        if nums[i] < pivot_num:
            nums[smaller], nums[i] = nums[i], nums[smaller]
            smaller += 1

    larger = len(nums) - 1
    for i in reversed(range(len(nums))):
        if nums[i] > pivot_num:
            nums[larger], nums[i] = nums[i], nums[larger]
            larger -= 1

    return nums


# time complexity O(n), space complexity O(1)
def partition_by_pivot_optimized_one_pass(nums: List[int], pivot: int):
    pivot_num = nums[pivot]
    smaller, equal, larger = 0, 0, len(nums) - 1

    while equal <= larger:
        if nums[equal] < pivot_num:
            nums[smaller], nums[equal] = nums[equal], nums[smaller]
            equal += 1
            smaller += 1
        elif nums[equal] == pivot_num:
            equal += 1
        elif nums[equal] > pivot_num:
            nums[larger], nums[equal] = nums[equal], nums[larger]
            larger -= 1


two_pass_arr = [0, 1, 2, 0, 2, 1, 1]
print(partition_by_pivot_optimized_two_pass(two_pass_arr, 3))

print(partition_by_pivot_optimized_two_pass(two_pass_arr, 2))

one_pass_arr = [-3, 0, -1, 1, 1, -5, 1, 3, 4, 2]

partition_by_pivot_optimized_one_pass(one_pass_arr, 3)
print(one_pass_arr)
