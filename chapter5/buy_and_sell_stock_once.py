from typing import List


#  Time complexity is O(n^2)
def buy_and_sell_stock_once_brute_force(prices: List[int]) -> int:
    max_profit = 0
    for i in range(0, len(prices)):
        for j in range(i + 1, len(prices)):
            max_profit = max(max_profit, prices[j] - prices[i])
    return max_profit


# Time complexity is O(N) since we iterate over dp at most 2N times and columns are either True or False
# Space complexity is O(N) since we store two additional array
def buy_and_sell_stock_once_brute_force_dp(prices: List[int]) -> int:
    dp = [[None, None] for _ in range(len(prices))]

    def helper(helper_prices, idx, bought_stock):
        if bought_stock and idx == len(helper_prices) - 1:
            return helper_prices[idx]
        if not bought_stock and idx == len(helper_prices) - 1:
            return 0
        bought_stock_idx = int(bought_stock)
        if dp[idx][bought_stock_idx] is not None:
            return dp[idx][bought_stock_idx]
        skip = helper(helper_prices, idx + 1, bought_stock)
        if bought_stock:
            sell_stock = helper_prices[idx]
            ans = max(sell_stock, skip)
            dp[idx][bought_stock_idx] = ans
            return ans
        else:
            buy_stock = -helper_prices[idx] + helper(helper_prices, idx + 1, True)
            ans = max(buy_stock, skip)
            dp[idx][bought_stock_idx] = ans
            return ans

    return helper(prices, 0, False)


#  Time complexity is O(N) and space complexity is O(N)
def buy_and_sell_stock_once_space_iterative(prices: List[int]) -> int:
    dp = [[0, 0] for _ in range(len(prices))]

    dp[0][0] = 0
    dp[0][1] = -prices[0]
    for i in range(1, len(prices)):
        dp[i][1] = max(-prices[i], dp[i - 1][1])
        dp[i][0] = max(prices[i] + dp[i - 1][1], dp[i - 1][0])
    return max(dp[-1][0], dp[-1][1])


#  Time complexity os O(N) and space complexity is O(1)
def buy_and_sell_stock_once_space_optimized(prices: List[int]) -> int:
    sold_stock_prev = 0
    bought_stock_prev = -prices[0]
    for i in range(1, len(prices)):
        bought_stock = max(-prices[i], bought_stock_prev)
        sold_stock = max(prices[i] + bought_stock_prev, sold_stock_prev)

        sold_stock_prev = sold_stock
        bought_stock_prev = bought_stock
    return max(sold_stock_prev, bought_stock_prev)


def maxProfit(prices: List[int]) -> int:
    min_stock_so_far, max_profit = float('inf'), 0

    for i in range(0, len(prices)):
        day_profit = prices[i] - min_stock_so_far
        max_profit = max(max_profit, day_profit)
        min_stock_so_far = min(min_stock_so_far, prices[i])
    return max_profit

# print(buy_and_sell_stock_once_brute_force_dp([7, 1, 5, 3, 6, 4]))
