'''given a string s which represents an expression, evaluate this expression and return its value. The integer division should truncate toward zero.
example:
input: s = "3+2*2"
output: 7
'''
def calculate(s):
    stack = [] # store numbers and intermediate results 
    