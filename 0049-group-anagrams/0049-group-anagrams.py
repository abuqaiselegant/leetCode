from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        anagram_map = defaultdict(list)  # key: sorted string, value: list of anagrams
        
        for word in strs:
            key = ''.join(sorted(word))  # Sorting gives us a consistent anagram signature
            anagram_map[key].append(word)
        
        return list(anagram_map.values())  # Convert to list of lists
