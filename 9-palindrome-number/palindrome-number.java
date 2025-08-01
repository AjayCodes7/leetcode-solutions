class Solution {
    public boolean isPalindrome(int x) {
        if(x < 0){
            return false;
        }
        int original = x;
        int num = 0;
        int rem;
        while(x != 0){
            rem = x % 10;
            num = num*10 + rem; 
            x = x/10;
        }
        return original == num;
    }
}