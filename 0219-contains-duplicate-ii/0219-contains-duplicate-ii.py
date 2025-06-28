class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # a = {}
        # for i in range(len(nums)):
        #     if nums[i] in a and abs(i - a[nums[i]])<=k:
        #         return True
        #     a[nums[i]] = i 
        # return False

        l,r=0,len(nums)-1
        while l<r:
            if nums[l]==nums[r] and abs(l-r)<=k:
                return True
            l+=1
        l,r=0,len(nums)-1
        while l<r:
            if nums[l]==nums[r] and abs(l-r)<=k:
                return True
            r-=1
        return False