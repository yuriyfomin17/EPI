# time complexity is O(N) where N is the size of the word
def get_closest_integer_with_same_weight(num: int) -> int:
    for un_signed_bit in range(63):
        if (num >> un_signed_bit) & 1 != (num >> (un_signed_bit + 1)) & 1:
            num ^= (1 << un_signed_bit) | (1 << (un_signed_bit + 1))
            return num
    return num


# time complexity is O(N) where N is the size of the word
def get_closest_integer_with_same_weight_optimized(num: int) -> int:
    num1 = num & ~(num - 1)
    mask = num1 | (num1 >> 1)
    return num ^ mask


print(get_closest_integer_with_same_weight(7))
print(get_closest_integer_with_same_weight_optimized(7))
print()
