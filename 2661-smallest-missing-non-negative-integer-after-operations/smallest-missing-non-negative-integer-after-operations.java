class Solution {
    public int findSmallestInteger(int[] nums, int value) {
        Map<Integer, Integer> map = new HashMap<>();
        int key;
        for(int num : nums){
            key = (num%value + value)%value;
            map.put(key, map.getOrDefault(key,0) + 1);
        }
        int i = 0;
        while (true) {
            int rem = i % value;
            if (!map.containsKey(rem) || map.get(rem) == 0) {
                return i;
            }
            map.put(rem, map.get(rem) - 1);
            i++;
        }
    }
}