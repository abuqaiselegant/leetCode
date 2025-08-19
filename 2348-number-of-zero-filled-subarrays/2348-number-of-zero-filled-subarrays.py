class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        subarray = 0
    
        count =0
        for i in range(len(nums)):

            if nums[i]==0:
                count +=1
            else:
                subarray += (count*(count+1))//2
                count = 0
        subarray +=(count*(count+1))//2
        return subarray


        