'''
INSTRUCTIONS: 
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.

class Solution
    def searchRange(self, nums: List[int], target: int) -> List[int]:
'''

nums = [8]
target = 8

def binary_search(nums, target): 
    lowest_index = 0
    highest_index = len(nums)-1
    middle_index = (lowest_index + highest_index) // 2

    while lowest_index <= highest_index: # search range not empty condition
        
        if nums[middle_index] == target:
            return middle_index # only return when found
            

        elif nums[middle_index] < target: 
            lowest_index = middle_index + 1
            middle_index = (lowest_index + highest_index) // 2 # search within new middle 
           

        else:
            highest_index = middle_index -1
            middle_index = (lowest_index + highest_index) // 2 # search within new middle 

    return -1 #none of conditions satisfy or range empty
            

