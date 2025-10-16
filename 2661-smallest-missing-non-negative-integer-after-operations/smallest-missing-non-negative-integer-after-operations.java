class Solution {
    public int findSmallestInteger(int[] nums, int value) {
        Map<Integer, Integer> map = new HashMap<>();
        int key;
        for(int num : nums){
            key = num%value;
            key = key >= 0 ? key:key + value;
            if(map.containsKey(key)){
                map.put(key, map.get(key) + 1);
            } else{
                map.put(key, 1);
            }
        }
        for(int i = 0; i < nums.length; i++){
            if(map.containsKey(i)) {
                map.put(i, map.get(i)-1);
                if(map.get(i) == 0){
                    map.remove(i);
                }
                continue;
            }
            else{
                int find = i % value;
                if(map.containsKey(find)){
                    map.put(find, map.get(find)-1);
                    if(map.get(find) == 0){
                        map.remove(find);
                    }
                    continue;
                } else{
                    return i;
                }
            }
        }
        return nums.length;
    }

}