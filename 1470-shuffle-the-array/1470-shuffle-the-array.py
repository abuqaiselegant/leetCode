class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        first = 0
        second = n
        answer = []
        while first <n and second < len(nums):
            answer.append(nums[first])
            answer.append(nums[second])
            first+=1
            second+=1
        return answer