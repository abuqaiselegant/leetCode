class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        # Trivial cases
        if k == 0 or n >= k - 1 + maxPts:
            return 1.0

        dp = [0.0] * (n + 1)
        dp[0] = 1.0
        window_sum = 0.0  # sum of dp[j] over j in [i-maxPts, i-1] that are < k
        ans = 0.0

        for i in range(1, n + 1):
            # include dp[i-1] in the window if it can still draw (i-1 < k)
            if i - 1 < k:
                window_sum += dp[i - 1]
            # exclude dp[i-1-maxPts] if it was in the window and drawable
            if i - 1 - maxPts >= 0 and (i - 1 - maxPts) < k:
                window_sum -= dp[i - 1 - maxPts]

            dp[i] = window_sum / maxPts

        # Sum probabilities of final totals k..n
        return sum(dp[k:n + 1])
