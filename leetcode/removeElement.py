from typing import List


class Solution:
    def removeElement(nums: List[int], val: int):

        while nums.count(val):
            nums.remove(val)

        return nums


result = Solution.removeElement([0,1,2,2,3,0,4,2], 2)
print(result)