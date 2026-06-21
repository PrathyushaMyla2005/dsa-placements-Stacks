'''decode string
Given an encoded string, return its decoded string.
The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
example:
input: s = "3[a]2[bc]"
output: "aaabcbc"
'''
def decodeString(s):
    stck = [] # stack to store numbers and strings
    current_string = '' # current string being built
    current_num = 0 # current number being built
    for ch in s:#iterate through each character in the input string
        if ch.is_digit(): # if the character is a digit
            current_num = current_num * 10 + int(ch) # build the currentnumber by multiplying the previous number by 10 and adding the new digit
        elif ch == '[': # if the character is an opening bracket
            stck.append(current_string) # push the current string onto the stack
            stck.append(current_num) # push the current number onto the stack
            current_string = '' # reset the current string
            current_num = 0 # reset the current number
        elif ch == ']': # if the character is a closing bracket
            num = stck.pop() # pop the number from the stack
            prev_string = stck.pop() # pop the previous string from the stack
            current_string = prev_string + current_string * num # build the new current string by repeating the current string num times and concatenating it with the previous string
        else: # if the character is a letter
            current_string += ch # add the character to the current string
    return current_string # the final result will be the current string after processing all characters
s = "3[a]2[bc]"
result = decodeString(s)
print(result) # Output: "aaabcbc"
'''tc = o(n) where n is the length of the input string, since we are iterating through the string once. The space complexity is O(m) where m is the maximum depth of nested brackets, as we may store intermediate strings and numbers in the stack.
sc = o(m) where m is the maximum depth of nested brackets, as we are using a stack to store intermediate strings and numbers. In the worst case, we may store all intermediate strings and numbers in the stack if there are many nested brackets.
'''