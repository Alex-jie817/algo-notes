"""
0015. 三数之和  Medium
https://leetcode.cn/problems/3sum/

思路：排序后固定第一个数 a，剩下两数用对撞双指针找 b + c = -a；
      三个位置都要跳过重复值，否则结果集里会出现重复三元组。
复杂度：时间 O(n^2)  空间 O(1)（不计结果数组）
易错：去重的位置——外层固定值要跳、内层找到答案后左右指针也要跳；
      结果判断放在 while 里，别在移动指针前提前 break。
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > 0:
                break
            left, right = i + 1, n - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif s < 0:
                    left += 1
                else:
                    right -= 1
        return res


if __name__ == "__main__":
    assert Solution().threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert Solution().threeSum([]) == []
    assert Solution().threeSum([0, 0, 0, 0]) == [[0, 0, 0]]
    print("ok")
