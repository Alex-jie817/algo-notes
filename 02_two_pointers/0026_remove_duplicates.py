"""
0026. 删除有序数组中的重复项  Easy
https://leetcode.cn/problems/remove-duplicates-from-sorted-array/

思路：（自己写，先写中文再写代码。卡住就写「卡在哪一步」）

复杂度：时间 O(?)  空间 O(?)

易错：（写完后补，记录这次踩的坑）

提示：
  - 数组有序 → 重复元素一定相邻，适合快慢指针
  - slow 指向「已确定不重复的最后一个位置」，fast 一路往前探
  - 返回值是长度，不是新数组
"""
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # TODO: 自己实现
        pass


if __name__ == "__main__":
    sol = Solution()
    # TODO: 至少写 3 组用例，包含边界情况
    print("先把用例补上再跑")
