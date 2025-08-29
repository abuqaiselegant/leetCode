class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        l = 0
        maxLen = 0
        maxCount = 0
        for r in range(len(s)):
            freq[s[r]]=freq.setdefault(s[r],0)+1
            maxCount = max(freq[s[r]],maxCount)
            while r-l+1-maxCount>k:
                freq[s[l]]-=1
                l+=1
            maxLen =max(maxLen,r-l+1)
        return maxLen










        
        # count={}
        # l=0
        # res=0
        # maxf=0

        # for r in range(len(s)):
        #     count[s[r]]=count.get(s[r],0)+1
        #     maxf=max(maxf,count[s[r]])

        #     while (r-l+1)-maxf >k:
        #         count[s[l]]-=1
        #         l+=1
        #     res = max(maxf,r-l+1)
        # return res
        