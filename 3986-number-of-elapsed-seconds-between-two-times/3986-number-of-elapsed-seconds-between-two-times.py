class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
       
        diff = self.fetchSecond(endTime) - self.fetchSecond(startTime) 
        return diff

    def fetchSecond(self,x):
        h,m,s = map(lambda x:int(x), x.split(":"))
        return h*60*60 + m*60 +s
    
