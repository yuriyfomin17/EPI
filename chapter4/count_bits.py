# time complexity O(n) where n is the size of num
def count_bits(num: int) -> int:
    num_bits = 0
    while num:
        num_bits += num & 1
        num >>= 1
    return num_bits


def count_bits_optimized(num: int) -> int:
    num_bits = 0
    while num:
        num &= (num - 1)
        num_bits += 1
    return num_bits


print(count_bits(5))
