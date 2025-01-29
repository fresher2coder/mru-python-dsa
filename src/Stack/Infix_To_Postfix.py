# Function to get the precedence of an operator
def precedence(op):
    if op == '^':
        return 3
    elif op == '*' or op == '/':
        return 2
    elif op == '+' or op == '-':
        return 1
    else:
        return -1


# Function to check if a character is an operator
def is_operator(ch):
    return ch in ['+', '-', '*', '/']


# Function to convert infix to postfix
def infix_to_postfix(exp):
    stack = []  # Stack implemented using a list
    result = []

    for char in exp:
        # If the character is an operand, add it to the result
        if char.isalnum():
            result.append(char)
        # If the character is '(', push it to the stack
        elif char == '(':
            stack.append(char)
        # If the character is ')', pop from the stack to result until '(' is encountered
        elif char == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()  # Pop '(' from stack
        # If the character is an operator
        else:
            while stack and precedence(char) <= precedence(stack[-1]):
                result.append(stack.pop())
            stack.append(char)

    # Pop all remaining operators from the stack to result
    while stack:
        result.append(stack.pop())

    return ''.join(result)


# Main function
if __name__ == "__main__":
    exp = input("Enter an infix expression: ")
    postfix = infix_to_postfix(exp)
    print("The postfix expression is:", postfix)
