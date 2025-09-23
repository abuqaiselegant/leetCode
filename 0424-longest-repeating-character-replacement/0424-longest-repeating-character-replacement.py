class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        l = 0
        r = 0
        maxCount = 0
        maxLen =0
        while r <len(s):
            freq[s[r]]=freq.setdefault(s[r],0)+1
            maxCount = max(maxCount, freq[s[r]])
            while (r-l+1 - maxCount) > k:
                freq[s[l]]-=1
                l+=1
            
            maxLen = max(maxLen, r-l+1)
            r+=1
        return maxLen

        
        # freq = {}
        # l = 0
        # maxLen = 0
        # maxCount = 0
        # for r in range(len(s)):
        #     freq[s[r]]=freq.setdefault(s[r],0)+1
        #     maxCount = max(freq[s[r]],maxCount)
        #     while r-l+1-maxCount>k:
        #         freq[s[l]]-=1
        #         l+=1
        #     maxLen =max(maxLen,r-l+1)
        # return maxLen