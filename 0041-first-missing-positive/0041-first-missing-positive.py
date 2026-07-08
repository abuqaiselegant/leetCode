class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        a = set(nums)
        ans = 0
        
        for i in range(1, len(nums)+1):
            if i not in a:
                ans = i
                return ans
        if len(nums)==max(nums):
            return max(nums)+1
        return ans