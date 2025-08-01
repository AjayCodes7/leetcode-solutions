class Solution {
    public int romanToInt(String s) {
        Map <Character, Integer> roman = new HashMap<>(Map.of('I',1,'V',5,'X', 10, 'L', 50, 'C', 100, 'D', 500, 'M', 1000));
        int result = 0;
        char[] ch = s.toCharArray();
        int i = 0;
        while(i < ch.length){
            if(ch[i] == 'I'){
                if((i + 1) < ch.length && (ch[i+1] == 'V' || ch[i+1] == 'X')){
                    result += (roman.get(ch[i+1]) - roman.get(ch[i]));
                    i += 2;
                    continue;
                }
            }else if(ch[i] == 'X'){
                if((i + 1) < ch.length && (ch[i+1] == 'L' || ch[i+1] == 'C')){
                    result += (roman.get(ch[i+1]) - roman.get(ch[i]));
                    i += 2;
                    continue;
                } 
            } else if(ch[i] == 'C'){
                if((i + 1) < ch.length && (ch[i+1] == 'D' || ch[i+1] == 'M')){
                    result += (roman.get(ch[i+1]) - roman.get(ch[i]));
                    i += 2;
                    continue;
                } 
            }
            result += roman.get(ch[i]);
            i++;
        }
        return result;
    }
}