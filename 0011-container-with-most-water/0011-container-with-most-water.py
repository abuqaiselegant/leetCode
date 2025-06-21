class Solution:
    def maxArea(self, height: List[int]) -> int:
        # maxArea=0
        # for i in range(0,len(height)-1):
        #     for j in range(i+1,len(height)):
        #         y = min(height[j],height[i])
        #         x = j-i
        #         maxArea=max(x*y,maxArea)
        # return maxArea
        
        maxArea = 0
        l , r = 0, len(height)-1
        while l<r:
            area = min(height[l],height[r]) * (r-l)
            maxArea= max(area,maxArea)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return maxArea
            
