class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        result = set()
        for i in range(len(s)-9):
            a = s[i:i+10]
            if a in seen:
                result.add(a)
            seen.add(a)
        return list(result)
