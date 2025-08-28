class Solution:


    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        prefix = {0: 0}   # sum -> number of operations
        s = 0

        # prefix sums
        for i in range(n):
            s += nums[i]
            if s > x: 
                break
            prefix[s] = i + 1

        ans = prefix.get(x, float('inf'))  # ✅ prefix-only case

        # suffix sums
        s = 0
        for i in range(n-1, -1, -1):
            s += nums[i]
            if s > x: 
                break
            if (x - s) in prefix and prefix[x - s] + (n - i) <= n:
                ans = min(ans, prefix[x - s] + (n - i))

        return ans if ans != float('inf') else -1





        # total_sum = sum(nums)
        # k = total_sum-x
        # if k<0:
        #     return -1
        # if k == 0:
        #     return len(nums)

        # l = 0
        # maxLen = 0
        # currentSum = 0
        # for r in range(len(nums)):
        #     currentSum +=nums[r]
        #     while currentSum >k:
        #         currentSum-=nums[l]
        #         l+=1
        #     if currentSum == k:
        #         maxLen = max(maxLen, r-l+1)
        # return len(nums)-maxLen if maxLen!=0 else -1
            