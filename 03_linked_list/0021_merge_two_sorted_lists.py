"""
0021. 合并两个有序链表  Easy
https://leetcode.cn/problems/merge-two-sorted-lists/

思路：哑节点（dummy）+ 尾指针。每次比较两条链当前节点，小的接到 tail 后面，
      某条链走完后把另一条剩下的一段整体接上。
复杂度：时间 O(m + n)  空间 O(1)（只改指针，不新建节点）
易错：
  1. 返回 dummy.next 而不是 dummy；
  2. 循环条件用 and——任一链为空就应该停下，再用三目把剩下的接上；
  3. 不要新建 ListNode 复制值，面试官会问「能不能原地接」。
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        tail.next = list1 or list2      # 剩下的整段直接挂上
        return dummy.next


def build(vals):
    dummy = ListNode()
    tail = dummy
    for v in vals:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


def to_list(node):
    out = []
    while node:
        out.append(node.val)
        node = node.next
    return out


if __name__ == "__main__":
    sol = Solution()
    assert to_list(sol.mergeTwoLists(build([1, 2, 4]), build([1, 3, 4]))) == [1, 1, 2, 3, 4, 4]
    assert to_list(sol.mergeTwoLists(build([]), build([]))) == []
    assert to_list(sol.mergeTwoLists(build([]), build([0]))) == [0]
    print("ok")
