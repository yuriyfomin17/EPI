from typing import List


def swap_bits(num: int, i: int, j: int) -> int:
    num_str: List[str] = list(bin(num)[2:])
    if (
            i >= len(num_str) or
            j >= len(num_str) or
            num_str[i] == num_str[j]
    ): return num
    temp = num_str[i]
    num_str[i] = num_str[j]
    num_str[j] = temp
    num_str.reverse()
    return int("".join(num_str), 2)


# time complexity O(1)
def swap_bits_optimized(num: int, i: int, j: int) -> int:
    if (num >> i) & 1 != (num >> j) & 1:
        bit_mask = 1 << i | 1 << j
        return num ^ bit_mask
    return num


print(swap_bits_optimized(73, 1, 6))
