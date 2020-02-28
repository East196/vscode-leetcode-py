import pytest

class Solution:
    def longestCommonPrefix(self, strs):
        pre = "" 
        if not strs:
            return ""
        if len(strs)==1:
            return strs[0]
        first = strs[0]
        for i in range(len(first)):
            pre = first[:i]
            print(pre)
            f = 1 # flag用于跳出外层循环
            for s in strs[1:]:
                if i>=len(s) or s[i] !=  first[i]:
                    f = 0 
                    break
            if f==0:
                break
        return pre

def test_Solution_longestCommonPrefix():
    assert Solution().longestCommonPrefix(["flower","flow","flight"]) == "fl"
    assert Solution().longestCommonPrefix(["dog","racecar","car"]) == ""
    assert Solution().longestCommonPrefix(["a"]) == "a"
    assert Solution().longestCommonPrefix(["c","c"]) == "c"