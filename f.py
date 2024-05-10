import os
import re

import pyperclip

res = ""

text = pyperclip.paste()
lines = text.splitlines()

lines = [line for line in lines if line.strip() != ""]
if len(lines) % 2 != 0:
    print("剪贴板内容不合法")
    exit(1)

for i in range(0, len(lines), 2):
    res += f"- [{lines[i]}]({lines[i + 1]})\n"

filename = input("请输入文件名：")
if filename == "":
    print("未输入文件名，生成的内容将保存到剪贴板")
    pyperclip.copy(res)
    exit(0)

filename = re.sub(r'[\\/:*?"<>|]', "-", filename.strip())
fullpath = os.path.join(os.getcwd(), f"{filename}.md")
if os.path.exists(fullpath):
    print("文件已存在，生成的内容将保存到剪贴板")
    pyperclip.copy(res)
    exit(0)

with open(fullpath, "w", encoding="utf-8") as f:
    f.write(res)

os.system(f'code "{fullpath}"')
