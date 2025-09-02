class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def gain(a,b):
            return ((a+1)/(b+1))-(a/b)
        heap = [(-gain(p, t), p, t) for p, t in classes]
        heapq.heapify(heap)
        
        for i in range(extraStudents):
            g, p, t = heapq.heappop(heap)
            p+=1
            t+=1
            heapq.heappush(heap,(-gain(p,t),p,t))
        
        total = 0
        while heap:
            _, p, t = heapq.heappop(heap)
            total += p/t
        
        return total/(len(classes))
        
      