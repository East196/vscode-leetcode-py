#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#
# Note: 首先自我充分测试
# @lc code=start


class Solution:
    ps = []
    p = ""

    def longestPalindrome(self, s: str) -> str:
        return self.dp(s)

    def window(self, s):
        length = len(s)
        if length == 0:
            return ""
        p = ""
        for i in range(length):
            for j in reversed(range(i+1, length)):
                if (s[i] == s[j]):
                    if len(s[i:j+1]) > len(p) and self.isPalindrome(s[i:j+1]):
                        p = s[i:j+1]
        return p if p else s[:1]

    def isPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return True
        return False

    def dp(self, s):
        self.p = ""
        length = len(s)
        if length <=1:
            return s
        for i in range(length):
            # print(s, i)
            self.findCenterPalindrome(s, i, i)
            self.findCenterPalindrome(s, i, i+1)
        return self.p

    def findCenterPalindrome(self, s: str, left: int, right: int) -> str:
        length = len(s)
        while(left>=0 and right<length and s[left]==s[right]):
            now = s[left:right+1]
            # print(s, now)
            if(len(now) > len(self.p)):
                self.p = now 
            left=left-1
            right=right+1
     


# @lc code=end

if __name__ == "__main__":
    ss = Solution().longestPalindrome("babad")
    print(ss)
