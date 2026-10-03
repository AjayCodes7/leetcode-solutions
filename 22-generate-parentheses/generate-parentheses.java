class Solution {
    List<String> result = new ArrayList<>();
    int l;
    public void generateP(String curr, int state){
        if(state < 0) return;

        if(curr.length() == l){
            if(state == 0)
            result.add(curr);
            return;
        }

        generateP(curr + '(', state + 1);
        generateP(curr + ')', state - 1);

    }

    public List<String> generateParenthesis(int n) {
        l = n * 2;
        generateP("", 0);
        return result;
    }
}