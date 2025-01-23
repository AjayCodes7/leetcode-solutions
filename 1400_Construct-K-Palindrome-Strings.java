class Solution {
    public boolean canConstruct(String s, int k) {
        if(s.length() < k) return false;
        // HashMap<String, Integer> map = new HashMap<>();
        // for(int i = 0; i < s.length(); i++){
        //     int count = map.containsKey(s.substring(i,i+1)) ? map.get(s.substring(i,i+1)) : 0;
        //     map.put(s.substring(i,i+1), count + 1);
        // }
        int[] map = new int[26];
        
        for ( char ch : s.toCharArray())
        {
            map[ch-'a'] += 1;
        }

        int odds = 0;
        for(int num : map){
            if(num %2 != 0) ++odds;
        }
        if(odds > k) return false;
        return true;
    }
}