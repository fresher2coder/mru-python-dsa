from Stack import Stack

stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)

print("Top:", stack.peek())
print("Popped Value:", stack.pop())
print("Top", stack.peek())

print(stack.size())
