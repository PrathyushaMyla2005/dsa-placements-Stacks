# Two stacks
s1 = []
s2 = []

# Push operation
def push(x):
    s1.append(x)

# Pop operation
def pop():
    if not s2:
        while s1:
            s2.append(s1.pop())
    return s2.pop()

# Peek operation
def peek():
    if not s2:
        while s1:
            s2.append(s1.pop())
    return s2[-1]

# Empty operation
def empty():
    return len(s1) == 0 and len(s2) == 0


# Driver Code
push(1)
push(2)
push(3)

print(peek())    # 1
print(pop())     # 1
print(pop())     # 2
print(empty())   # False
print(pop())     # 3
print(empty())   # True