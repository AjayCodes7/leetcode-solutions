class Solution {
    public static String rle(String partial){
        StringBuilder result = new StringBuilder();
        int count = 1;
        for(int i = 1; i < partial.length();i++){
            if(partial.charAt(i-1)==partial.charAt(i)){
                    count++;
                }else{
                    result.append(count);
                    result.append(partial.charAt(i-1));
                    count = 1;
                }
            }
            result.append(count); 
            result.append(partial.charAt(partial.length()-1));
            return result.toString();
    }
    public static String recurse(int n){
        if(n == 1){
            return "1";
        }
        return rle(recurse(n-1));
    }
    public String countAndSay(int n) {
        return recurse(n);
    }
}