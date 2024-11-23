// class Solution {
//     public void rotate(int[] nums, int k) {
//         int d = nums.length-k;
//         for(int i =0;i<d;i++){
//             rotateOne(nums);
//         }
        

//     }
//     public void rotateOne(int[] nums){
//         int temp = nums[0];
//         for(int i  = 1;i<nums.length;i++){
//             nums[i-1]=nums[i];
//         }
//         nums[nums.length-1]=temp;
//     }
// }

class Solution {
    public void rotate(int[] nums, int k) {
        int n = nums.length;
        k = k % n; // Handle the case when k is larger than the array size
        
        // Reverse the entire array
        reverse(nums, 0, n - 1);
        
        // Reverse the first k elements
        reverse(nums, 0, k - 1);
        
        // Reverse the remaining elements
        reverse(nums, k, n - 1);
    }

    private void reverse(int[] nums, int start, int end) {
        while (start < end) {
            int temp = nums[start];
            nums[start] = nums[end];
            nums[end] = temp;
            start++;
            end--;
        }
    }
}
