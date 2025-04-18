class Solution {
    public int fib(int n) {
        int[] dp = {0,1};
        int temp;
        for(int i = 0; i < n; i++){
            temp = dp[0] + dp[1];
            dp[0] = dp[1];
            dp[1] = temp;
        }
        return dp[0];
    }
}