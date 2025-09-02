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
        if n<k:
            return []
        
        p_count = Counter(p)
        window_count = Counter(s[:k-1])
        answer = []

        for i in range(k-1, n):
            window_count[s[i]] += 1

            if window_count == p_count:
                answer.append(i-k+1)
            
            left_char = s[i-k+1]
            window_count[left_char] -= 1
            if window_count[left_char] == 0:
                del window_count[left_char]
        
        return answer
        