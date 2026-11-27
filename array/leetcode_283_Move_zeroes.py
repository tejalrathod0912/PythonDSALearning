'''

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1

        Time complexity: O(n), where n is the number of elements.
        Space complexity: O(1), because the array is modified in place.

'''

class Solution:
	def moveZeroes(self, nums: list[int]) -> list[int]:
		# i tracks where the next non-zero element should be placed.
		i = 0

		# j scans each element in the array.
		for j in range(len(nums)):
			if nums[j] != 0:
				# Move the non-zero element to the front of the array.
				nums[i], nums[j] = nums[j], nums[i]
				i += 1

		return nums


s = Solution()
answer = s.moveZeroes([0,1,0,3,12])
print(answer)
