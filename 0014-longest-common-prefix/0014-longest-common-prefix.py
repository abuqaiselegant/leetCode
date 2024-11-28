class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Handle empty array
        if not strs:
            return ""
            
        # Get shortest string length
        min_len = min(len(s) for s in strs)
        
        # Check each character position
        for i in range(min_len):
            # Get character to compare
            char = strs[0][i]
            
            # Check this character in all strings
            for string in strs[1:]:
                if string[i] != char:
                    # Return prefix up to this position
                    return strs[0][:i]
        
        # If we get here, return the shortest string
        return strs[0][:min_len]