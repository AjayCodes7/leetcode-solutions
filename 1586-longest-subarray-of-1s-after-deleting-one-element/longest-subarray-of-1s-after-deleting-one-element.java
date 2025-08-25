class Solution {
    public int longestSubarray(int[] nums) {
        // Sliding window Approach

        int left = 0;
        int right = 0;
        int zeros = 0;
        int ans = 0;

        for(right = 0; right < nums.length; right++){
            if(nums[right] == 0){
                zeros++;
            }
            while(zeros==2){
                if(nums[left++] == 0){
                    zeros--;
                }
            }
            ans = Math.max(ans, right-left);
        }
        return ans;
    }
}