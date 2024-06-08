# time complexity is O(N) where N is number of digits in num
def reverse_digits(num: int) -> int:
    result = 0
    negative = num < 0
    num = abs(num)
    while num:
        quotient = num // 10
        remainder = num - quotient * 10
        result *= 10
        result += remainder
        num = num // 10
    if negative: return -result
    return result


print(reverse_digits(625))
