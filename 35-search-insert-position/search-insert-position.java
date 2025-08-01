class Solution {
    public int searchInsert(int[] nums, int target) {
        int i = -1;
        while(++i < nums.length && nums[i] <= target){
            if(nums[i]==target) return i;
        }
        return i;
    }
}