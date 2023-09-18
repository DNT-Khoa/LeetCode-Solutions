class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<>();
        
        // fill the stack with number
        for (String token : tokens) {
            // if token is an operand
            if (
                !token.equals("+") &&
                !token.equals("-") &&
                !token.equals("*") &&
                !token.equals("/")
            ) {
                stack.push(Integer.parseInt(token));
            } else {
                int operand1 = stack.pop();
                int operand2 = stack.pop();
                int res = 0;
                
                if (token.equals("+")) {
                    res = operand2 + operand1;
                    stack.push(res);
                } else if (token.equals("-")) {
                    res = operand2 - operand1;
                    stack.push(res);
                } else if (token.equals("*")) {
                    res = operand2 * operand1;
                    stack.push(res);
                } else {
                    res = operand2 / operand1;
                    stack.push(res);
                }
            }
        }
        
        return stack.pop();
    }
}