class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # for i in range(1,len(nums)+1):
        #     if i not in nums:
        #         return i
        # return 0
        n = len(nums)
        summation = (n*(n+1))//2
        numSum = sum(nums)
        return summation - numSum
