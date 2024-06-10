import math


def check_if_decimal_is_palindrome(num: int) -> bool:
    if num <= 0: return num == 0
    num_str = str(num)
    for i in range(len(num_str) // 2):
        if num_str[i] != num_str[-i]:
            return False
    return True


def check_if_decimal_palindrome_space_optimized(num: int) -> bool:
    if num <= 0:
        return num == 0
    num_digits = math.floor(math.log10(num)) + 1
    msd_mask = 10 ** (num_digits - 1)
    for i in range(num_digits // 2):
        if num // msd_mask != num % 10:
            return False
        num %= msd_mask
        num //= 10
        msd_mask /= 100
    return True


print(check_if_decimal_is_palindrome(-5))
print(check_if_decimal_palindrome_space_optimized(5565))
