class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if len(nums)==1:
            return [nums[0]]
        x, y , count1, count2 = None, None, 0,0
        for num in nums:
            if x==num:
                count1+=1
            elif y ==num:
                count2+=1
            elif count1 == 0:
                x = num
                count1 =1
            elif count2 ==0:
                y = num
                count2 =1
            else:
                count1-=1
                count2-=1
        a = []
        for num in nums:
            count1=1
            count2=1
            if num ==x:
                count1+=1
            elif num ==y:
                count2+=1
        if count1 >len(nums)/3:
            a.append(x)
        if count2>len(nums)/3:
            a.append(y)
        return a
