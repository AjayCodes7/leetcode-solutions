class Solution {
    public int longestValidParentheses(String s) {
        // Two Pointers Approach

        int left = 0, right = 0;
        int state = 0;
        int maxLen = 0;

        Stack<Integer> stack = new Stack<>();
        stack.push(-1);

        while(right < s.length() && left <= right){
            if(s.charAt(right) == '('){
                stack.push(right);
            } else{
                stack.pop();
                if(stack.isEmpty()){
                    stack.push(right);
                }
                if(maxLen < right - stack.peek()) maxLen = right - stack.peek();
            }
            right++;
        }
        return maxLen;
    }
}