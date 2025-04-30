class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount < 1:
            return 0
        dp = [math.inf for _ in range(amount + 1)]

        for coin in coins:
            if coin <= amount:
                dp[coin] = 1

        for amt in range(1, amount + 1):
            for coin in coins:
                if amt - coin >= 0:
                    dp[amt] = min(dp[amt], dp[amt - coin] + 1)

        return dp[amount] if dp[amount] < math.inf else -1
