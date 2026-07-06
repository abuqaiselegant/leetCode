class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        a  = set() 
        answ = []
        for i in nums:
            if i not in a:
                a.add(i)
            elif i in a:
                answ.append(i)
        return answ
            