import random


def get_random_bit():
    return random.getrandbits(1)


def generate_random_number_within_range(a: int, b: int) -> int:
    num_outcomes = 1 + b - a
    while True:
        result = 0
        ct = 0
        while 1 << ct < num_outcomes:
            result = (result << 1) | get_random_bit()
            ct += 1
        if result < num_outcomes:
            return a + result


print(generate_random_number_within_range(1, 6))
