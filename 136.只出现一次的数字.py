#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#

# @lc code=start
class Solution:
    def singleNumber(self, nums) -> int:
        num =0
        for i in nums:
           num = num^i
        return num
# @lc code=end

