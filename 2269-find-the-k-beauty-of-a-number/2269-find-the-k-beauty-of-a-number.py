class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        a = str(num)
        count = 0
        for i in range(len(a)-k+1):
            sub_a = a[i:i+k]
            if int(sub_a) ==0:
                continue
            if num%int(sub_a)==0:
                count+=1
        return count
        