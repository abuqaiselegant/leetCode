class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        l , r = 0, len(s)-1
        sList = list(s)
        while l<=r:
            if sList[l].isalpha() and sList[r].isalpha():
                # temp = sList[l]
                # sList[l]=sList[r]
                # sList[r] = temp
                sList[l],sList[r] = sList[r],sList[l]
                l+=1
                r-=1
            elif sList[l].isalpha()==False:
                l+=1
            else:
                r-=1
        return "".join(sList)
        