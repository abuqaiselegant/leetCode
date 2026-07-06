class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans = []
        a = set()
        for i in nums:
            if i in a:
                ans.append(i)
            else:
                a.add(i)
        
        for i in range(1,len(nums)+1):
            if i not in nums:
                ans.append(i)
                
        return ans