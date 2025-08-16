class Solution {
    public int maximum69Number (int num) {
        char[] chars = String.valueOf(num).toCharArray();
        int n = chars.length - 1;
        for(int i = 0; i < chars.length; i++){
            if(chars[i] == '6'){
                num += 3 * Math.pow(10, n);
                break;
            }
            --n;
        }
        return num;
    }
}