class Solution {
    public int[] plusOne(int[] digits) {
        // for(int i = digits.length-1; i >= 0; i++){
        //     digits[i] += 1;
        //     if(digit[i] != 10){

        //     }
        // }
        int i = digits.length-1;
        boolean carry = false;
        while(i >= 0){
            digits[i]++;
            // No carry
            if(digits[i]!=10){
                return digits;
            }
            carry = true;
            digits[i] = 0;
            i -= 1;
        }
        int[] arr = new int[digits.length+1];
        if(carry){
            arr[0] = 1;
            System.arraycopy(digits,0, arr, 1, digits.length);
        }
        return arr;
    }
}