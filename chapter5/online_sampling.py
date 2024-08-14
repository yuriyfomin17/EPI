import random
from typing import List


def online_sampling(nums: List[int], k: int):
    for i in range(len(nums)):
        idx = random.randint(i, len(nums) - 1)
        nums[idx], nums[i] = nums[i], nums[idx]


