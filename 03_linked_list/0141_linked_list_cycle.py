"""
0141. 环形链表  Easy
https://leetcode.cn/problems/linked-list-cycle/

思路：（自己写，先写中文再写代码。卡住就写「卡在哪一步」）

复杂度：时间 O(?)  空间 O(?)

易错：（写完后补，记录这次踩的坑）

提示：
  - 快慢指针：慢的走 1 步，快的走 2 步，有环必然相遇
  - 循环条件要同时判 fast 和 fast.next，否则会空指针
  - 进阶：还要返回入环点（0142），想想相遇后怎么走
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # TODO: 自己实现
        pass


if __name__ == "__main__":
    sol = Solution()
    # TODO: 补至少 3 组用例，含边界情况
    print("先把用例补上再跑")
