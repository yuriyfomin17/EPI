def add(num1: int, num2: int) -> int:
    return num1 if num2 == 0 else add(num1 ^ num2, (num1 & num2) << 1)


def multiply(num1: int, num2: int) -> int:
    result = 0

    while num1:
        if num1 & 1:
            result = add(result, num2)
        num2 <<= 1
        num1 >>= 1
    return result


# it takes O(p) iterations where p is the digit of power. To multiply num by result is O(n^2) complexity
# hence total complexity is O(p * n^2)
def custom_power(num: int, pow: int) -> int:
    result = 1
    while pow:
        result = multiply(num, result)
        pow -= 1
    return result


# at mostly iterations will be done till the most significant bit of power. Hence, total time complexity is
# O(N)
def power_optimized(num: int, power: int) -> float:
    result = 1.0
    if power < 0:
        num = 1.0 / num
        power = -power
    while power:
        if power & 1:
            result *= num
        power >>= 1
        num = num * num
    return result


print(custom_power(5, 4))
print(power_optimized(5, 4))
print(power_optimized(5, -4))
