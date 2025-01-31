class Solution {
    public int[] findThePrefixCommonArray(int[] A, int[] B) {
        int n = A.length;
        int[] map = new int[n];
        int[] res = new int[n];
        for(int i = 0; i < n; i++){
            if(i>0){
                res[i] = res[i-1];
            }
            if(++map[A[i]-1]==2){
                res[i]++;
            }
            if(++map[B[i]-1]==2){
                res[i]++;
            }
        }
        return res;
    }
}