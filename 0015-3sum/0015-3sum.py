class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):

            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                        
        return res




        # for i in range(len(nums)-2):
        #     if i>0 and nums[i] == nums[i-1]:
        #         continue
            
        #     sum = -nums[i]
        #     left=i+1
        #     right = len(nums)-1

        #     while left < right:
        #         if nums[left]+nums[right]== sum:
        #             ans.append([nums[i], nums[left],nums[right]])
        #             while left <right and nums[left]==nums[left+1]:
        #                 left+=1
        #             while left <right and nums[right] == nums[right-1]:
        #                 right-=1
        #             left+=1
        #             right-=1

        #         elif nums[left]+nums[right]>sum:
        #             right -=1
        #         else :
        #             left+=1
        # return ans
