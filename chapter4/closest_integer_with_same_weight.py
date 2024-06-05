# time complexity is O(N) where N is the size of the word
def get_closest_integer_with_same_weight(num: int) -> int:
    for un_signed_bit in range(63):
        if (num >> un_signed_bit) & 1 != (num >> (un_signed_bit + 1)) & 1:
            num ^= (1 << un_signed_bit) | (1 << (un_signed_bit + 1))
            return num
    raise ValueError('all bits are either 0s or 1s')


def lowest_bit_set(num: int) -> int:
    return num & ~(num - 1)


def lowest_bit_unset(num: int) -> int:
    return ~num & (num + 1)


# time complexity is O(1)
def closest_integer_with_same_weight_optimized(num: int) -> int:
    lbs = lowest_bit_set(num)
    lbu = lowest_bit_unset(num)

    if lbu > lbs:
        num |= lbu
        return num ^ (lbu >> 1)
    else:
        num |= (lbs >> 1)
        return num ^ lbs


for n in range(1, 30):
    print(get_closest_integer_with_same_weight(n))
    print(closest_integer_with_same_weight_optimized(n))
