# Time complexity O(n) where n is the size of the word
def compute_parity(num: int) -> int:
    parity = 0
    while num:
        parity ^= (num & 1)
        num >>= 1
    return parity


# Time complexity O(k) where k is number of bit in word
def compute_parity_optimized(num: int) -> int:
    parity = 0
    while num:
        parity ^= 1
        num &= num - 1
    return parity


# time complexity is log n where n is the size of the word
def compute_parity_optimized_xor(num: int) -> int:
    num ^= num >> 32
    num ^= num >> 16
    num ^= num >> 8
    num ^= num >> 4
    num ^= num >> 2
    num ^= num >> 1
    return num & 1


print(compute_parity_optimized_xor(9))

PRE_COMPUTED_PARITY = [0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1]


# time complexity is O(N/L) where L is the width of the words and N is the word size.
def compute_parity_with_lookup_table(num: int) -> int:
    mask_size = 16
    mask = 0xFFFF
    return (PRE_COMPUTED_PARITY[(num >> (3 * mask_size)) & mask] |
            PRE_COMPUTED_PARITY[(num >> (2 * mask_size)) & mask] |
            PRE_COMPUTED_PARITY[(num >> mask_size) & mask] |
            PRE_COMPUTED_PARITY[num & mask]
            )


print(compute_parity_with_lookup_table(8))
