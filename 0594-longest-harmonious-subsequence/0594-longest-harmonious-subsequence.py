class Solution:
    def findLHS(self, nums: List[int]) -> int:
        a ={}
        for i in nums:
            if i in a:
                a[i]+=1
            else:
                a[i]=1
        maxC = 0
        for i in a:
            if i+1 in a:
                maxC = max(maxC,a[i]+a[i+1])
        return maxC
        