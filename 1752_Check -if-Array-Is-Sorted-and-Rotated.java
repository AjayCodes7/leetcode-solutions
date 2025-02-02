class Solution {
    public boolean check(int[] nums) {
        int change = 0;
        for(int i = 0; i < nums.length-1; i++){
            if(nums[i] > nums[i+1]) change++;
        }
        if(nums[nums.length-1]>nums[0]) change++;
        return change <= 1;
    }
}