'''valid parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Example 1:
Input: s = "()"
Output: true
Example 2:
Input: s = "()[]{}"
Output: true
Example 3:
Input: s = "(]"
Output: false
'''
def isvalid(str):
    stack = [] # create an empty stack
    match = {')':'(', '}':'{', ']':'['} # create a dictionary to match the parentheses
    for ch in str:#iterate through the string
        if ch in match: # if the character is a closing parenthesis
            stack.append(ch) # push the closing parenthesis onto the stack
        else: # if the character is an opening parenthesis
            if not stack: # if the stack is empty, return false
                return False
            top = stack.pop() # pop the top element from the stack
            if match[ch] != top: # if the popped element does not match the current character, return false
                return False
    return not stack # return true if the stack is empty, false otherwise
# test the function
print(isvalid("()")) # true
print(isvalid("()[]{}")) # true
print(isvalid("(]")) # false
'''tc: O(n) where n is the length of the string
sc: O(n) in the worst case when all characters are opening parentheses'''