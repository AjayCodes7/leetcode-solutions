class Solution {
    public boolean areAlmostEqual(String s1, String s2) {
        if(s1.equals(s2)){
            return true;
        }
        char a = ' ';
        char b = ' ';
        int count = 0;
        for(int i = 0; i < s1.length(); i++){
            if(s1.charAt(i)==s2.charAt(i)){
                continue;
            } else {
                switch(count){
                    case 0:
                        a = s1.charAt(i);
                        b = s2.charAt(i);
                    break;
                    case 1:
                        if(!(a == s2.charAt(i) && b == s1.charAt(i))){
                            return false;
                        }
                    break;
                    case 2:
                        return false;
                }
                count++;
            }
        }
        return count!=1;
    }
}