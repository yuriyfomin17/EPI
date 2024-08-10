import math
from typing import List


def is_prime(el: int) -> bool:
    for division in range(2, int(math.sqrt(el)) + 1):
        if el % division == 0:
            return False
    return True


def enumerate_primes(N: int) -> List[int]:
    candidates = [True] * (N + 1)

    ans = [2]
    for el in range(2, N + 1):
        is_prime_num = is_prime(el)
        if is_prime_num and candidates[el]:
            for i in range(2, len(candidates)):
                if i % el == 0:
                    candidates[i] = False
            ans.append(el)

    return ans


print(enumerate_primes(18))
