class Solution {
    public boolean isPowerOfFour(int n) {
        if(n <= 0){
            return false;
        }
        double num = Math.log(n)/Math.log(4);        
        if((int)num == num){
            return true;
        }
        return false;
    }
}