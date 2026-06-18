class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = {}
        for x in nums:
            a[x] = a.get(x,0)+1
        sorted_a = dict(sorted(a.items(), key=lambda item: item[1], reverse=True))
        answer = []
        sorted_list = [x for x in sorted_a] # list(sorted_a.keys)
        for i in range(k):
            answer.append(sorted_list[i])
        return answer
            
        