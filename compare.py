import subprocess
import difflib
import os

def get_files_state():
    # 取得目前資料夾所有檔案的修改時間
    files = {}
    for f in os.listdir():
        if os.path.isfile(f):
            files[f] = os.path.getmtime(f)

    return files


def get_changed_file(before, after):
    # 找出新增或被修改的檔案
    changed = []

    for f in after:
        if f not in before:
            changed.append(f)
        elif after[f] != before[f]:
            changed.append(f)

    return changed


def run_and_capture(cmd, case):

    before = get_files_state()
    result = subprocess.run(cmd, input=case, capture_output=True, text=True)
    after = get_files_state()

    # Error
    if result.returncode != 0:
        return f"[Error]\n{result.stderr}"

    # 1. 如果有 stdout 則直接輸出
    if result.stdout != "":
        return result.stdout

    # 2. 否則找檔案輸出
    changed_files = get_changed_file(before, after)
    if changed_files:
        # 只取第一個變動檔
        fname = changed_files[0]
        with open(fname, encoding="utf-8") as f:
            return f.read()

    # 3. 兩者都沒有
    return ""


# 主程式

file1 = input("檔案1: ")
file2 = input("檔案2: ")

# 讀入測試資料
with open("input.txt") as f:
    test_case = f.read().strip().split("\n\n")

cmd1 = ["python", file1]
cmd2 = ["python", file2]

for i, case in enumerate(test_case, 1):
    case = case.strip() + "\n"

    # 分別執行兩個 .py 檔
    output1 = run_and_capture(cmd1, case)
    output2 = run_and_capture(cmd2, case)

    # 比較輸出結果
    if output1 == output2:
        print(f"測試{i}: 輸出結果相同")
    else:
        print(f"測試{i}: 輸出結果不同")

        diff = difflib.unified_diff(
            output1.splitlines(),
            output2.splitlines(),
            fromfile=file1,
            tofile=file2,
            lineterm=""
        )

        print("\n".join(diff))
        print("----------------")