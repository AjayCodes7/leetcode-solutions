// class Solution {

//     public static int digitsSum(int num){
//         int sum = 0;
//         while(num > 0){
//             sum += num%10;
//             num /= 10;
//         }
//         return sum;
//     }

//     public int maximumSum(int[] nums) {
//         int result = -1;
//         HashMap<Integer, Integer> map = new HashMap<>();
//         for(int i = 0; i < nums.length; i++){
//             int digSum = digitsSum(nums[i]);
//             if(map.containsKey(digSum)){
//                 if(nums[i] + map.get(digSum) > result){
//                     result = nums[i] + map.get(digSum);
//                 }
//                 if(nums[i] > map.get(digSum)){
//                     map.put(digSum,nums[i]);
//                 }
//             } else{
//                 map.put(digSum,nums[i]);
//             }
//         }
//         return result;
//     }
// }


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
        int[] map = new int[82];
        map[0] = -1; // As we are not using map[0], I'll use it for storing result
        int digSum;
        for(int i = 0; i < nums.length; i++){
            digSum = digitsSum(nums[i]);
            if(map[digSum]!=0){
                if(nums[i] + map[digSum] > map[0]){
                    map[0] = nums[i] + map[digSum];
                }
            } 
            map[digSum] = Math.max(map[digSum], nums[i]);
        }
        return map[0];
    }
}