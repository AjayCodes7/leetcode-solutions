class Solution {
    public int maxAscendingSum(int[] nums) {
        int sum = nums[0];
        int result = 0;
        for(int i = 1; i < nums.length; i++){
            if(nums[i-1] < nums[i]){
                sum += nums[i];
            }else {
                result = Math.max(result,sum);
                sum = nums[i];
            }
        }
        result = Math.max(result, sum);
        return result;
    }
}