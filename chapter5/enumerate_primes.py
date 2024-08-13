import math


# Time Complexity is O(n * n^0.5) => O(n^1.5) and space complexity is O(1)
# Actual time complexity is O(n^1.5 / (ln(n)^2))
def countPrimesBruteForce(n: int) -> int:
    def is_prime(current_candidate: int) -> bool:
        for el in range(2, int(math.sqrt(current_candidate) + 1)):
            if current_candidate % el == 0:
                return False
        return True

    if n <= 2:
        return 0

    ct = 0
    for curr_n in range(2, n):
        if is_prime(curr_n):
            ct += 1
    return ct


# so overall time complexity is O(n/2 + n/3 + n/5 + n/7 + n/11 + ....) which is N * prime harmonic series
# sum of reciprocals of primes is donated by 1/p which sums up to ln(ln(x)) for p <= x
# So time complexity can be expressed as O(n * log(log(n))) and space complexity is O(P) where p is prime number
def countPrimesBruteForceSieve(n: int) -> int:
    ct = 0
    is_prime_candidate = [False, False] + [True] * (n - 1)
    for el in range(2, n):
        if is_prime_candidate[el]:
            ct += 1
            for multiple in range(el, n, el):
                is_prime_candidate[multiple] = False
    return ct
