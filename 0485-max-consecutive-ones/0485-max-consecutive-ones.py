class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        MaxCount =0
        count =0
        for i in nums:
            if i ==1:
                count+=1
                if count>MaxCount:
                    MaxCount = count
            else: count =0

        return MaxCount
