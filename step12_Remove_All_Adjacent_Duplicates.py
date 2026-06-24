'''Remove All Adjacent Duplicates in String
example 1:
Input: s = "abbaca"
Output: "ca"'''
def  remove_element(s):
    stack = [] # create an empty list to use as a stack
    for char in s:  # iterate through each character in the string
        if stack and stack[-1] == char:  # if the stack is not empty and the top element of the stack is equal to the current character
            stack.pop()  # pop the top element from the stack (remove the adjacent duplicate)
        else:
            stack.append(char)  # append the current character to the stack (no adjacent duplicate)
    return ''.join(stack)  # join the characters in the stack to form the final string after removing adjacent duplicates
s = "abbaca"
print(remove_element(s))  # Output: "ca"
'''tc of the above code is O(n), where n is the length of the input string s. This is because we iterate through each character in the string once to process and remove adjacent duplicates. The space complexity is also O(n) in the worst case, as we may need to store all characters in the stack if there are no adjacent duplicates.
sc of the above code is O(n), where n is the length of the input string s. This is because we may need to store all characters in the stack in the worst case if there are no adjacent duplicates.'''