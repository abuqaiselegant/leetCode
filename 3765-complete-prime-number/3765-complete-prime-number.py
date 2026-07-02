class Solution:
    def isPrime(self,n):
        if n ==2:
            return True
        if n<2 :
            return False
        if n % 2 ==0:
            return False
        i= 3
        while i*i<=n:
            if n%i==0:
                return False
            i+=2
        return True

    def completePrime(self, num: int) -> bool:
        s = str(num)
        for i in range(1, len(s)+1):
            if not self.isPrime(int(s[:i])):
                return False
        for i in range(len(s)):
            if not self.isPrime(int(s[i:])):
                return False
        return True
