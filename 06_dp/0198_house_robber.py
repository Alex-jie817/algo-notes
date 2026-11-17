"""
0198. 打家劫舍  Medium
https://leetcode.cn/problems/house-robber/

思路：（自己写，先写中文再写代码。卡住就写「卡在哪一步」）

复杂度：时间 O(?)  空间 O(?)

易错：（写完后补，记录这次踩的坑）

提示：
  - 定义 dp[i] 为「前 i 间房能偷到的最大金额」
  - 第 i 间房：偷它就不能偷 i-1，状态转移写出来
  - 只留两个变量做滚动，把空间压到 O(1)
"""
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # TODO: 自己实现
        pass


if __name__ == "__main__":
    sol = Solution()
    # TODO: 至少写 3 组用例，包含边界情况
    print("先把用例补上再跑")
