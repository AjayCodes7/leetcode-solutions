class Solution {
    public int numRabbits(int[] answers) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for(int ans : answers) map.put(ans,map.getOrDefault(ans, 0)+1);
        int result = 0;
        for(int key : map.keySet()){
            if (key == 0) result += map.get(key);
            else if (key > map.get(key)) result += key + 1;
            else{
                result += (map.get(key)/(key+1))*(key+1);
                if (map.get(key)%(key+1) != 0){
                    result += key + 1;
                }
            }
        }
        return result;
    }
}