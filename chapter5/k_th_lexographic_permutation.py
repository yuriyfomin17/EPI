import math
from typing import List


def next_kth_lexographical_permutation(sequence: List[int], k: int) -> List[int]:
    res = []
    N = len(sequence)
    for i in reversed(range(N)):
        idx_to_remove = k // math.factorial(i)
        k -= idx_to_remove * math.factorial(i)
        if len(sequence) == 0 or not 0 <= idx_to_remove < len(sequence):
            return []
        res.append(sequence.pop(idx_to_remove))
    return res


print(next_kth_lexographical_permutation([1, 2, 3, 4], 4))
