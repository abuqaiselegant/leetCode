class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters ={}
        left = 0
        max_count = 0
        for right in range(len(s)):
            letters[s[right]] = letters.get(s[right],0)+1
            while(letters[s[right]] >1):
                letters[s[left]]-=1
                if letters[s[left]]==0:
                    del letters[s[left]]
                left+=1
            max_count=max(max_count, right-left+1)
        return max_count
        