"""
0021. 合并两个有序链表  Easy
https://leetcode.cn/problems/merge-two-sorted-lists/

思路：（自己写，先写中文再写代码。卡住就写「卡在哪一步」）

复杂度：时间 O(?)  空间 O(?)

易错：（写完后补，记录这次踩的坑）

提示：
  - 用哑节点（dummy）省掉「头节点怎么定」的判断
  - 每次比较两个链表当前节点的值，小的接到结果尾部
  - 一条链走完后，把另一条剩下的一整段直接接上
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # TODO: 自己实现
        pass


if __name__ == "__main__":
    sol = Solution()
    # TODO: 至少写 3 组用例，包含边界情况
    print("先把用例补上再跑")
