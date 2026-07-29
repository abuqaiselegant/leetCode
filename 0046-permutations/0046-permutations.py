class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        path = []
        used = [False]* len(nums)
        def backtrack(used, path):
            if len(path) == len(nums):
                ans.append(path.copy())
                return
            for i in range(len(nums)):
                if not used[i] :
                    path.append(nums[i])
                    used[i] = True
                    backtrack(used, path)
                    path.pop()
                    used[i] = False
        backtrack(used, path)
        return ans