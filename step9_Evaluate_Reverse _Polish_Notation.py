'''find the value of an expression in Reverse Polish Notation. Valid operators are +, -, *, /. Each operand may be an integer or another expression
in Reverse Polish Notation. Note that division between two integers should truncate toward zero.
example:
input: tokens = ["2","1","+","3","*"]
output: 9
'''
def evalRPN(tokens):
    stack = []# store numbers and intermediate results
    for token in tokens:
        if token not in '+-*/': # if the token is a number
            stack.append(int(token)) # convert it to an integer and push it onto the stack
        else: # if the token is an operator
            b = stack.pop() # pop the top two numbers from the stack
            a = stack.pop()
            if token == '+':
                stack.append(a + b) # perform addition and push the result onto the stack
            elif token == '-':
                stack.append(a - b) # perform subtraction and push the result onto the stack
            elif token == '*':
                stack.append(a * b) # perform multiplication and push the result onto the stack
            elif token == '/':
                # perform integer division and truncate toward zero
                stack.append(int(a / b))
    return stack[0] # the final result will be the only number left in the stack
tokens = ["2","1","+","3","*"]
result = evalRPN(tokens)
print(result) # Output: 9
'''tc = o(n) where n is the number of tokens, since we are iterating through the tokens once. The space complexity is also O(n) in the worst case, as we may store all numbers in the stack.
sc = o(n) where n is the number of tokens, since we are using a stack to store numbers and intermediate results. In the worst case, we may store all numbers in the stack.
'''