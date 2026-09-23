// class Solution {

//     int[] nums;
//     int count = 0;
//     boolean reducable = false;

//     private int dfs(int left, int right, int x, int count){
//         if(x == 0) {
//             return count;
//         }
//         if(left > right || x < 0){
//             return Integer.MAX_VALUE;
//         }

//         int l = dfs(left + 1, right, x - nums[left], count + 1);
//         int r = dfs(left, right - 1, x - nums[right], count + 1);
//         return Math.min(l, r);
//     }

//     public int minOperations(int[] nums, int x) {
//         this.nums = nums;
//         int res = dfs(0, nums.length - 1, x, 0);
//         if(res == Integer.MAX_VALUE) return -1;
//         return res;
//     }
// }
// TLE

class Solution {
    public int minOperations(int[] nums, int x) {

        int left = nums.length, right = 0;
        int curr_sum = 0;

        while(left > 0 && x - curr_sum - nums[left - 1] >= 0){
            curr_sum += nums[left - 1];
            left--;
        }

        int n = nums.length;
        int res = Integer.MAX_VALUE;

        if(curr_sum == x) res = n - left;

        while(right < left && right < n){
            
            curr_sum += nums[right++];

            while(curr_sum > x && left < nums.length){
                curr_sum -= nums[left++];
            }

            if(curr_sum == x){
                res = Math.min(res, n - left + right);
            }
        }
        if(res == Integer.MAX_VALUE) return -1;
        return res;
    }
}







