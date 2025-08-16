class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        ops = 0
        if nums == sorted(nums):
            return 0
        while nums !=sorted(nums):
            minsum = float('inf') 
            index =-1
            for i in range(len(nums)-1):
                pairsum = nums[i]+nums[i+1]
                if pairsum < minsum:
                    minsum = pairsum
                    index = i        
            nums.pop(index+1)
            ops+=1
            nums[index]=minsum
            
        return ops

            