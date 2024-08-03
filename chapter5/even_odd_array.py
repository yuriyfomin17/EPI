from typing import List


def even_odd_array(curr_arr: List[int]) -> List[int]:
    even_idx, odd_idx = 0, len(curr_arr) - 1
    while even_idx < odd_idx:
        if curr_arr[even_idx] % 2 == 0:
            even_idx += 1
        else:
            curr_arr[even_idx], curr_arr[odd_idx] = curr_arr[odd_idx], curr_arr[even_idx]
            odd_idx -= 1
    return curr_arr


arr = [1, 10, 9, 8, 7, 6, 2, 3, 4, 5]

print(even_odd_array(arr))
