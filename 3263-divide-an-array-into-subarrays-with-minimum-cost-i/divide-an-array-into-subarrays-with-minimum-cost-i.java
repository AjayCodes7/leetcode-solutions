class Solution {
    public int minimumCost(int[] nums) {
        int temp = 151;
        int n = nums.length;
        for(int i = 1; i < n-1; i++){
            for(int j = i+1; j < n; j++){
                temp = Math.min(temp, nums[i]+nums[j]);
            }
        }
        return temp + nums[0];
    }
}