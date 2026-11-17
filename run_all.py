#!/usr/bin/env python
"""
一次跑完仓库里所有题的自测，给出 PASS / TODO / FAIL 汇总。

用法：
    python run_all.py            # 跑全部
    python run_all.py 02         # 只跑 02 开头的目录
    python run_all.py -v         # 失败时打印完整报错

判定规则：
    PASS  脚本正常退出，且输出里有 ok
    TODO  脚本正常退出，但输出是「先把用例补上再跑」
    FAIL  脚本报错退出，或者输出既不是 ok 也不是 TODO
"""
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
MARK_TODO = "先把用例补上再跑"


def find_files(prefix=None):
    hits = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = sorted(d for d in dirnames if not d.startswith(".") and d != "__pycache__")
        for name in sorted(filenames):
            if not name.endswith(".py") or name == "run_all.py":
                continue
            path = os.path.join(dirpath, name)
            rel = os.path.relpath(path, ROOT).replace("\\", "/")
            if prefix and not rel.startswith(prefix):
                continue
            hits.append((rel, path))
    return sorted(hits)


def run_one(path):
    proc = subprocess.run(
        [sys.executable, path],
        capture_output=True,
        text=True,
        timeout=30,
        cwd=os.path.dirname(path),
    )
    out = (proc.stdout or "") + (proc.stderr or "")
    if proc.returncode != 0:
        return "FAIL", out.strip()
    if MARK_TODO in out and "ok" not in out.replace(MARK_TODO, ""):
        return "TODO", ""
    if "ok" in out:
        return "PASS", ""
    return "FAIL", out.strip() or "既没有输出 ok 也没有报错，检查一下文件末尾的 __main__ 段"


def main():
    args = [a for a in sys.argv[1:]]
    verbose = "-v" in args
    prefix = next((a for a in args if not a.startswith("-")), None)

    files = find_files(prefix)
    if not files:
        print("没找到匹配的 .py 文件，检查一下参数是不是目录名前缀（例如 02）")
        return 1

    buckets = {"PASS": [], "TODO": [], "FAIL": []}
    width = max(len(rel) for rel, _ in files)
    for rel, path in files:
        status, detail = run_one(path)
        buckets[status].append(rel)
        print(f"{status:4}  {rel.ljust(width)}" + (f"  <- {detail.splitlines()[-1][:80]}" if detail else ""))

    print("\n" + "-" * (width + 8))
    print(f"PASS {len(buckets['PASS'])}  |  TODO {len(buckets['TODO'])}  |  FAIL {len(buckets['FAIL'])}  |  共 {len(files)} 个文件")

    if buckets["FAIL"]:
        print("\n没过的文件：")
        for rel in buckets["FAIL"]:
            print("  -", rel)
        if verbose:
            print("\n重跑单个文件看完整报错：python " + buckets["FAIL"][0])
        return 1

    if buckets["TODO"]:
        print("\nTODO 是还没写的模板。今天挑一个，25 分钟计时器按下去。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
