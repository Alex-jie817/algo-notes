"""
0094. 二叉树的中序遍历  Easy
https://leetcode.cn/problems/binary-tree-inorder-traversal/

思路：（自己写，先写中文再写代码。卡住就写「卡在哪一步」）

复杂度：时间 O(?)  空间 O(?)

易错：（写完后补，记录这次踩的坑）

提示：
  - 顺序是「左 - 根 - 右」，递归三行就写完
  - 迭代版用显式栈：一路向左压栈，弹出即访问，再转向右子树
  - 进阶：Morris 遍历能做到 O(1) 空间，面试问「不用栈不用递归」时用
"""
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # TODO: 自己实现
        pass


if __name__ == "__main__":
    sol = Solution()
    # TODO: 补至少 3 组用例，含边界情况
    print("先把用例补上再跑")
