class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total_sum = sum(nums)
        k = total_sum-x
        if k<0:
            return -1
        if k == 0:
            return len(nums)

        l = 0
        maxLen = 0
        currentSum = 0
        for r in range(len(nums)):
            currentSum +=nums[r]
            while currentSum >k:
                currentSum-=nums[l]
                l+=1
            if currentSum == k:
                maxLen = max(maxLen, r-l+1)
        return len(nums)-maxLen if maxLen!=0 else -1
            