class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        i = 0
        j = len(s)-1 
        a = [x for x in s]
        while(i<j):
            if a[i] in vowels and a[j] in vowels: 
                a[i],a[j] = a[j],a[i]
                i+=1
                j-=1
            elif a[j] not in vowels:
                j-=1
            elif a[i] not in vowels:
                i+=1
        return "".join(a)

            