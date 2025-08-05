class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        """
        :type fruits: List[int]
        :type baskets: List[int]
        :rtype: int
        """
        placed = 0
        for x in fruits:
            for i in range(len(baskets)):
                if x <=baskets[i]:
                    baskets.pop(i)
                    placed +=1
                    break
        return len(fruits)-placed
