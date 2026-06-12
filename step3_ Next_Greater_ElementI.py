'''find the next greater e;ement
'''
class Solution:
    def nextGreaterElement(self, nums1, nums2):

        stack = []
        mp = {}

        for num in nums2:

            while stack and stack[-1] < num:

                small = stack.pop()

                mp[small] = num


            stack.append(num)


        while stack:

            mp[stack.pop()] = -1


        ans = []

        for num in nums1:

            ans.append(mp[num])


        return ans