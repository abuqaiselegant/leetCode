class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        ans = [1]
        i = 2
        while n>1 and i<=n:
            if n%i==0:
                ans.append(i)
            i+=1
            # print(ans)
        return ans[k-1] if k<=len(ans) else -1
