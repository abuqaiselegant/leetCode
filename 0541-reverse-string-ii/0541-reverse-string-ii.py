class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        i=0
        a = [x for x in s]
        while i<len(a):
            a[i:i+k]=reversed(a[i:i+k])
            i+=2*k
            # a[i:k] =a[k:i-1:-1]

            # i=2*k
            # k=2*k+2

            
        return ''.join(a)
