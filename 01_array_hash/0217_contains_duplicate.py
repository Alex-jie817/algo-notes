"""
0217. 存在重复元素  Easy
https://leetcode.cn/problems/contains-duplicate/

思路：（自己写，先写中文再写代码。卡住就写「卡在哪一步」）

复杂度：时间 O(?)  空间 O(?)

易错：（写完后补，记录这次踩的坑）

提示：
  - 把数丢进集合，边放边查——命中就立刻 return True，不用先建完集合
  - 比长度也是常见写法：len(set(nums)) != len(nums)
  - 想想排序法（O(n log n)）和哈希法（O(n)）各自适合什么场景
"""
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # TODO: 自己实现
        pass


if __name__ == "__main__":
    sol = Solution()
    # TODO: 补至少 3 组用例，含边界情况
    print("先把用例补上再跑")
