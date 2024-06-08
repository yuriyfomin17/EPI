# It takes n bits to represent num1/num2 there are O(N) iterations
# To find 2k num2 <= num1, it is computed by iterating through k. Each iteration
# has O(n) time complexity. Hence, total time complexity if O(n^2)
def calculate_quotient(num1: int, num2: int) -> int:
    if num1 < num2:
        return 0
    quotient_sum = 1
    temp = num2
    while num1 >= temp << 1:
        temp <<= 1
        quotient_sum <<= 1
    return quotient_sum + calculate_quotient(num1 - temp, num2)


# It takes n bits to represent num1/num2 there are O(N) iterations
# To find 2k num2 <= num1, it is computed by iterating through k. Each iteration
# has O(n) time complexity. Hence, total time complexity if O(n^2)
def calculate_quotient_iteratively(num1: int, num2: int) -> int:
    result = 0
    while num2 <= num1:
        ct = 0
        temp = num2
        while temp << 1 < num1:
            temp <<= 1
            ct += 1
        result += 1 << ct
        num1 -= temp
    return result

# It takes n bits to represent num1/num2 there are O(N) iterations
# To find 2k num2 <= num1, it is computed by iterating through k. Each iteration
# has O(n) time complexity. Hence, total time complexity if O(n^2)
def calculate_quotient_iteratively_optimized(num1: int, num2: int) -> int:
    power = 32
    result = 0
    while num1 > num2:
        ct = 0
        temp = num2 << power
        while temp > num1:
            temp >>= 1
            ct += 1
        result += 1 << (power - ct)
        power = power - ct
        num1 -= temp
    return result


# time complexity is O(N) where N is the size of the number in bit
def calculate_quotient_optimized(num1: int, num2: int, power: int) -> int:
    if num1 < num2:
        return 0
    ct = 0
    curr_num = num2 << power
    while curr_num > num1:
        curr_num >>= 1
        ct += 1
    quotient_power = power - ct
    return (1 << quotient_power) + calculate_quotient_optimized(num1 - curr_num, num2, quotient_power)


print(calculate_quotient_iteratively(11, 2))
print(calculate_quotient_iteratively_optimized(11, 2))
print(calculate_quotient(11, 2))
print(calculate_quotient_optimized(11, 2, 31))
