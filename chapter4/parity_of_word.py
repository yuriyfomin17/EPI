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

PRECOMPUTED_PARITY = []

# time complexity is O(N\L) where L is the width of the word and n is the size of the word
def compute_parity_pre_computed(num: int) -> int:
    mask_size = 16
    mask = 0XFFFF
    return (PRECOMPUTED_PARITY[(num >> 3 * mask_size) & mask] ^
            PRECOMPUTED_PARITY[(num >> 2 * mask_size) & mask] ^
            PRECOMPUTED_PARITY[(num >> mask_size) & mask] ^
            PRECOMPUTED_PARITY[(num & mask)]
            )


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
# print(computer_parity_optimized(8))
