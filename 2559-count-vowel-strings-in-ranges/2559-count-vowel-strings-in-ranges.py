class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = ['a','e','i','o','u']
        prefix = [0]
        answer = []
        for i in words:
            if i[0] in vowels and i[-1] in vowels:
                prefix.append(prefix[-1]+1)
            else: prefix.append(prefix[-1])
        print(prefix)
        for l,r in queries:
            answer.append(prefix[r+1]-prefix[l])
        return answer
