class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # a ={}
        # for num in nums:
        #     a[num]=1+a.get(num,0)

        # arr=[]
        # for num, cnt in a.items():
        #     arr.append([cnt, num])
        # arr.sort()
        
        # i =0
        # res=[]
        # while i<k:
        #     res.append(arr.pop()[1])
        #     i+=1
        # return res
        count ={}
        for num in nums:
            count[num]=1+count.get(num,0)
        
        freq =[[] for i in range (len(nums)+1)]

        for n,c in count.items():
            freq[c].append(n)
        
        res=[]
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res
