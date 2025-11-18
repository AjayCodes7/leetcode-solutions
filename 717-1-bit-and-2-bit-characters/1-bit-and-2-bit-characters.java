class Solution {
    public boolean isOneBitCharacter(int[] bits) {
        int n = bits.length;
        // if(n == 1){
        //     if(bits[0] == 0) return true;
        //     else return false;
        // }

        int i = 0;
        while(i < n){
            if(i == n - 1) return true;
            if(bits[i] == 1){
                i++;
            }
            i++;
        }
        return false;
    }
}