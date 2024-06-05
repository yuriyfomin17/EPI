def propagate_right_most_bit(num: int) -> str:
    return num | (num - 1)

# expected 01011111
print(propagate_right_most_bit(80))
# expected 0b10111111
print(propagate_right_most_bit(160))
