class Solution:
    def largestOddNumber(self, num: str) -> str:
        
        # not run bcz of some conversion
        # temp = int(num)
        # while temp%2==0: 
        #     temp = temp//10 
        #     if temp ==0: 
        #         return "" 
        # return str(temp)


        # while num and int(num[-1])%2==0:
        #     num = num[:-1]
        # return num

        for i in range(len(num)-1,-1,-1):
            if int(num[i]) %2==1:
                return num[:i+1]
        return ""