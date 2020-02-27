#
# @lc app=leetcode.cn id=344 lang=python3
#
# [344] 反转字符串
#

# @lc code=start
class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        length = len(s)
        for i in range(length//2):
            s[i],s[length-1-i]=s[length-1-i],s[i]
# @lc code=end

