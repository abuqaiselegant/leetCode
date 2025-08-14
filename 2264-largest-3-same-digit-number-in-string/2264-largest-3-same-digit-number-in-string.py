class Solution:
    def largestGoodInteger(self, num: str) -> str:
        
        count = 1
        best = ""
        for i in range(1,len(num)):
            if num[i]==num[i-1]:
                count+=1
            else:
                if count >= 3:
                    string = 3*num[i-1]
                    if string >best:
                        best = string
                count = 1
        if count >=3:
            triple = 3*num[-1]
            if triple >best:
                best = triple
        return best