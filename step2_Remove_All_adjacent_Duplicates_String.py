'''remove all adjacent duplicates in a string
Given a string s, a duplicate removal consists of choosing two adjacent and equal letters and removing them.
We repeatedly make duplicate removals on s until we no longer can.
Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.
Example 1:
Input: s = "abbaca"
Output: "ca"'''
def removeDuplicates(s):
    stack = [] 
    for ch in s:
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)
    return "".join(stack)
s = "abbaca"
print(removeDuplicates)
'''tC: O(n) — because we traverse the string once and each push/pop operation takes O(1) time.

SC: O(n) — because in the worst case the stack can store all n characters. ✅'''