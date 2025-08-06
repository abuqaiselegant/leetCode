class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        a = {}
        for x in nums:
            if x in a:
                a[x]+=1
            else:
                a[x] =1
        num=0
        
        for i in a:
            if a[i]%2==0:
                num+=a[i]/2
            
        return num==len(nums)/2
