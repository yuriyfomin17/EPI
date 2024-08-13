from typing import List


# Given a directed graph of `n` nodes labeled from `0` to `n-1`. Find the length of longest path out of each node.

dp = {}
def max_node_distance(curr_node, visited, tree):
    max_distance = 0
    if curr_node in dp: return dp[curr_node]
    visited.add(curr_node)
    for next_node in tree[curr_node]:
        if next_node in visited:
            continue
        max_distance = max(max_distance, 1 + max_node_distance(next_node, visited, tree))
    dp[curr_node] = max_distance
    return max_distance

def create_graph(nums: List[int]) -> List[int]:
    tree = {}
    for idx, el in enumerate(nums):
        if idx not in tree:
            tree[idx] = []
        tree[idx].append(el)
    ans = [0] * len(nums)
    for key in tree.keys():
        ans[key] = max_node_distance(key, set(), tree)
    return ans

print(create_graph([0,0,1,2]))


