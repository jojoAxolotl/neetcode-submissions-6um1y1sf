# T: O(n*t) n: the number of coins t: the given amount
# S: O(t)

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] * (amount+1)
        # print("dp: ", dp)
        for i in range(1, amount+1):
            cur_min = float('inf')
            for coin in coins:
                if i - coin < 0: 
                    continue
                elif i == coin: 
                    cur_min = 1
                elif dp[i-coin] != -1:
                    cur_min = min(cur_min, dp[i-coin] + 1)
            dp[i] = cur_min if cur_min != float('inf') else -1
            # print("dp: ", dp)
        return dp[amount]