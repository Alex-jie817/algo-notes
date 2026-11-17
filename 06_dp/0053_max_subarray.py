"""
0053. 最大子数组和  Medium
https://leetcode.cn/problems/maximum-subarray/

思路：（自己写，先写中文再写代码。卡住就写「卡在哪一步」）

复杂度：时间 O(?)  空间 O(?)

易错：（写完后补，记录这次踩的坑）

提示：
  - dp[i] 定义成「以 i 结尾的最大和」，不是「前 i 个里最大的」
  - 转移：dp[i] = max(nums[i], dp[i-1] + nums[i])，前者意味着丢掉前面
  - 初值不能设 0——数组全为负数时会错，用 nums[0] 起手
"""
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # TODO: 自己实现
        pass


if __name__ == "__main__":
    sol = Solution()
    # TODO: 补至少 3 组用例，含边界情况
    print("先把用例补上再跑")
