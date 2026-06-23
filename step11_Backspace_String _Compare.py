'''given the two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character. Note that after backspacing an empty text, the text will continue empty.
example 1: s = "ab#c", t = "ad#c" => true (both become "ac")
example 2: s = "ab##", t = "c#d#" => true (both become "")
example 3: s = "a#c", t = "b" => false (s becomes "c", t becomes "b")
'''
def backspace_compare(s: str, t: str) -> bool:
    def build(string: str) -> str:
        result = []# create an empty list to store the characters after processing backspaces
        for char in string:# iterate through each character in the string
            if char != '#':# if the character is not a backspace, append it to the result list
                result.append(char)#Append the character to the result list if it's not a backspace
            elif result:# if the character is a backspace and the result list is not empty, pop the last character from the result list
                result.pop()# pop the last character from the result list if it's a backspace and the result list is not empty
        return ''.join(result)# join the characters in the result list to form the final string after processing backspaces

    return build(s) == build(t)# compare the final strings after processing backspaces for both input strings s and t
s = "ab#c"
t = "ad#c"
print(backspace_compare(s, t))  # Output: True
'''tc of the above code is O(n + m), where n is the length of string s and m is the length of string t. This is because we iterate through each character in both strings once to build the final strings after processing backspaces. The space complexity is also O(n + m) in the worst case, as we may need to store all characters in the result lists for both strings.
sc of the above code is O(n + m), where n is the length of string s and m is the length of string t. This is because we may need to store all characters in the result lists for both strings in the worst case.'''
