class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        a = s[0:k]
        count = 0
        for i in range(k):
            if a[i] in vowels:
                count+=1
        answer = count

        for i in range(k,len(s)):
            if s[i] in vowels:
                count+=1
            if s[i-k] in vowels:
                count-=1
            answer  = max(count, answer)
        return answer