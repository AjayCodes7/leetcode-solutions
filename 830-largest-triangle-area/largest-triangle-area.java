class Solution {
    public double area(int[] x, int[] y,int[] z){
        return  0.5 * (Math.abs(
                x[0]*y[1] - x[1]*y[0]
            +   y[0]*z[1] - y[1]*z[0] 
            +   z[0]*x[1] - z[1]*x[0])
            );
    }

    public double largestTriangleArea(int[][] points) {
        double result = 0;

        for(int i = 0 ;i < points.length; i++){
            for(int j = i+1; j < points.length; j++){
                for(int k = j+1; k < points.length; k++){
                    result = Math.max(result, area(points[i],points[j],points[k]));
                }
            }
        }
        return result;
    }
}