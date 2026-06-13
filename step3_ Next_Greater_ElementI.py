'''
Next Greater Element I

Find the first greater element on the right side.

Example:
nums1 = [4,1,2]
nums2 = [1,3,4,2]

4 -> no greater element -> -1
1 -> next greater element -> 3
2 -> no greater element -> -1

Output: [-1,3,-1]
'''

def nextGreaterElement(nums1, nums2):

    result = [] # store final answer


    for num in nums1: # take each element from nums1

        index = nums2.index(num) # find position of num in nums2

        next_greater = -1 # assume no greater element


        for i in range(index+1, len(nums2)): # check right side elements

            if nums2[i] > num: # greater element found

                next_greater = nums2[i]

                break # stop after first greater element


        result.append(next_greater) # add answer


    return result # return final answer



nums1 = [4,1,2]

nums2 = [1,3,4,2]


print(nextGreaterElement(nums1, nums2))

# Output: [-1,3,-1]


'''
TC: O(m*n)
because for every nums1 element we search nums2

SC: O(1)
extra space (not counting output array)
'''