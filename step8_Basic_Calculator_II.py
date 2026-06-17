'''given a string s which represents an expression, evaluate this expression and return its value. The integer division should truncate toward zero.
example:
input: s = "3+2*2"
output: 7
'''
def calculate(s):
    stack = [] # store numbers and intermediate results 
    num = 0 # current number being processed
    sign = '+' # current sign, initialized to '+' for the first number
    for i,ch in enumerate(s):
        if ch.isdigit(): # if the character is a digit, build the current number
            num = num * 10 + int(ch)
        if ch in '+-*/' or i == len(s) - 1: # if the character is an operator or the last character
            if sign == '+':
                stack.append(num) # add the current number to the stack
            elif sign == '-':
                stack.append(-num) # subtract the current number from the stack
            elif sign == '*':
                stack[-1] = stack[-1] * num # multiply the last number in the stack by the current number
            elif sign == '/':
                # perform integer division and truncate toward zero
                stack[-1] = int(stack[-1] / num) 
            sign = ch # update the current sign to the new operator
            num = 0 # reset the current number for the next iteration
    return sum(stack) # return the sum of all numbers in the stack, which is the final result
s = "3+2*2"
result = calculate(s)
print(result) # Output: 7
'''tc = o(n) where n is the length of the string s, since we are iterating through the string once. The space complexity is also O(n) in the worst case, as we may store all numbers in the stack.
sc = o(n) where n is the length of the string s, since we are using a stack to store numbers and intermediate results. In the worst case, we may store all numbers in the stack.'''