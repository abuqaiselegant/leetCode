class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        h1,m1,s1 = startTime.split(":")
        h2,m2,s2 = endTime.split(":")
        diffH1 = int(h2)-int(h1)
        diffM1 = int(m2)-int(m1)
        diffS1 = int(s2)-int(s1)

        return diffH1*60*60+diffM1*60+diffS1