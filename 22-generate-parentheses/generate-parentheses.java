class Solution {
    List<String> result = new ArrayList<>();
    int l;
    public void generateP(StringBuilder curr, int state){
        if(state < 0) return;

        if(curr.length() == l){
            if(state == 0)
            result.add(curr.toString());
            return;
        }

        curr.append('(');
        generateP(curr, state + 1);
        curr.deleteCharAt(curr.length() - 1);
        
        curr.append(')');
        generateP(curr, state - 1);
        curr.deleteCharAt(curr.length() - 1);


    }

    public List<String> generateParenthesis(int n) {
        l = n * 2;
        generateP(new StringBuilder(), 0);
        return result;
    }
}