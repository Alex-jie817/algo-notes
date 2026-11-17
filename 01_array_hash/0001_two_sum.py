"""
0001. 两数之和  Easy
https://leetcode.cn/problems/two-sum/

思路：一边遍历一边把「当前值 → 下标」存进哈希表；
      对每个数先查「还差多少」是否已经在表里，命中即返回。
复杂度：时间 O(n)  空间 O(n)
易错：同一个元素不能用两次，所以必须先查后存，不能先存后查。
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, x in enumerate(nums):
            need = target - x
            if need in seen:
                return [seen[need], i]
            seen[x] = i
        return []


if __name__ == "__main__":
    assert Solution().twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert Solution().twoSum([3, 2, 4], 6) == [1, 2]
    assert Solution().twoSum([3, 3], 6) == [0, 1]
    print("ok")
