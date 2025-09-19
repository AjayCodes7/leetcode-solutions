class Solution {
    public int compress(char[] chars) {
        StringBuilder result = new StringBuilder();
        
        int pos = 0;
        char curr;
        int count = 0;
        while (pos < chars.length){
            curr = chars[pos];
            count = 0;
            while(pos < chars.length && curr == chars[pos]){
                count++;
                pos++;
            }
            if(count <= 1) result.append(curr);
            else{
                result.append(curr);
                result.append(count);
            }
        }
        for(int i = 0; i < result.length(); i++){
            chars[i] = result.charAt(i);
        }
        return result.length();
    }
}