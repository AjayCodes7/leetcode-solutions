class Solution {
    public int removeDuplicates(int[] nums) {
        int curr = 0;
        for(int i = 1 ; i < nums.length; i++){
            if(nums[i] != nums[curr]){
                nums[curr+1] = nums[i];
                curr++;
            }
        }
        return curr+1;
    }
}