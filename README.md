# python程式輸出比對
用於自動比對兩個 Python 程式的執行結果是否一致，若結果不同會顯示詳細差異。

## 環境需求
- Python 3.7 以上（需支援 `subprocess.run` 的 `capture_output` 參數）
- 使用標準函式庫：
  - subprocess
  - difflib
  - os

## 功能
### 多測資批次比對
- 可一次讀取多組測資
- 使用空行分隔不同測資
### 自動判斷輸出來源
- 若程式有輸出結果 → 使用標準輸出
- 若程式為寫入檔案 → 偵測執行後新增或修改的檔案並讀取內容
### 顯示差異
- 使用 `difflib.unified_diff` 顯示兩份輸出的逐行差異：
  - -：原程式內容
  - +：比較程式內容
### 輸出結果
**輸出相同**
```
測試1: 輸出結果相同
測試2: 輸出結果相同
```

**輸出不同**
```
測試1: 輸出結果不同
--- 檔案1
+++ 檔案2
@@ -1,3 +1,3 @@
 True
-True
+False
 True
 ```


## 使用方法
1. 在 `input.txt` 中輸入測試資料，多筆資料使用空行分隔
1. 在終端機執行 `compare.py`
1. 分別輸入想要比對的兩個 python 檔案名稱

## 成果
### 執行影片
[![程式輸出比對](https://img.youtube.com/vi/hfTQgAHwfVM/maxresdefault.jpg)](https://www.youtube.com/watch?v=hfTQgAHwfVM)
