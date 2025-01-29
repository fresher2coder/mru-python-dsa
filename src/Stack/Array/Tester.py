from Stack import Stack

stack = Stack(10)

stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)
stack.push(60)
stack.push(70)
stack.push(80)
stack.push(90)
stack.push(100)
stack.push(110)

print("Top:", stack.peek())
print("Popped Value:", stack.pop())
print("Top", stack.peek())

print(stack.size())
