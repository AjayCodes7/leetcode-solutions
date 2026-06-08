class Solution {
    public int evalRPN(String[] tokens) {
        Deque<Integer> stack = new ArrayDeque<>();
        for(String token : tokens){
            if("+-*/".contains(token)){
                int val1 = stack.pop();
                int val2 = stack.pop();
                int res = switch(token){
                    case "+" -> val2 + val1;
                    case "-" -> val2 - val1;
                    case "/" -> val2 / val1;
                    default -> val2 * val1;
                };
                stack.push(res);
            }
            else{
                stack.push(Integer.valueOf(token));
            }
        }
        return stack.pop();
    }
}