"""
0026. 删除有序数组中的重复项  Easy
https://leetcode.cn/problems/remove-duplicates-from-sorted-array/

思路：数组有序 → 重复元素一定相邻 → 快慢指针。
      slow 指向「已确认不重复区」的最后一个位置，fast 一路往前探；
      nums[fast] 和 nums[slow] 不同，就把 slow 往前挪一格并覆盖。
复杂度：时间 O(n)  空间 O(1)（原地修改）
易错：
  1. 返回的是长度 slow + 1，不是新数组——这题只判前 k 个元素；
  2. 空数组要单独处理，否则 slow 初值会越界；
  3. 别先无脑去重再返回长度，题目要求原地改。
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        slow = 0
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1


if __name__ == "__main__":
    sol = Solution()
    a = [1, 1, 2]
    k = sol.removeDuplicates(a)
    assert k == 2 and a[:k] == [1, 2], (k, a[:k])

    b = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k = sol.removeDuplicates(b)
    assert k == 5 and b[:k] == [0, 1, 2, 3, 4], (k, b[:k])

    assert sol.removeDuplicates([]) == 0
    print("ok")
