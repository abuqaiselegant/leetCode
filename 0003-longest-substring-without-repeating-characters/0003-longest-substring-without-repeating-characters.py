class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l =0
        r=0
        a = set()
        maxLen = 0
        while r <len(s):
            while s[r] in a:
                a.remove(s[l])
                l+=1
            a.add(s[r])
            maxLen = max(maxLen, r-l+1)
            r+=1

        return maxLen









        
        a = set()
        l =0
        r=0
        maxLen = 0
        while r<len(s):
            while s[r] in a:
                a.remove(s[l])
                l+=1
            a.add(s[r])
            maxLen=max(maxLen, r-l+1)
            r+=1
        return maxLen

      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
        # l= 0 
        # a=set()
        # maxLen=0
        # for r in range(len(s)):
        #     while s[r] in a:
        #         a.remove(s[l])
        #         l+=1
        #     a.add(s[r])
        #     maxLen = max(maxLen,r-l+1)
        # return maxLen

        
        
        
        
        
        
        # maxLen = 0
        # for i in range(len(s)):
        #     a =set()
        #     for j in range(i,len(s)):
        #         if s[j] in a:
        #             i+=1
        #             break
        #         maxLen = max(maxLen, j-i+1)
        #         a.add(s[j])
        # return maxLen
                
        
        
        
        
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
        