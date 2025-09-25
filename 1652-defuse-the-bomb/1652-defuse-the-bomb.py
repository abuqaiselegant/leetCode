class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k==0:
            return [0]*n
        code2 = code*2

        prefix =[0]*(2*n+1)
        for i in range(1,2*n+1):
            prefix[i]=prefix[i-1]+code2[i-1]

        result = [0]*n
        if k>0:
            for i in range(n):
                result[i]=prefix[i+k+1]-prefix[i+1]
        else:
            k = -k
            for i in range(n):
                result[i] = prefix[i+n]-prefix[i+n-k]
        return result

        # n = len(code)
        # res = [0] * n

        # for i in range(n):
        #     if k > 0:
        #         for j in range(i+1, i + 1 + k):
        #             res[i] += code[j % n]
        #     elif k < 0:
        #         for j in range(i - 1, i - 1 - abs(k), -1):
        #             res[i] += code[j % n]

        # return res