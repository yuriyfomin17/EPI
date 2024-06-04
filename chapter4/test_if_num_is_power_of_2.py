def is_num_power_of_two(num: int) -> bool:
    num &= (num - 1)
    return num == 0


print(is_num_power_of_two(8))
