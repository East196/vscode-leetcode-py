#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        r=-1
        for i,c in enumerate(s):
            f=True
            for j,k in enumerate(s[i:]):
                if c==k:
                    f=False
            if f:
                return i 
        return r
        
# @lc code=end

if __name__ == "__main__":
    print(Solution().firstUniqChar("leetcode"))
