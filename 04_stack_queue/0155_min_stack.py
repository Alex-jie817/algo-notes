"""
0155. 最小栈  Medium
https://leetcode.cn/problems/min-stack/

思路：（自己写，先写中文再写代码。卡住就写「卡在哪一步」）

复杂度：时间 O(?)  空间 O(?)

易错：（写完后补，记录这次踩的坑）

提示：
  - 关键：再开一个辅助栈，和主栈同步进出，栈顶始终是当前最小值
  - push 时辅助栈压 min(新值, 辅助栈栈顶)；pop 时两个一起弹
  - 别用 min(self.stack) 糊过去——那是 O(n)，题目要 O(1)
"""

class Solution:
    pass


if __name__ == "__main__":
    # TODO: 补至少 3 组用例，含边界情况
    print("先把用例补上再跑")
