# You are given an array of integers nums. You are also given an integer original which is the first number that needs to be searched for in nums.
#
# You then do the following steps:
#
# If original is found in nums, multiply it by two (i.e., set original = 2 * original).
# Otherwise, stop the process.
# Repeat this process with the new number as long as you keep finding the number.
# Return the final value of original.
from typing import List


class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        while original in nums:
            original = 2 * original
        return original

if __name__ == '__main__':
    s = Solution()

    nums = [5, 3, 6, 1, 12]
    print(s.findFinalValue(nums, 3))

    nums = [2, 7, 9]
    print(s.findFinalValue(nums, 4))