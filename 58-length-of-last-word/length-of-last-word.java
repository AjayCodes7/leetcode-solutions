class Solution {
    public int lengthOfLastWord(String s) {
        int i = s.length();
        int result = 0;
        while(s.charAt(--i) == ' ');
        while(i >= 0 && s.charAt(i--) != ' ') result++;
        return result;
    }
}