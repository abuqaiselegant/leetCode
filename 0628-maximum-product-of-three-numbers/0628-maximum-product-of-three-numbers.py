class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        ans1 = 1
        ans2 = 1
        n = len(nums)-1
        for i in range(3):
            ans1*=nums[n-i]
        ans2 = nums[0]*nums[1]*nums[-1]
        
        return max(ans1,ans2)