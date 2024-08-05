def sum_bit(a_val: str, b_val: str, carry: bool):
    a_bool = a_val == "1"
    b_bool = b_val == "1"
    if a_bool and b_bool and carry:
        return "1", True
    if a_bool and b_bool:
        return "0", True
    if a_bool and carry:
        return "0", True
    if b_bool and carry:
        return "0", True
    if a_bool:
        return "1", False
    if b_bool:
        return "1", False
    if carry:
        return "1", False
    return "0", False


# time complexity is O(N)
def add_binary_strings(a: str, b: str) -> str:
    a_i = len(a) - 1
    b_i = len(b) - 1
    res = ""
    carry = False
    while a_i >= 0 and b_i >= 0:
        a_val = a[a_i]
        b_val = b[b_i]
        new_val, carry = sum_bit(a_val, b_val, carry)
        res = new_val + res
        a_i -= 1
        b_i -= 1
    while a_i >= 0:
        a_val = a[a_i]
        new_val, carry = sum_bit(a_val, "0", carry)
        res = new_val + res
        a_i -= 1

    while b_i >= 0:
        b_val = b[b_i]
        new_val, carry = sum_bit("0", b_val, carry)
        res = new_val + res
        b_i -= 1
    if carry:
        return "1" + res
    return res


print(add_binary_strings("11", "11"))
