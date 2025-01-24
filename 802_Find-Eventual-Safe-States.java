class Solution {
    
    public boolean dfs(int num, HashMap map, int[][] graph){
        if(map.containsKey(num)){
            return (boolean)map.getOrDefault(num, false);
        }
        map.put(num, false);
        for(int nei : graph[num]){
            if(!dfs(nei,map, graph)){
                return (boolean)map.get(num);
            }
        }
        map.put(num,true);
        return (boolean)map.get(num);
    }

    public List<Integer> eventualSafeNodes(int[][] graph) {
        int len = graph.length;
        HashMap<Integer, Boolean> map = new HashMap<>();

        List<Integer> result = new ArrayList<>();

        for(int i = 0; i < len; i++){
            if(dfs(i, map, graph)){
                result.add(i);
            }
        }
        return result;
    }
}