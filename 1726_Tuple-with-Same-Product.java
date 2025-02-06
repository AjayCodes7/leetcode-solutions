class Solution {
    public int tupleSameProduct(int[] nums) {
        HashMap<Integer, Integer> product = new HashMap<>();
        int currProduct;
        for(int i = 0; i < nums.length; i++){
            for(int j = i+1; j < nums.length; j++){
                currProduct = nums[i] * nums[j];
                product.put(currProduct, product.getOrDefault(currProduct,0)+1);
            }
        }
        int result = 0;
        for(int cnt: product.values()){
            result += (int)(cnt * (cnt-1))/2;
        }
        return result * 8;
    }
}