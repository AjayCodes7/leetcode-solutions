class Solution {
    public int longestValidParentheses(String s) {
        int right = 0;
        int maxLen = 0;

        Stack<Integer> stack = new Stack<>();
        stack.push(-1);

        while(right < s.length()){
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