class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        arr=[]
        sum = 0
        for i in range(len(digits)):
            sum=sum*10+digits[i]
        sum=sum+1
        for i in str(sum):
            arr.append(int(i))
        return arr
            
        