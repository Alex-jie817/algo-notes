"""
0232. 用栈实现队列  Easy
https://leetcode.cn/problems/implement-queue-using-stacks/

思路：（自己写，先写中文再写代码。卡住就写「卡在哪一步」）

复杂度：时间 O(?)  空间 O(?)

易错：（写完后补，记录这次踩的坑）

提示：
  - 两个栈：in 负责入队，out 负责出队
  - 只在 out 为空时，才把 in 全部倒进 out，这样每个元素最多被搬两次
  - 想想均摊复杂度为什么是 O(1)
"""
class MyQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []


class Solution:
    def push(self, x: int) -> None:
        # TODO: 自己实现
        pass


if __name__ == "__main__":
    sol = Solution()
    # TODO: 至少写 3 组用例，包含边界情况
    print("先把用例补上再跑")
