class Solution {
    public long zeroFilledSubarray(int[] nums) {
        long result = 0;
        long temp = 0;
        for(int i = 0; i < nums.length; i++){
            if(nums[i] == 0){
                temp++;
            } else{
                result += (long)temp*(temp+1)/2;
                temp = 0;
            }
        }
        if(temp != 0){
            result += (long)temp*(temp+1)/2;
        }
        return result;
    }
}