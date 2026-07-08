class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # ans = []
        # a = set()
        # for i in nums:
        #     if i in a:
        #         ans.append(i)
        #     else:
        #         a.add(i)
        
        # for i in range(1,len(nums)+1):
        #     if i not in nums:
        #         ans.append(i)
                
        # return ans

        # seen = set()
        # duplicate = 0
        # for num in nums:
        #     if num in seen:
        #         duplicate = num
        #     seen.add(num)
        # for i in range(1, len(nums) + 1):
        #     if i not in seen:
        #         return [duplicate, i]

        n = len(nums)
        i = 0
        while i <n:
            index = nums[i]-1
            if 1<=nums[i]<=n and nums[index] != nums[i]:
                nums[index], nums[i] = nums[i], nums[index]
            else: 
                i+=1
        for i in range(n):
            if nums[i] != i+1:
                return [nums[i], i+1]
        return [nums[n],n+1]
