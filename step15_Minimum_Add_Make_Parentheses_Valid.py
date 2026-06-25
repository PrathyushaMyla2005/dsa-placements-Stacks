'''minimum add to make parentheses valid
example 1:
Input: s = "())"
Output: 1
'''
def min_add_to_make_valid(s):
    stack = []  # create an empty list to use as a stack
    count = 0  # initialize a counter to keep track of the number of unmatched parentheses
    for char in s:  # iterate through each character in the string
        if char == '(':  # if the current character is an opening parenthesis
            stack.append(char)  # append it to the stack
        elif char == ')':  # if the current character is a closing parenthesis
            if stack:  # if the stack is not empty
                stack.pop()  # pop the top element from the stack (match the closing parenthesis with an opening one)
            else:
                count += 1  # increment the counter for unmatched closing parentheses
    return count + len(stack)  # return the total number of unmatched parentheses (unmatched closing + unmatched opening)
s = "())"
print(min_add_to_make_valid(s))  # Output: 1
s = "((("
print(min_add_to_make_valid(s))  # Output: 3
'''tc of the above code is O(n), where n is the length of the input string s. This is because we iterate through each character in the string once to process and match parentheses. The space complexity is also O(n) in the worst case, as we may need to store all opening parentheses in the stack if there are no matching closing parentheses.
sc of the above code is O(n), where n is the length of the input string s'''
    