"""
0070. 爬楼梯  Easy
https://leetcode.cn/problems/climbing-stairs/

思路：到第 n 阶只能从 n-1 或 n-2 阶上来，所以 f(n) = f(n-1) + f(n-2)，
      本质是斐波那契。只留两个变量滚动，不用数组。
复杂度：时间 O(n)  空间 O(1)
易错：n = 1 时循环一次都不进，返回的初值必须对；
      用数组写会多花 O(n) 空间，面试可以主动说「可以优化成两个变量」。
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        a, b = 1, 2
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b


if __name__ == "__main__":
    assert Solution().climbStairs(1) == 1
    assert Solution().climbStairs(2) == 2
    assert Solution().climbStairs(5) == 8
    print("ok")
