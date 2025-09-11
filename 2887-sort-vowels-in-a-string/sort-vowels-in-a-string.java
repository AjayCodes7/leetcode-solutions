class Solution {
    public String sortVowels(String s) {
        char[] arr = s.toCharArray();
        String str = new String("AEIOUaeiou");
        List<Character> vowels = new ArrayList<Character>();
        for(int i = 0; i < arr.length ; i++){
            if(str.indexOf(arr[i]) != -1){
                vowels.add(arr[i]);
                arr[i] = '.';
            }
        }
        Collections.sort(vowels);
        for(int i = 0; i < arr.length ; i++){
            if(arr[i] == '.'){
                arr[i] = vowels.get(0);
                vowels.remove(0);
            }
        }
        return String.valueOf(arr);
    }
}