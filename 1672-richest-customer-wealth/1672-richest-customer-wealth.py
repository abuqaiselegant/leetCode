class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        rich = 0
        for x in accounts:
            rich = max(rich, sum(x))
        return rich