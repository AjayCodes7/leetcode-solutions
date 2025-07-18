class Solution {
    public int climbStairs(int n) {
        int[] fib = {1, 2};
        if(n==1 || n == 2){
            return fib[n-1];
        }
        else{
            int temp;
            for(int i = 3; i <= n; i++){
                temp = fib[1];
                fib[1] = fib[0] + fib[1];
                fib[0] = temp;
            }
        }
        return fib[1];
    }
}