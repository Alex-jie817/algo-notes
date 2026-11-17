"""
0011. 盛最多水的容器  Medium
https://leetcode.cn/problems/container-with-most-water/

思路：（自己写，先写中文再写代码。卡住就写「卡在哪一步」）

复杂度：时间 O(?)  空间 O(?)

易错：（写完后补，记录这次踩的坑）

提示：
  - 面积 = min(左高, 右高) × 底边宽度
  - 每一步移动「较矮的那一侧」——想清楚为什么移动高的那侧没有意义
  - 这是对撞指针，while left < right，不是 for 循环
"""
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # TODO: 自己实现
        pass


if __name__ == "__main__":
    sol = Solution()
    # TODO: 补至少 3 组用例，含边界情况
    print("先把用例补上再跑")
