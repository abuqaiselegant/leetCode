class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        add = 0
        for a in nums:
            if a%2 == 0:
                add +=a
        print("1:",nums)
        print("add1:",add)
        for val, index in queries:

            if nums[index] %2==0:
                add-=nums[index]

            nums[index]+=val

            if nums[index] % 2 == 0:
                add += nums[index]

            ans.append(add)
        return ans
                    