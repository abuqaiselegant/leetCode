class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        first = 1  # ways to reach step 1
        second = 2  # ways to reach step 2
        
        for i in range(3, n+1):
            third = first + second  # current step = prev + prev-prev
            first = second          # shift first forward
            second = third          # shift second forward
            
        return second  # second holds ways to reach step n
