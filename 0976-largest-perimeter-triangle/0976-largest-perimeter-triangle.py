class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        a = sorted(nums,reverse = True)
        for i in range(len(a)-2):
            if a[i]<a[i+1]+a[i+2]:
                return a[i]+a[i+1]+a[i+2]
        return 0
