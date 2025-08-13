class Solution {
    public boolean isPowerOfThree(int n) {
        // int total = 1;
        // while (total<=n/3){
            
        //     if (total == n){
        //         return true;
        //     }
        //     total = total *3;
        // }
        // return total ==n;

        if (n<=0){
            return false;
        }        
        while (n%3==0){
            n/=3;
        }
        return n==1;
    }
}