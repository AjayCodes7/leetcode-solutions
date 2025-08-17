class Solution {
    public double new21Game(int n, int k, int maxPts) {
        if (k == 0 || n >= k - 1 + maxPts) return 1.0;

        double[] dp = new double[n+1];
        for(int i = k ; i <= n ; i++) dp[i] = 1;
        double probSum = n - k + 1;
        for(int i = k - 1 ; i >= 0 ; i--){
            dp[i] = (probSum)/maxPts;
            probSum += dp[i];
            if(i + maxPts <= n){
                probSum -= dp[i + maxPts];
            }
        }
        return dp[0];
    }
}