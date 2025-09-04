class Solution {
    public int findClosest(int x, int y, int z) {
        int xSteps = Math.abs(x-z);
        int ySteps = Math.abs(y-z);
        if (xSteps == ySteps){
            return 0;
        } else if (xSteps < ySteps){
            return 1;
        } else{
            return 2;
        }
    }
}