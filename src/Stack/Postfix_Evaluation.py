# Function to evaluate a postfix expression
def evaluate_postfix(exp):
    stack = []

    # Loop through each character in the expression
    for char in exp:
        # If the character is a digit, push it onto the stack
        if char.isdigit():
            stack.append(int(char))  # Convert character to integer
        else:
            # Pop two operands from the stack
            operand2 = stack.pop()
            operand1 = stack.pop()

            # Perform the operation and push the result back onto the stack
            if char == '+':
                stack.append(operand1 + operand2)
            elif char == '-':
                stack.append(operand1 - operand2)
            elif char == '*':
                stack.append(operand1 * operand2)
            elif char == '/':
                stack.append(operand1 // operand2)  # Integer division
            elif char == '^':
                stack.append(operand1 ** operand2)  # Exponentiation
            else:
                print(f"Invalid operator: {char}")
                return None

    # The result is the only element left in the stack
    return stack.pop()

# Main function
if __name__ == "__main__":
    exp = input("Enter a postfix expression: ")
    result = evaluate_postfix(exp)
    if result is not None:
        print("Result:", result)

