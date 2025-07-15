class Solution {
    public int maxProduct(int[] nums) {
        // Brute-Force Approach
        // if(nums.length == 1){
        //     return nums[0];
        // }
        // int[][] dp = new int[nums.length][nums.length];
        // for(int i = 0; i < nums.length; i++){
        //     Arrays.fill(dp[i], -Integer.MAX_VALUE);
        // }
        // int max_value = -Integer.MAX_VALUE;
        // for(int s = 0; s < nums.length; s++){
        //     dp[s][s] = nums[s];
        //     max_value = Math.max(max_value, nums[s]);
        // }
        // for(int i = 0; i < nums.length; i++){
        //     for(int j = i+1; j < nums.length; j++){
        //         dp[i][j] = dp[i][j-1]*nums[j];
        //         max_value = Math.max(max_value, dp[i][j]);
        //     }
        // }
        // return max_value;

        int best_prod = nums[0];
        int max_prod = nums[0];
        int min_prod = nums[0];

        for(int i = 1; i < nums.length; i++){
            int curr = nums[i];

            if(curr < 0){
                int temp = max_prod;
                max_prod = min_prod;
                min_prod = temp;
            }

            max_prod = Math.max(curr, max_prod*curr);
            min_prod = Math.min(curr, min_prod*curr);

            best_prod = Math.max(best_prod, max_prod);
        }
        return best_prod;
    }

}