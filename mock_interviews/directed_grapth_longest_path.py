from typing import List


# Given directed graph of n nodes labeled from 0 to n - 1. Find the length
# of the longest path from each node
# 0->1<-2<-3
# [1, 0, 1, 2]


# Construct the graph (adj list)
# ans = dict
# for loop --> 0 to n
# visited --> set()
# dict[curr_node] = longest_path(curr_node, visited)


# longest_path(curr_node, visited)
# if curr_node is already visited return 0
# add curr_node to visited
# curr_max_distance = 0
#
# for adj_node in graph[curr_node]
# curr_max_distance = max(curr_max_distance, longest_path(adj_node, visited))
# return curr_max_distance

def construct_graph(current_nodes: List[int]) -> dict:
    dict_info = {}
    for node, connected_node in enumerate(current_nodes):
        if node not in dict_info:
            dict_info[node] = []
        dict_info[node].append(connected_node)
    return dict_info


def find_longest_path_for_node(curr_node, visited, graph):
    visited.add(curr_node)
    curr_max_dist = 0
    for adj_node in graph[curr_node]:
        if adj_node not in visited:
            curr_max_dist = max(curr_max_dist, 1 + find_longest_path_for_node(adj_node, visited, graph))
    return curr_max_dist


def find_length_of_longest_path_from_each_node(nums: List[int]) -> List[int]:
    graph = construct_graph(nums)
    res = [0] * len(nums)
    for node in graph.keys():
        res[node] = find_longest_path_for_node(node, set(), graph)
    return res

# 0 -> 1 <- 2 <- 3 -> 4 -> 5 -> 6
nums = [0, 0, 1, 2, 3, 4, 5]

print(find_length_of_longest_path_from_each_node(nums))
