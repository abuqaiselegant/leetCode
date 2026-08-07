class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def dfs(index, currentSum , path):
            if currentSum == target:
                ans.append(path.copy())
                return
            if currentSum > target or index == len(candidates):
                return
            path.append(candidates[index])
            dfs(index, currentSum + candidates[index], path)
            path.pop()

            dfs(index+1, currentSum, path)
        dfs(0, 0, [])
        return ans