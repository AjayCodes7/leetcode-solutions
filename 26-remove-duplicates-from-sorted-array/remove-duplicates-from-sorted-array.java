class Solution {
    public int removeDuplicates(int[] nums) {
        int result = 1;
        int curr = 1;
        for(int i = 1 ; i < nums.length; i++){
            if(nums[i] != nums[i-1]){
                nums[curr] = nums[i];
                curr++;
                result++;
            }
        }
        return result;
    }
}