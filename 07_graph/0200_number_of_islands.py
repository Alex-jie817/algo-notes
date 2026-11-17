"""
0200. 岛屿数量  Medium
https://leetcode.cn/problems/number-of-islands/

思路：（自己写，先写中文再写代码。卡住就写「卡在哪一步」）

复杂度：时间 O(?)  空间 O(?)

易错：（写完后补，记录这次踩的坑）

提示：
  - 外层双重循环，遇到 '1' 就计数 +1，然后用 DFS/BFS 把整块陆地淹成 '0'
  - 直接改 grid 就不用额外开 visited，省空间也省代码
  - 递归 DFS 要判边界；网格很大时改 BFS 防递归深度爆掉
"""
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # TODO: 自己实现
        pass


if __name__ == "__main__":
    sol = Solution()
    # TODO: 补至少 3 组用例，含边界情况
    print("先把用例补上再跑")
