from typing import List


def remove_leading_zeros(arr):
    return arr[next((i for i, x in enumerate(arr) if x != 0), len(arr)):] or [0]

# Time complexity is O(mn)
def multiply_two_integers(num1: List[int], num2: List[int]) -> List[int]:
    sign = -1 if (num1[0] < 0) ^ (num2[0] < 0) else 1
    num1[0], num2[0] = abs(num1[0]), abs(num2[0])

    result = [0] * (len(num1) + len(num2))

    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            result[i + j + 1] += num1[i] * num2[j]
            result[i + j] += result[i + j + 1] // 10
            result[i + j + 1] %= 10
    result = remove_leading_zeros(result)
    result[0] *= sign
    return result


print(multiply_two_integers([-1, 2, 3], [9, 8, 7]))
