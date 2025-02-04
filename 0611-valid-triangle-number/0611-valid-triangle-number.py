class Solution:
    def triangleNumber(self, nums: List[int]) -> int:

        nums.sort()  # Step 1: Sort the array
        count = 0

        for k in range(len(nums) - 1, 1, -1):  # Fix nums[k] as the largest side
            left, right = 0, k - 1  # Two pointers

            while left < right:
                if nums[left] + nums[right] > nums[k]:  # Valid triangle condition
                    count += (right - left)  # All pairs (left, left+1, ..., right) are valid
                    right -= 1  # Move right pointer to check for other valid pairs
                else:
                    left += 1  # Increase left to get a larger sum

        return count