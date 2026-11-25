'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104


time complexity: O(log n)
space complexity: O(1)
'''


# Binary search finds the target or its insertion position in O(log n) time.

class Solution:
	def searchInsert(self, nums: list[int], target: int) -> int:
		left = 0
		right = len(nums) - 1

		while left <= right:
			# Recompute the midpoint as the search range shrinks.
			mid = (left + right) // 2
			if target == nums[mid]:
				return mid
			elif nums[mid] < target:
				left = mid + 1
			else:
				right = mid - 1

		# left is the first index where target can be inserted without
		# changing the sorted order (including len(nums) when target is largest).
		return left

 


s = Solution()
answer = s.searchInsert([1,2,3,4,5,6,7,10],7)
print(answer)

answer1 = s.searchInsert([1,2,3,4,5,6,7,10],8)
print(answer1)

answer1 = s.searchInsert([1,2,3,4,5,6,7,10],0)
print(answer1)

