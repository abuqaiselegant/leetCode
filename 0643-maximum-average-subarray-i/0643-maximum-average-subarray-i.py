class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums)<k:
            return -1
        sum_window = sum(nums[:k])
        max_sum = sum_window
        for i in range(k,len(nums)):
            sum_window= sum_window+nums[i]-nums[i-k]
            max_sum = max(sum_window,max_sum)
        return max_sum/k

