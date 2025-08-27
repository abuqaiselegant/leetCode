class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        l = 0
        count = 0
        cost = 0
        for r in range(len(s)):
            asc = abs(ord(s[r]) - ord(t[r]))
            cost += asc
            while cost > maxCost:
                asc = abs(ord(s[l])-ord(t[l]))
                cost -= asc
                l += 1
            count = max(count, r-l+1)
        return count



        # count = 0
        # left = 0 
        # cost = 0
        # for i in range(len(s)):
        #     asc = abs(ord(s[i])-ord(t[i]))
        #     cost+=asc
        #     while cost > maxCost:
        #         cost -=abs(ord(s[left])-ord(t[left]))
        #         left+=1
        #     count  = max(count, i-left+1)
        # return count
        