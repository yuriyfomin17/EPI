def count_bits(num: int) -> int:
    num_bits = 0
    while num:
        num_bits += num & 1
        num >>= 1
    return num_bits

print(count_bits(5))
