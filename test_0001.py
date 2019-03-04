class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, num in enumerate(nums[:-1]):
            for j, plus in enumerate(nums[i + 1:]):
                if num + plus == target:
                    return [i, i + 1 + j]


def test_0001():
    assert Solution().twoSum([2, 7, 8], 9) == [0, 1]
    assert Solution().twoSum([2, 7, 8], 15) == [1, 2]
    assert Solution().twoSum([2, 7, 8], 10) == [0, 2]


if __name__ == '__main__':
    print(Solution().twoSum([2, 7, 8], 15))
