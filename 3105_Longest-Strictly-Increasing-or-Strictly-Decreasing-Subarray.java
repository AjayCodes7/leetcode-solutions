class Solution {
    public int longestMonotonicSubarray(int[] nums) {
        // int i = 0;
        // int result = 1;
        // int count = 1;
        // int deccount = 1;
        // while(i < nums.length - 1){
        //     if(nums[i] < nums[i+1]){
        //         count++;
        //     }else{
        //         result = Math.max(result,count);
        //         count = 1;
        //     }
        //     if(nums[i] > nums[i+1]){
        //         deccount++;
        //     }else{
        //         result = Math.max(result,deccount);
        //         deccount = 1;
        //     }
        //     i++;
        // }
        // return Math.max(result,Math.max(deccount,count));

        int[] count = new int[nums.length];
        int result = 1;
        for(int i = 1; i < nums.length; i++){
            if(nums[i-1] < nums[i]){
                if(count[i-1] >= 0){
                    count[i] = count[i-1] + 1;
                } else{
                    count[i] = 1;
                }
            }
            if(nums[i-1] > nums[i]){
                if(count[i-1] <= 0){
                    count[i] = count[i-1] - 1;
                } else{
                    count[i] = -1;
                }
            }
            result = Math.max(result,Math.abs(count[i])+1);
        }
        return result;

    }
}