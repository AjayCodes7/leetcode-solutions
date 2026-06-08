class MyQueue {

    Queue<Integer> queue;

    public MyQueue() {
        this.queue = new ArrayDeque<>();
    }
    
    public void push(int x) {
        this.queue.offer(x);
    }
    
    public int pop() {
        return this.queue.poll();
    }
    
    public int peek() {
        return this.queue.peek();
    }
    
    public boolean empty() {
        return this.queue.isEmpty();
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */