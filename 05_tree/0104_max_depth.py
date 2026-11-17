"""
0104. 二叉树的最大深度  Easy
https://leetcode.cn/problems/maximum-depth-of-binary-tree/

思路：（自己写，先写中文再写代码。卡住就写「卡在哪一步」）

复杂度：时间 O(?)  空间 O(?)

易错：（写完后补，记录这次踩的坑）

提示：
  - 递归定义：深度 = max(左子树深度, 右子树深度) + 1
  - 空节点的深度是多少？这是递归的终止条件
  - 进阶：用 BFS 层序遍历数层数，写一遍对比
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # TODO: 自己实现
        pass


if __name__ == "__main__":
    sol = Solution()
    # TODO: 至少写 3 组用例，包含边界情况
    print("先把用例补上再跑")
