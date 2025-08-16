class Solution:
    def maximum69Number (self, num: int) -> int:
        arr = [int(digit) for digit in str(num)]
        
        flag  = True

        for i in range(len(arr)):
            if arr[i]!=9:
                arr[i]=9
                flag = False
                break
        
        if flag == False:
            num=0
            for digit in arr:
                num = num * 10 + digit
        return num
            
            



        