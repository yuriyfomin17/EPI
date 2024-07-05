import math
import random

PRECOMPUTED_PARITY = []


def count_bits(num: int) -> int:
    ct = 0
    while num:
        num = num & (num - 1)
        ct += 1
    return ct


# print(count_bits(9))

# // O(N)
def compute_parity(num: int) -> int:
    parity = 0
    while num:
        if num & 1:
            parity ^= 1
        num >>= 1
    return parity


def compute_parity_optimized(num: int) -> int:
    num = num ^ (num >> 32)
    num = num ^ (num >> 16)
    num = num ^ (num >> 8)
    num = num ^ (num >> 4)
    num = num ^ (num >> 2)
    num = num ^ (num >> 1)
    return num & 1


def compute_parity_pre_computed(num: int) -> int:
    mask_size = 16
    mask = 0XFFFF
    return (PRECOMPUTED_PARITY[num & mask] ^
            PRECOMPUTED_PARITY[(num >> mask_size) & mask] ^
            PRECOMPUTED_PARITY[(num >> 2 * mask_size) & mask] ^
            PRECOMPUTED_PARITY[(num >> 3 * mask_size) & mask]
            )


def swap_bits(num: int, i: int, j: int) -> int:
    if (num >> i) & 1 != (num >> j) & 1:
        mask = 1 << i | 1 << j
        return num ^ mask
    return num


def reverse_bits(num: int) -> int:
    mask_size = 8
    mask = 0XFF
    num = num & mask
    for i in range(mask_size // 2):
        num = swap_bits(num, i, 7 - i)
    return num


# O(N) where N is the bit  size of the num
def find_closest_integer_with_same_weight(num: int) -> int:
    for bit_i in range(63):
        if (num >> bit_i) & 1 != (num >> (bit_i + 1)) & 1:
            mask = 1 << bit_i | 1 << (bit_i + 1)
            return num ^ mask
    return num


# O(1) where N is the bit  size of the num
def least_significant_bit_set(num: int) -> int:
    mask = num & (num - 1)
    return num ^ mask


def least_significant_bit_unset(num: int) -> int:
    return ~num & (num + 1)


def find_closest_integer_with_same_weight_optimized(num: int) -> int:
    lsb_set = least_significant_bit_set(num)
    lsb_unset = least_significant_bit_unset(num)
    if lsb_unset > lsb_set:
        num |= lsb_unset
        return num ^ (lsb_unset >> 1)
    else:
        num |= (lsb_set >> 1)
        return num ^ lsb_set


def add(num1: int, num2: int) -> int:
    return num2 if num1 == 0 else add((num1 & num2) << 1, num1 ^ num2)


def multiply(num1: int, num2: int) -> int:
    running_sum = 0
    while num1:
        if num1 & 1:
            running_sum = add(running_sum, num2)
        num2 <<= 1
        num1 >>= 1
    return running_sum


def compute_quotient_without_arithmetical_product(num1: int, num2: int) -> int:
    quotient = 0
    while num1 >= num2:
        ct = 0
        temp = num2
        while temp << 1 < num1:
            temp <<= 1
            ct += 1
        num1 = num1 - temp
        quotient += 1 << ct
    return quotient


def compute_quotient_optimized(num1: int, num2: int, power: int) -> int:
    if num1 < num2: return 0
    ct = 0
    curr_num = num2 << power
    while curr_num > num1:
        curr_num >>= 1
        ct += 1
    quotient_power = power - ct
    return (1 << quotient_power) + compute_quotient_optimized(num1 - curr_num, num2, quotient_power)


def compute_power(num: int, power: int) -> int:
    result = 1
    while power:
        if power & 1:
            result *= num
        num = num * num
        power >>= 1

    return result


def check_if_integer_is_palindrome(num: int) -> bool:
    mask_size = int(math.log10(num))
    for i in range(mask_size // 2):
        if num % 10 != num // 10 ** mask_size:
            return False
        num = num - (num // 10 ** mask_size) * 10 ** mask_size
        num = num // 10
        mask_size -= 1
    return True


def generate_random_number(a: int, b: int) -> bool:
    occurrences = b - a

    while True:
        res = 0
        ct = 0
        while (1 << ct) < occurrences:
            res = (res << 1) | random.getrandbits(1)
            ct += 1
        if res <= occurrences:
            return a + res
    return 0

def calc_num_ones(num):
    ct = 0
    while num:
        ct += 1
        num = num & (num - 1)
    return ct

def sorter_func(a):
    num_ones_a = calc_num_ones(a)
    return (-num_ones_a, a)

arr = [479 ,403, 399 ,184, 116 ,100, 13, 232, 268, 331]
new_arr = sorted(arr, key=sorter_func)
print(new_arr)
for i in range(1, len(new_arr)):
    print(new_arr[i - 1] ^ new_arr[i])
