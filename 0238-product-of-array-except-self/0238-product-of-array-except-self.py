class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        answer =[1]* len(nums)

        for i in range(len(nums)):
            answer[i] = prefix
            prefix *= nums[i]
            
        suffix =1
        print(answer)
        for i in range(len(nums)-1,-1,-1):
            answer[i]*=suffix
            suffix *= nums[i]
            
        return answer
            
