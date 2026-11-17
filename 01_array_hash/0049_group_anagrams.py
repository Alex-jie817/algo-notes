"""
0049. 字母异位词分组  Medium
https://leetcode.cn/problems/group-anagrams/

思路：异位词排序后是同一个字符串，所以「排序后的串」就是天然的哈希键。
      遍历一遍，把原词塞进对应的桶里。
复杂度：时间 O(n * k log k)（k 是最长单词长度，瓶颈在排序）
        空间 O(n * k)（结果本身要存）
易错：
  1. 键用 tuple(sorted(s)) 而不是 sorted(s)——list 不可哈希，会直接报错；
  2. 往字典里塞桶时用 setdefault 或 defaultdict，别写 if/else 判断两次；
  3. 返回 list(d.values())，直接返回 dict.values() 类型不对。
"""
from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        buckets = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))      # 排序后的串作键
            buckets[key].append(s)        # 同键进同一个桶
        return list(buckets.values())


# 进阶写法：用 26 个字母的计数元组作键，复杂度降到 O(n * k)，不依赖排序
class SolutionCounting:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        buckets = defaultdict(list)
        for s in strs:
            cnt = [0] * 26
            for ch in s:
                cnt[ord(ch) - ord("a")] += 1
            buckets[tuple(cnt)].append(s)   # tuple 才能当字典键
        return list(buckets.values())


if __name__ == "__main__":
    sol = Solution()
    got = sorted(sorted(g) for g in sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    assert got == [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]], got
    assert sol.groupAnagrams([""]) == [[""]]
    assert sol.groupAnagrams(["a"]) == [["a"]]
    print("ok")
