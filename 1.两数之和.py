#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, num in enumerate(nums[:-1]):
            for j, plus in enumerate(nums[i + 1:]):
                if num + plus == target:
                    return [i, i + 1 + j]
# @lc code=end

