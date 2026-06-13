'''
Next Greater Element II

Find the first greater element on right side.
Array is circular, so after last index again check from start.

Example:

nums = [1,2,1]

First 1 -> next greater 2
2 -> no greater -> -1
Last 1 -> circular check -> 2

Output: [2,-1,2]
'''

def nextGreaterElements(nums):

    n = len(nums) # length of array

    result = [] # store answers


    for i in range(n): # take every element

        ans = -1 # assume no greater element


        for j in range(1, n): # check next n-1 elements

            index = (i + j) % n # circular index


            if nums[index] > nums[i]: # greater found

                ans = nums[index] # update answer

                break # stop because first greater needed


        result.append(ans) # add answer


    return result



nums = [1,2,1]

print(nextGreaterElements(nums))


# Output: [2,-1,2]


'''
TC: O(n^2)
because for every element we check remaining elements

SC: O(1)
except output array
'''