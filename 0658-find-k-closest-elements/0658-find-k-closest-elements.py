class Solution:
    def binary_search_left(self, arr, x):
        left, right = 0, len(arr)   # search range [0, n)
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < x:
                left = mid + 1
            else:
                right = mid
        return left

    def findClosestElements(self, arr, k, x):
        n = len(arr)
        
        # 1. Find insertion point
        pos = self.binary_search_left(arr, x)
        
        # 2. Initialize pointers
        if pos < n and arr[pos] == x:
            left = right = pos
        else:
            left, right = pos - 1, pos
        
        # 3. Expand outward until we have k elements
        while (right - left - 1) < k:
            if left < 0:
                right += 1
            elif right >= n:
                left -= 1
            else:
                if abs(arr[left] - x) <= abs(arr[right] - x):
                    left -= 1
                else:
                    right += 1
        
        # 4. Return the window
        return arr[left+1:right]
