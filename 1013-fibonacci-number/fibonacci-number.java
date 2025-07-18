class Solution {
    public int fib(int n) {
        int[] fib = {0, 1};
        if(n==0 || n == 1){
            return fib[n];
        }
        else{
            int temp;
            for(int i = 2; i <= n; i++){
                temp = fib[1];
                fib[1] = fib[0] + fib[1];
                fib[0] = temp;
            }
        }
        return fib[1];
    }
}