"""
0207. 课程表  Medium
https://leetcode.cn/problems/course-schedule/

思路：（自己写，先写中文再写代码。卡住就写「卡在哪一步」）

复杂度：时间 O(?)  空间 O(?)

易错：（写完后补，记录这次踩的坑）

提示：
  - 本质是「有向图判环」：能排完 = 无环
  - BFS 拓扑排序：算入度，入度 0 的入队，弹一个就把邻居入度减 1
  - 最后看已处理课程数是否等于 numCourses；DFS 三色标记也行
"""
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # TODO: 自己实现
        pass


if __name__ == "__main__":
    sol = Solution()
    # TODO: 补至少 3 组用例，含边界情况
    print("先把用例补上再跑")
