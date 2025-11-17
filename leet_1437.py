from typing import List


# Given an binary array nums and an integer k, return true if all 1's are at least k places away from each other,
# otherwise return false.

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        places = []
        for i in range(len(nums)):
            if nums[i] == 1:
                places.append(i)

        for j in range(1, len(places)):
            if places[j] - places[j - 1] - 1 < k:
                return False

        return True

if __name__ == '__main__':
    nums = [1, 0, 0, 0, 1, 0, 0, 1]

    nums_2 = [1, 0, 0, 1, 0, 1]
    s = Solution()

    print(s.kLengthApart(nums_2, 2))

