class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int i = 0;
        int j = 0;
        int k = 0;
        int a[]= new int[m+n];
        while(i<m&&j<n){
            if(nums1[i]<nums2[j]){
                a[k]=nums1[i];
                k++;
                i++;
            }
            else{
                a[k]=nums2[j];
                k++;
                j++;
            }
        }
        while(i<m){
            a[k]=nums1[i];
            i++;
            k++;
        }
        while(j<n){
            a[k]=nums2[j];
            k++;
            j++;
        }
        for(int z =0;z<a.length;z++){
            nums1[z]=a[z];
        }

    }
}