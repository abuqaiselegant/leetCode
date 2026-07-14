class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
       
        
        def fetchSecond(x):
            h,m,s = map(lambda x:int(x), x.split(":"))
            return h*60*60 + m*60 +s
        diff = fetchSecond(endTime) - fetchSecond(startTime) 
        return diff
