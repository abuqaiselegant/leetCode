class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        M = max(nums)
        sum = 0
        for i in range(k):
            sum +=M
            M=M+1
        return sum
