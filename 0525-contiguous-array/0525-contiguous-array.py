class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        first_seen ={0:-1}
        floor = 0
        best = 0
        for i,n in enumerate(nums):
            floor +=1 if n== 1 else -1
            if floor in first_seen:
                best = max(best,i-first_seen[floor])
            else:
                first_seen[floor] = i
        return best