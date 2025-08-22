class Solution {
    public int minimumArea(int[][] grid) {
        int[] topLeft = new int[2];
        topLeft[0] = Integer.MAX_VALUE;
        topLeft[1] = Integer.MAX_VALUE;
        int[] bottomRight = new int[2];
        bottomRight[0] = Integer.MIN_VALUE;
        bottomRight[1] = Integer.MIN_VALUE;
        for(int i = 0;i<grid.length;i++){
            for(int j = 0; j < grid[0].length; j++){
                if (grid[i][j] == 1){
                    topLeft[0]= Math.min(topLeft[0], i);
                    topLeft[1]= Math.min(topLeft[1], j);
                    bottomRight[0]= Math.max(bottomRight[0], i);
                    bottomRight[1]= Math.max(bottomRight[1], j);
                }
            }
        }
        return (bottomRight[0] - topLeft[0] + 1)*(bottomRight[1] - topLeft[1] + 1);
    }
}