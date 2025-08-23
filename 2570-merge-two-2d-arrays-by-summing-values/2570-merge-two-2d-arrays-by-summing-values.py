class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        a ={}
        for i in nums1:
            a[i[0]]= i[1]
        for i in nums2:
            if i[0] in a:
                a[i[0]]+=i[1]
            else:
                a[i[0]]=i[1]
        return [[k,a[k]] for k in sorted(a)]