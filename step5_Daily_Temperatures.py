'''daily temperatures
Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.
Example 1:
Input: T = [73, 74, 75, 71, 69, 72, 76, 73]
Output: [1, 1, 4, 2, 1, 1, 0, 0]
Explanation: For day 0 (temperature 73), you have to wait 1 day for
a warmer temperature (74). For day 1 (temperature 74), you have to wait 1 day for a warmer temperature (75). For day 2 (temperature 75), you have to wait 4 days for a warmer temperature (76). For day 3 (temperature 71), you have to wait 2 days for a warmer temperature (72). For day 4 (temperature 69), you have to wait 1 day for a warmer temperature (72). For day 5 (temperature 72), you have to wait 1 day for a warmer temperature (76). For days 6 and 7, there are no future days for which this is possible, so they output 0.
'''
def dailyTemperatures(T):
    answer = [0] * len(T) # initialize answer array with 0s
    stack = [] # store indices of days
    for i in range(len(T)):#take every element
        while stack and T[i] > T[stack[-1]]: # check if current temp is greater than temp at index on top of stack
            prev_index = stack.pop() # get index of previous day
            answer[prev_index] = i - prev_index # calculate days to wait and update answer
        stack.append(i) # add current index to stack
    return answer
example = [73, 74, 75, 71, 69, 72, 76, 73]
print(dailyTemperatures(example))
# Output: [1, 1, 4, 2, 1, 1, 0, 0]

'''TC: O(n)
because each element is pushed and popped at most once
SC: O(n)
because in worst case all elements are in stack (e.g. strictly decreasing temperatures)
'''
