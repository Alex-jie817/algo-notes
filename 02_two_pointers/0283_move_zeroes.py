"""
0283. 移动零  Easy
https://leetcode.cn/problems/move-zeroes/

思路：快慢指针做「非零元素压缩」：slow 指向下一个非零元素该放的位置，
      fast 扫到非零就交换，保证非零元素相对顺序不变，零被换到后面。
复杂度：时间 O(n)  空间 O(1)（原地交换）
易错：
  1. 用「先覆盖再补零」写法时，补零要另起一个循环，容易漏；
  2. 交换写法里 slow 和 fast 指向同一位置时自交换无害，可以不用判断；
  3. 函数返回 None，判题是直接看 nums 被改成什么样。
"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1


if __name__ == "__main__":
    sol = Solution()
    a = [0, 1, 0, 3, 12]
    sol.moveZeroes(a)
    assert a == [1, 3, 12, 0, 0], a

    b = [0]
    sol.moveZeroes(b)
    assert b == [0]

    c = [1, 0]
    sol.moveZeroes(c)
    assert c == [1, 0]
    print("ok")
