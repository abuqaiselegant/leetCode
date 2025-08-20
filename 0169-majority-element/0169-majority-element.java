class Solution {
    public int majorityElement(int[] nums) {
        int count =1,res =0;
        if(nums.length==1){
            return nums[0];
        }
        for(int i =0;i<nums.length;i++){
            if(nums[i]==nums[res]){
                count++;
            }
            else{
                count--;
            }
            if(count==0){
                res = i;
                count =1;
            }
        }
        count =0;
        for(int i =0;i<nums.length;i++){
            if(nums[res]==nums[i]){
                count++;
            }
        }
        if(count<=nums.length/2){
            res =-1;
        }
        return nums[res];

    }
}