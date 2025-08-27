class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        for i in range(len(s)):
            a =set()
            for j in range(i,len(s)):
                if s[j] in a:
                    i+=1
                    break
                maxLen = max(maxLen, j-i+1)
                a.add(s[j])
        return maxLen
                
        
        
        
        
        # letters ={}
        # left = 0
        # max_count = 0
        # for right in range(len(s)):
        #     letters[s[right]] = letters.get(s[right],0)+1
        #     while(letters[s[right]] >1):
        #         letters[s[left]]-=1
        #         if letters[s[left]]==0:
        #             del letters[s[left]]
        #         left+=1
        #     max_count=max(max_count, right-left+1)
        # return max_count
        