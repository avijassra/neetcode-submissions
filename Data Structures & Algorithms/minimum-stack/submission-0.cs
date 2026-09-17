public class MinStack {
    private Stack<int> _valStack;
    private Stack<int> _minStack;

    public MinStack() {
        _valStack = new Stack<int>();
        _minStack = new Stack<int>();
    }
    
    public void Push(int val) {
        _valStack.Push(val);

        if(_minStack.Count > 0) {
            if(val <= _minStack.Peek()) 
            {
                _minStack.Push(val);
            } else {
                _minStack.Push(_minStack.Peek());
            }
        } else {
            _minStack.Push(val);
        }
    }
    
    public void Pop() {
        _valStack.Pop();
        _minStack.Pop();
    }
    
    public int Top() {
        return _valStack.Peek();
    }
    
    public int GetMin() {
        return _minStack.Peek();
    }
}
