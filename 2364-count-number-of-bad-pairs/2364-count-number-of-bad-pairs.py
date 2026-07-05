class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        total = n *(n-1)//2
        seen = {}
        good = 0

        for i, x in enumerate(nums):
            key = x-i
            if key in seen:
                good+=seen[key]
                seen[key]+=1
            else:
                seen[key]=1
        return total-good