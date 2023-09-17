class MinStack {
    
    private List<Node> stack;
    
    public MinStack() {
      stack = new ArrayList<>();
    }
    
    public void push(int val) {
        // calculate the current min value
        int min = val;
        
        if (!stack.isEmpty()) {
            // get the top node
            Node top = stack.get(stack.size() - 1);
            int oldMin = top.getMinValue();
            
            if (min >= oldMin) {
                min = oldMin;
            }
        }
        
        Node node = new Node(val, min);
        stack.add(node);
    }
    
    public void pop() {
        stack.remove(stack.size() - 1);
    }
    
    public int top() {
        return stack.get(stack.size() - 1).getValue();
    }
    
    public int getMin() {
        Node top = stack.get(stack.size() - 1);
        return top.getMinValue();
    }
    
    static class Node {
        private final int value;
        private final int minValue;
        
        Node(int value, int minValue) {
            this.value = value;
            this.minValue = minValue;
        }
        
        public int getValue() {
            return this.value;
        }
        
        public int getMinValue() {
            return this.minValue;
        }
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */