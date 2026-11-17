"""
0242. 有效的字母异位词  Easy
https://leetcode.cn/problems/valid-anagram/

思路：（自己写，先写中文再写代码。卡住就写「卡在哪一步」）

复杂度：时间 O(?)  空间 O(?)

易错：（写完后补，记录这次踩的坑）

提示：
  - 长度不同直接 False，这一句能省掉后面所有工作
  - 26 个字母的计数数组，s 加、t 减，最后看是否全 0
  - 进阶：如果字符不限于小写字母，用字典计数；如果含 Unicode，先问面试官
"""
from typing import List

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # TODO: 自己实现
        pass


if __name__ == "__main__":
    sol = Solution()
    # TODO: 补至少 3 组用例，含边界情况
    print("先把用例补上再跑")
