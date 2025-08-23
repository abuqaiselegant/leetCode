class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        a = {0:1}
        prefix = 0
        for i in range(len(nums)):
            prefix+=nums[i]
            need = prefix - k
            if need in a:
                count+=a[need]
            a[prefix] =a.get(prefix, 0)+1
        return count

