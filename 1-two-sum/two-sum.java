class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> store = new HashMap<Integer, Integer>();

        for(int idx = 0; idx < nums.length; idx++){
            if(store.containsKey((target - nums[idx]))){
                return new int[] {store.get(target - nums[idx]), idx};
            }
            store.put(nums[idx], idx);
        }
        return new int[]{};
    }
}