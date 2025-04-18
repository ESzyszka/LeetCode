"""
You are given a non-negative integer array nums. In one operation, you must:

Choose a positive integer x such that x is less than or equal to the smallest non-zero element in nums.
Subtract x from every positive element in nums.
Return the minimum number of operations to make every element in nums equal to 0.

 

Example 1:

Input: nums = [1,5,0,3,5]
Output: 3
Explanation:
In the first operation, choose x = 1. Now, nums = [0,4,0,2,4].
In the second operation, choose x = 2. Now, nums = [0,2,0,0,2].
In the third operation, choose x = 2. Now, nums = [0,0,0,0,0].
Example 2:

Input: nums = [0]
Output: 0
Explanation: Each element in nums is already 0 so no operations are needed.

"""


class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        iterrations = 0
        while any(num > 0 for num in nums):   #For as long as at least number is greater than 0
            #Choose a positive integer x 
            positive = {i for i in nums if i !=0}
            #Choose a smallest non-zero element in nums 
            smallest = min(positive)
            print(smallest)

            #Subtracting smallest from each i in the array 
            nums = [num - smallest if num > 0 else num for num in nums]
            print(nums)
            iterrations +=1

        #You need the number of iterrations to get to nums = [0,0,0,0]
        return iterrations

  
nums = [1,5,0,3,5]
solution_1 = Solution() #initialize instance of a class
result = solution_1.minimumOperations(nums)
print("Total operations:", result)
