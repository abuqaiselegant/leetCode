from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        # answer = []
        # for r in range(len(s)-len(p)+1):
        #     a = s[r:r+len(p)]
        #     if sorted(a)==sorted(p):
        #         answer.append(r)
        # return answer

        k = len(p)
        n = len(s)
        answer = []
        window = Counter(s[:k-1])
        p_count = Counter(p)
        
        for i in range(k-1, n):
            window[s[i]] += 1
            if window == p_count:
                answer.append(i+1-k)
            leftChar = i+1-k
            window[s[leftChar]]-=1
            if window[s[leftChar]]==0:
                del window[s[leftChar]]
        return answer