import subprocess
import difflib
import os

file1 = input("檔案1: ")
file2 = input("檔案2: ")
out_file1 = input("輸出檔案1:")
out_file2 = input("輸出檔案2:")

with open("input.txt") as f:
    test_case = f.read().strip().split("\n\n")

cmd1 = ["python", file1]
cmd2 = ["python", file2]

for i, case in enumerate(test_case, 1):
    case = case.strip() + "\n"

    output1 = subprocess.run(cmd1, input=case, capture_output=True, text=True)
    output2 = subprocess.run(cmd2, input=case, capture_output=True, text=True)

    # print(output1)
    # print(output2)

    if output1.stdout != "":  # 有 stdout
        result1 = output1.stdout
    elif os.path.exists(out_file1):  # 用檔案
        with open(out_file1, encoding="utf-8") as f:
            result1 = f.read()
    else:
        result1 = ""

    if output2.stdout != "":  # 有 stdout
        result2 = output2.stdout
    elif os.path.exists(out_file2):  # 用檔案
        with open(out_file2, encoding="utf-8") as f:
            result2 = f.read()
    else:
        result2 = ""


    if result1 == result2:
        print(f"測試{i}: 輸出結果相同")
        # print(output1.stdout)

    else:
        print(f"測試{i}: 輸出結果不同")

        diff = difflib.unified_diff(
            output1.stdout.splitlines(),
            output2.stdout.splitlines(),
            fromfile=f"{file1}",
            tofile=f"{file2}",
            lineterm=""
        )

        print("\n".join(diff))
        print("----------------")