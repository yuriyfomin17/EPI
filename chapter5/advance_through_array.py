from typing import List
import queue

pre_computed = {}


def is_possible_to_win_optimized(nums: List[int], curr_index) -> bool:
    if curr_index >= len(nums) - 1:
        return True
    if nums[curr_index] == 0:
        return False
    if curr_index in pre_computed:
        return pre_computed[curr_index]
    for next_step in range(curr_index + 1, curr_index + nums[curr_index] + 1):
        if is_possible_to_win_optimized(nums, next_step):
            pre_computed[curr_index] = True
            return True
    pre_computed[curr_index] = False
    return False


def is_it_possible_to_win(nums: List[int]) -> bool:
    if len(nums) == 0 or nums[0] == 0:
        return False
    curr_queue = queue.Queue()
    curr_queue.put((nums[0], 0))
    while not curr_queue.empty():
        num_steps, curr_idx = curr_queue.get()
        if curr_idx + nums[curr_idx] >= len(nums) - 1:
            return True
        if num_steps == 0: continue
        for next_step in range(curr_idx + 1, curr_idx + num_steps + 1):
            curr_queue.put((nums[next_step], next_step))
    return False


#  time complexity is O(N) where N is number of elements
def is_possible_to_reach_book(nums: List[int]) -> bool:
    i = 0
    furthest_can_reach, last_index = 0, len(nums) - 1
    while i < len(nums) and furthest_can_reach < last_index:
        furthest_can_reach = max(furthest_can_reach, nums[i] + i)
        i += 1
    return furthest_can_reach >= last_index


arr = [3, 2, 0, 0, 2, 0, 1]
print(is_possible_to_win_optimized(arr, 0))
