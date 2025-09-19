class Solution {
    public static int binSearchList(int[][] matrix, int target){
        int left = 0;
        int right = matrix.length - 1;
        int mid;
        int n = matrix[0].length;
        while (left <= right){
            mid = (left + right)/2;
            if(target < matrix[mid][0]){
                right = mid - 1;
            } else if (target > matrix[mid][n-1]){
                left = mid + 1;
            } else{
                return mid;
            }
        }
        return -1;
    }

    public static boolean binSearch(int[] matrix, int target){
        int left = 0;
        int right = matrix.length - 1;
        int mid;
        while(left <= right){
            mid = (left + right)/2;
            if(target == matrix[mid]){
                return true;
            } else if(target < matrix[mid]){
                right = mid - 1;
            } else{
                left = mid + 1;
            }
        }
        return false;
    }

    public boolean searchMatrix(int[][] matrix, int target) {
        int idx = binSearchList(matrix, target);
        if(idx == -1){
            return false;
        }
        return binSearch(matrix[idx], target);
    }
}