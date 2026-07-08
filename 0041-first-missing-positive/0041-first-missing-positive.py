class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # a = set(nums)
        # ans = 0
        
        # for i in range(1, len(nums)+1):
        #     if i not in a:
        #         ans = i
        #         return ans
        # if len(nums)==max(nums):
        #     return max(nums)+1
        # return ans

        n = len(nums)

        i = 0
        while i < n:
            correct_index = nums[i] - 1

            if 1 <= nums[i] <= n and nums[i] != nums[correct_index]:
                nums[i], nums[correct_index] = nums[correct_index], nums[i]
            else:
                i += 1
        # print(nums)
        for i in range(n):
            if nums[i] != i+1:
                return i+1
        return n+1

