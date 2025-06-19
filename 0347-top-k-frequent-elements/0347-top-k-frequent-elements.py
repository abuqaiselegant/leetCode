class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a ={}
        for num in nums:
            a[num]=1+a.get(num,0)

        arr=[]
        for num, cnt in a.items():
            arr.append([cnt, num])
        arr.sort()
        
        i =0
        res=[]
        while i<k:
            res.append(arr.pop()[1])
            i+=1
        return res