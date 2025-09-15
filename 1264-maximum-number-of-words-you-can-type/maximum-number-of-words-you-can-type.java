class Solution {
    public int canBeTypedWords(String text, String brokenLetters) {
        int[] broken = new int[26];
        for(int i = 0; i < brokenLetters.length(); i++){
            broken[(int)brokenLetters.charAt(i)-97]++;
        }
        boolean flag = true;
        int result = 0;
        for(String str : text.split(" ")){
            flag = true;
            for(char ch : str.toCharArray()){
                if(broken[(int)ch-97] == 1){
                    flag = false;
                    break;
                }
            }
            if(flag) result++;
        }
        return result;
    }
}