class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = collections.deque()
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue.append(x) # 일단 맨 뒤에 넣고
        
        # 맨 앞으로 이동
        for _ in range(len(self.queue)-1):
            self.queue.append(self.queue.popleft())
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.queue.popleft()
        

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.queue[0]
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.queue) == 0
            


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

"""
* 스택으로 큐 구현
- enqueue : inBox 스택에 데이터 push()
- dequeue : inBox의 모든 원소를 pop() -> outBox에 push()
          : outBox에서 pop()

* 큐로 스택 구현 (데이터를 넣을때 큐의 맨 앞에 넣는다!)
- push : main 큐에 있는 데이터를 dequeue() -> sub 큐에 enqueue() [원래 있던 데이터 이동]
       : 넣으려는 데이터를 main 큐에 enqueue() [큐 맨 앞에 저장]
       : sub 큐에 있는 데이터를 dequeue() -> main 큐에 enqueue() [원래 있던 데이터 이동]
- pop : main 큐에서 dequeue()
"""