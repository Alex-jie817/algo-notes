"""
0128. 最长连续序列  Medium
https://leetcode.cn/problems/longest-consecutive-sequence/

思路：把所有数丢进集合（O(1) 查找），然后只从「连续段的起点」开始往后数，
      也就是 x-1 不在集合里的那个 x。这样每个数只会被访问一次。
复杂度：时间 O(n)（每个元素最多进一次内层 while）
        空间 O(n)
易错：
  1. 不判断「起点」直接对每个数向后数，最坏退化成 O(n^2)，这题就白做了；
  2. 空数组要返回 0，别让 best 初始值把答案吃掉；
  3. 题目要的是「序列长度」，不是「连续子数组」，元素在原数组里可以不挨着。
"""
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        best = 0
        for x in s:
            if x - 1 in s:          # 不是起点，跳过，交给它的起点去数
                continue
            cur, length = x, 0
            while cur in s:         # 从起点一路往后数
                cur += 1
                length += 1
            best = max(best, length)
        return best


if __name__ == "__main__":
    sol = Solution()
    assert sol.longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
    assert sol.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
    assert sol.longestConsecutive([]) == 0
    assert sol.longestConsecutive([1, 1, 1]) == 1
    print("ok")
