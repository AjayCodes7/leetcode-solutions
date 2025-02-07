class Solution {
    public int[] queryResults(int limit, int[][] queries) {
        int[] result = new int[queries.length];
        HashMap<Integer, HashSet<Integer>> colors = new HashMap<>();
        HashMap<Integer, Integer> balls = new HashMap<>();
        int a, b;
        for(int i = 0; i < queries.length; i++){
            a = queries[i][0];
            b = queries[i][1];
            if(balls.containsKey(a)){
                int oldVal = balls.get(a);
                if(colors.get(oldVal).size() == 1){
                    colors.remove(balls.get(a));
                } else{
                    colors.get(balls.get(a)).remove(a);
                }
            } 
            balls.put(a,b);
            colors.putIfAbsent(b, new HashSet<>());
            colors.get(b).add(a);
            result[i] = colors.size();
        }
        return result;
    }
}
