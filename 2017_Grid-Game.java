class Solution {
    public long gridGame(int[][] grid) {
        long fSum = 0;
        for(int num: grid[0]){
            fSum += num;
        }
        long sSum = 0;
        long minSum = Long.MAX_VALUE;
        for(int i = 0; i < grid[1].length; i++){
            fSum -= grid[0][i];
            minSum = Math.min(
                minSum, 
                Math.max(fSum, sSum)
            );
            sSum += grid[1][i];
        }
        return minSum;
    }
}