'''valid parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
eg input: s = "()[]{}"
output: true
'''
def isValid(s):
    stack = [] # # stack to store opening brackets
    bracket_map = {')': '(', '}': '{', ']': '['} # mapping of closing brackets to their corresponding opening brackets
    for ch in s: # iterate through each character in the input string
        if ch in bracket_map: #ifthe character is a closing bracket
            top_element = stack.pop() if stack else '#' # pop the top element from the stack, or use a dummy value if the stack is empty
            if bracket_map[ch] != top_element: # check if the popped element matches the corresponding opening bracket
                return False # if it doesn't match, the string is not valid
        else: # if the character is an opening bracket
            stack.append(ch) # push the opening bracket onto the stack
    return not stack # if the stack is empty, all brackets are matched and the string is valid; otherwise, it is not valid\
s = "()[]{}"
result = isValid(s)
print(result) # Output: True
'''tc = o(n) where n is the length of the input string, since we are iterating through the string once. The space complexity is O(n) in the worst case, as we may store all opening brackets in the stack if there are no closing brackets.
sc = o(n) in the worst case, as we may store all opening brackets in the'''