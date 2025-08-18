class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        EPS = 1e-6
        n = len(cards)
        
        # memo: map subset mask -> set of possible values
        memo = {}

        def dp(mask: int) -> List[float]:
            if mask in memo:
                return memo[mask]
            
            values = []
            nums = [cards[i] for i in range(n) if (mask >> i) & 1]
            
            # base case: single number
            if len(nums) == 1:
                values = [float(nums[0])]
            else:
                # split mask into two non-empty disjoint subsets
                submask = (mask - 1) & mask
                while submask:
                    other = mask ^ submask
                    if other:  # both parts non-empty
                        for x in dp(submask):
                            for y in dp(other):
                                values.append(x + y)
                                values.append(x - y)
                                values.append(y - x)
                                values.append(x * y)
                                if abs(y) > EPS:
                                    values.append(x / y)
                                if abs(x) > EPS:
                                    values.append(y / x)
                    submask = (submask - 1) & mask

            memo[mask] = values
            return values

        full_mask = (1 << n) - 1
        for v in dp(full_mask):
            if abs(v - 24) < EPS:
                return True
        return False
