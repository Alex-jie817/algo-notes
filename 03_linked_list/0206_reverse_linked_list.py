"""
0206. 反转链表  Easy
https://leetcode.cn/problems/reverse-linked-list/

思路：三指针迭代。prev 记录已反转部分的头，cur 是当前节点，
      每步先把 cur.next 存到 nxt，再把 cur.next 指向 prev，然后整体右移一格。
复杂度：时间 O(n)  空间 O(1)
易错：循环结束返回的是 prev 不是 cur（cur 此时是 None）；
      忘记先存 nxt 就改 cur.next，链会断。
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, cur = None, head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev


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
    assert to_list(Solution().reverseList(build([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1]
    assert to_list(Solution().reverseList(build([]))) == []
    print("ok")
