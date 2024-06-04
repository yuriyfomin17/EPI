from typing import List


def reverse_bits(num: int) -> int:
    str_arr: List[str] = list(bin(num)[2:])
    str_arr.reverse()
    return int("".join(str_arr), 2)


PRECOMPUTED_REVERSE_TABLE = [0, 1, 1, 3, 1, 5, 3, 7, 1, 9, 5, 13, 3, 11, 7, 15, 1]


# # time complexity is O(N/L) where L is the width of the words and N is the word size.
def reverse_bit_optimized(num: int) -> int:
    mask_size = 16
    mask = 0xFFFF
    return (PRECOMPUTED_REVERSE_TABLE[num & mask] << (3 * mask_size) |
            PRECOMPUTED_REVERSE_TABLE[(num >> mask_size) & mask] << 2 * mask_size |
            PRECOMPUTED_REVERSE_TABLE[(num >> 2 * mask_size) & mask] << mask_size |
            PRECOMPUTED_REVERSE_TABLE[(num >> 3 * mask_size) & mask]
            )


print(reverse_bit_optimized(4294967300))
