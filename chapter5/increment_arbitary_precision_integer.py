from typing import List


# Time complexity is O(N)
def plusOne(digits: List[int]) -> List[int]:
    for idx in reversed(range(len(digits))):
        if digits[idx] + 1 != 10:
            digits[idx] += 1
            return digits
        digits[idx] = 0
        if idx == 0:
            digits[0] = 1
            digits.append(0)
            return digits
    return digits


print(plusOne([9, 9, 9]))
