class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> result = new ArrayList<>();

        for(int i = 1; i <= numRows; i++){
            List<Integer> curr = new ArrayList<>(Collections.nCopies(i, 1));

            if(i > 2){
                List<Integer> prev = result.get(result.size() -1);
                for(int n = 1; n < i-1; n++){
                    curr.set(n, prev.get(n)+ prev.get(n-1));
                }
            }
            result.add(curr);
        }
        return result;
    }
}