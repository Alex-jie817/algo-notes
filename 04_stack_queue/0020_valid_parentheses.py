"""
0020. 有效的括号  Easy
https://leetcode.cn/problems/valid-parentheses/

思路：左括号入栈；遇到右括号就看栈顶是不是它的另一半，
      不匹配直接 False，匹配则弹出。遍历完栈必须为空。
复杂度：时间 O(n)  空间 O(n)
易错：只写了「右括号时栈为空」的判断，忘了最后检查栈里有没有剩余左括号。
"""
from typing import List


class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")": "(", "]": "[", "}": "{"}
        stack = []
        for ch in s:
            if ch in pairs:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        return not stack


if __name__ == "__main__":
    assert Solution().isValid("()[]{}") is True
    assert Solution().isValid("(]") is False
    assert Solution().isValid("([)]") is False
    assert Solution().isValid("(") is False
    print("ok")
