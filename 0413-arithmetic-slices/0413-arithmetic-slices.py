class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        total = 0
        streak = 0
        if len(nums)<3:
            return 0
        for i in range(2,len(nums)):
            if nums[i]-nums[i-1] == nums[i-1]-nums[i-2]:
                streak+=1
            else :
                streak=0
            total +=streak
        return total
