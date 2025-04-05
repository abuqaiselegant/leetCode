class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Check if lengths match
        if len(s) != len(t):
            return False
        
        # Map s chars to t chars
        s_to_t = {}
        # Track used t chars
        t_used = set()
        
        # Iterate over both strings together
        for s_char, t_char in zip(s, t):
            # If s_char is already mapped
            if s_char in s_to_t:
                # Mapping must match current t_char
                if s_to_t[s_char] != t_char:
                    return False

            else:
                # t_char must not be used by another s_char
                if t_char in t_used:
                    return False
                s_to_t[s_char] = t_char
                t_used.add(t_char)
        
        return True