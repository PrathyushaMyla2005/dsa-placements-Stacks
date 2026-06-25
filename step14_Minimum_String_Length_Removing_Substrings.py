'''Minimum String Length After Removing Substrings
example:
Input: s = "ABAB"
Output: 0
Explanation: Remove "AB" repeatedly until the string is empty.'''
def min_length(s):
    stack = []  # create an empty list to use as a stack
    for char in s:  # iterate through each character in the string
        if stack and (
            (stack[-1] == 'A' and char == 'B') or (stack[-1] == 'B' and char == 'A') or
            (stack[-1] == 'C' and char == 'D') or (stack[-1] == 'D' and char == 'C')
        ):  # if the stack is not empty and the top element of the stack is equal to the current character (case-insensitive) and they are not the same character
            stack.pop()  # pop the top element from the stack (remove the adjacent duplicate)
        else:
            stack.append(char)  # append the current character to the stack (no adjacent duplicate)
    return len(stack)  # return the length of the stack, which represents the minimum length of the string after removing substring
s = "ABAB"
print(min_length(s))  # Output: 0
'''tc of the above code is O(n), where n is the length of the input string s. This is because we iterate through each character in the string once to process and remove adjacent duplicates. The space complexity is also O(n) in the worst case, as we may need to store all characters in the stack if there are no adjacent duplicates.
sc of the above code is O(n), where n is the length of the input string s
'''
