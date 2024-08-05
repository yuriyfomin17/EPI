from typing import List
import heapq


def add(a: int, b: int) -> int:
    return a if b == 0 else add(a ^ b, (a & b) << 1)


def compute_product_without_arithmetical_operation(a: int, b: int):
    neg = ((a < 0 and b > 0) or (b < 0 and a > 0))
    a = abs(a)
    b = abs(b)
    running_sum = 0
    while a:
        if a & 1:
            running_sum = add(running_sum, b)
        a, b = a >> 1, b << 1

    if neg:
        return -running_sum
    return running_sum


def compute_quotient_using_arithmetical_operation(dividend: int, divisor: int):
    negative = (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0)
    dividend = abs(dividend)
    divisor = abs(divisor)
    power = 31
    ans = 0
    while dividend >= divisor:
        while (divisor << power) > dividend:
            power -= 1

        ans += 1 << power
        dividend -= divisor << power
    if negative:
        if -ans < -2 ** 31: return -2 ** 31
        return -ans
    if ans > (2 ** 31 - 1):
        return 2 ** 31 - 1
    return ans


def find_next_pivot(nums: List[int], lo: int, hi: int) -> int:
    pivot_num = nums[hi]
    swap_marker = lo - 1
    for curr_idx in range(lo, hi + 1):
        if nums[curr_idx] > pivot_num:
            continue
        swap_marker += 1
        if nums[swap_marker] > nums[curr_idx]:
            nums[curr_idx], nums[swap_marker] = nums[swap_marker], nums[curr_idx]
    return swap_marker


def quick_select(nums: List[int], lo: int, hi: int, k: int):
    if lo >= hi:
        return
    next_pivot = find_next_pivot(nums, lo, hi)

    if k - 1 <= next_pivot:
        quick_select(nums, lo, next_pivot - 1, k)
    else:
        quick_select(nums, next_pivot + 1, hi, k)


arr = [1, 6, 3, 9, 8, 5]
k = 2
quick_select(arr, 0, len(arr) - 1, k)
print(arr)
print(arr[k - 1])