class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return -1
        prefix_sum = [0]*(n+1)
        for i in range(n):
            prefix_sum[i+1]=prefix_sum[i]+nums[i]
        
        for i in range(n):
            leftSum = prefix_sum[i]
            rightSum = prefix_sum[n]-prefix_sum[i]-nums[i]

            if leftSum == rightSum :
                return i
        return -1