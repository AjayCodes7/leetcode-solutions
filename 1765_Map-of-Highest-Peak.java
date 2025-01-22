class Solution {
    public int[][] highestPeak(int[][] isWater) {
        Deque<int[]> deque = new ArrayDeque<>();
        Set<String> visited = new HashSet<>();
        int[][] result = new int[isWater.length][isWater[0].length];

        for (int i = 0; i < isWater.length; i++) {
            for (int j = 0; j < isWater[i].length; j++) {
                result[i][j] = -1;
            }
        }

        for(int r = 0; r < isWater.length; r++){
            for(int c = 0; c < isWater[r].length; c++){
                
                if(isWater[r][c] == 1){
                    deque.addLast(new int[] {r,c});
                    visited.add(r + "," + c);
                    result[r][c] = 0;
                }
                
            }
        }


        while(deque.size() > 0){
            int[] item = deque.removeFirst();
            int r = item[0];
            int c = item[1];
            int height = result[r][c];
            int[][] neighbors = new int[][]{{r+1,c},{r,c+1},{r-1,c},{r,c-1}};
            for(int[] neighbor: neighbors){
                int nr = neighbor[0];
                int nc = neighbor[1];

                if(nr < 0 || nc < 0 || nr == isWater.length || nc == isWater[nr].length || visited.contains(nr + "," + nc)){
                    continue;
                }

                deque.addLast(new int[] {nr,nc});
                visited.add(nr + "," + nc);
                result[nr][nc] = height + 1;
            }
        }
        return result;
    }
}
