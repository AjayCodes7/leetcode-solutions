class Solution {

    public static int digitsSum(int num){
        int sum = 0;
        while(num > 0){
            sum += num%10;
            num /= 10;
        }
        return sum;
    }

    public int maximumSum(int[] nums) {
        int result = -1;
        HashMap<Integer, Integer> map = new HashMap<>();
        for(int i = 0; i < nums.length; i++){
            int digSum = digitsSum(nums[i]);
            if(map.containsKey(digSum)){
                if(nums[i] + map.get(digSum) > result){
                    result = nums[i] + map.get(digSum);
                }
                if(nums[i] > map.get(digSum)){
                    map.put(digSum,nums[i]);
                }
            } else{
                map.put(digSum,nums[i]);
            }
        }
        return result;
    }
}