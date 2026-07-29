class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answers = []
        def backtrack(index, path):
            if index == len(nums):
                answers.append(path.copy())
                return
            
            path.append(nums[index])
            backtrack(index+1, path)
            path.pop()

            backtrack(index+1,path)
        backtrack(0,[])
        return answers
        



            
