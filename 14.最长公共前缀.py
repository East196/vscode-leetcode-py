#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs):
        pre = "" # 公共前缀
        now = ""
        i = 1 
        for s in strs:
            if not now:
                now=s[:i]
            else :
                if s[:i] is not now:
                    break
            pre = pre 

# @lc code=end

