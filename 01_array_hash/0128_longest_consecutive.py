"""
0128. 最长连续序列  Medium
https://leetcode.cn/problems/longest-consecutive-sequence/

思路：（自己写，先写中文再写代码。卡住就写「卡在哪一步」）

复杂度：时间 O(?)  空间 O(?)

易错：（写完后补，记录这次踩的坑）

提示：
  - 先把所有数放进集合，实现 O(1) 查找
  - 只从一个连续段的起点开始数（即 x-1 不在集合里），才能做到 O(n)
  - 如果不加这个「起点判断」，最坏会退化成 O(n^2)
"""
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # TODO: 自己实现
        pass


if __name__ == "__main__":
    sol = Solution()
    # TODO: 至少写 3 组用例，包含边界情况
    print("先把用例补上再跑")
