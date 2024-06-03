def compute_parity(num: int) -> int:
    parity = 0
    while num:
        parity ^= (num & 1)
        num >>= 1
    return parity


# Time complexity O(n)

print(compute_parity(5))
print(compute_parity(8))
print(compute_parity(9))
