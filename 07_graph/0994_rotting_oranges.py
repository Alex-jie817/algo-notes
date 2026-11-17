"""
0994. 腐烂的橘子  Medium
https://leetcode.cn/problems/rotting-oranges/

思路：（自己写，先写中文再写代码。卡住就写「卡在哪一步」）

复杂度：时间 O(?)  空间 O(?)

易错：（写完后补，记录这次踩的坑）

提示：
  - 多源 BFS：一开始把所有烂橘子（2）同时入队
  - 按层推进，每推进一层就是「一分钟」，层数就是答案
  - 最后要检查还有没有新鲜橘子（1）剩下，有就返回 -1
"""
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # TODO: 自己实现
        pass


if __name__ == "__main__":
    sol = Solution()
    # TODO: 补至少 3 组用例，含边界情况
    print("先把用例补上再跑")
