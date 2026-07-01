class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0
        for x in nums:
            i = 2
            div = [1,x]
            while i*i<=x:
                if x %i == 0:
                    div.append(i)
                    if i!=x//i:
                        div.append(x//i)
                
                if len(div)>4:
                    break
                i+=1
            if len(div)==4:
                ans += sum(div)
        return ans
            
            

