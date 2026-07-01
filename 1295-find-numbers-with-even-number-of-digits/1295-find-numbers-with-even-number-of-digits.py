class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        for i in nums:
            temp = i 
            count = 0
            while temp>0:
                count+=1
                temp = temp//10
            if count%2 ==0:
                ans+=1
        return ans