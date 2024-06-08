def add(num1: int, num2: int) -> int:
    return num1 if num2 == 0 else add(num1 ^ num2, (num1 & num2) << 1)


# Time complexity of addition is O(N) where n is hte number of bits needed to represent the operand
# since we do addition N times when N is the size of the number. The total time complexity is O(n^2)
def compute_product(num1: int, num2: int) -> int:
    running_sum = 0
    while num1:
        bit1 = num1 & 1
        if bit1:
            running_sum = add(num2, running_sum)
        num1 >>= 1
        num2 <<= 1
    return running_sum


print(compute_product(13, 9))
