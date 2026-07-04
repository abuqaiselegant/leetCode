class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        a  = nums[:k]
        pre = sum(a)
        average = sum(a)/k
        ans = average
        for i in range(len(nums)-k):
            pre = pre + nums[i+k]-nums[i]
            average = pre/k
            ans = max(ans, average)
        return ans