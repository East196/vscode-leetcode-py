#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbersList(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = []
        up = 0
        length = max(len(l1), len(l2))
        for i in range(length):
            add = self.get(l1, i) + self.get(l2, i) + up
            here = add % 10
            result.append(here)
            up = add // 10
            if up == 1 and i == length - 1:
                result.append(1)
        return result

    def get(self, l, i):
        try:
            return l[i]
        except:
            return 0

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = None
        old = None
        up = 0
        while (True):

            add = l1.val + l2.val + up
            here = add % 10
            up = add // 10
            print(l1.val, l2.val, here, up)
            now = ListNode(here)
            if result is None and old is None:
                result = now
            else:
                old.next = now

            if not l1.next and not l2.next:
                if up == 1:
                    now.next = ListNode(1)
                break
            l1 = l1.next if l1.next else ListNode(0)
            l2 = l2.next if l2.next else ListNode(0)
            old = now
        return result
# @lc code=end

