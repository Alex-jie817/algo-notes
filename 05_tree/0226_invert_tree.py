"""
0226. 翻转二叉树  Easy
https://leetcode.cn/problems/invert-binary-tree/

思路：（自己写，先写中文再写代码。卡住就写「卡在哪一步」）

复杂度：时间 O(?)  空间 O(?)

易错：（写完后补，记录这次踩的坑）

提示：
  - 先交换左右孩子，再分别递归两棵子树
  - 前序和后序都能做，中序遍历会做错——想清楚为什么
  - 返回的是 root 本身，不是新节点
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # TODO: 自己实现
        pass


if __name__ == "__main__":
    sol = Solution()
    # TODO: 补至少 3 组用例，含边界情况
    print("先把用例补上再跑")
