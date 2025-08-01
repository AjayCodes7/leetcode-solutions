class Solution {
    public int minCostClimbingStairs(int[] cost) {
        int[] mincost = new int[cost.length+1];
        mincost[0] = cost[0];
        mincost[1] = cost[1];
        for(int i = 2; i < cost.length ; i++){
            mincost[i] = Math.min(mincost[i-1]+cost[i], mincost[i-2]+cost[i]);
        }
        return Math.min(mincost[cost.length-1], mincost[cost.length-2]);
    }
}