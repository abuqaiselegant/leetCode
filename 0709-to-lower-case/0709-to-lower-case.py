class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()
        """
        a =[x for x in s]
        for i in range(len(a)):
            if 64<ord(a[i])<91:
                a[i] = chr(ord(a[i])+32)
        a ="".join(a)
        return a"""


        