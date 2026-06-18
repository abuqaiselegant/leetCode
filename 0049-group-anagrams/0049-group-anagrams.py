class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = {}
        for i in range(len(strs)):
            key = ''.join(sorted(strs[i]))
            if key not in a:
                a[key] = []
            a[key].append(strs[i])
        return [a[x] for x in a]

