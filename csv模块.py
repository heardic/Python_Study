# -*- coding: utf-8 -*-
import csv

print("🌟 CSV 模块练习：读和写表格数据 🌟\n")

# ==================== 1. 写入 CSV 文件 ====================
print("1. ✍️ 写入 CSV 文件：创建一个学生成绩表")

# 要写入的数据（每一行是一个学生）
students = [
    ["姓名", "年龄", "语文", "数学", "英语"],  # 表头
    ["小明", 15, 88, 92, 85],
    ["小红", 16, 90, 87, 94],
    ["小刚", 15, 78, 85, 80],
    ["小丽", 16, 92, 90, 88]
]

# 打开一个文件，准备写入
with open('students.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    # 一行一行写入
    for row in students:
        writer.writerow(row)

print("✅ 已创建文件 'students.csv'，内容已保存！")
print()

# ==================== 2. 读取 CSV 文件 ====================
print("2. 📖 读取 CSV 文件：读取刚才保存的数据")

with open('students.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        print(" | ".join(row))  # 用竖线分隔，好看一点

print()

# ==================== 3. 用字典方式写入（更直观）====================
print("3. 🏷️ 用字典写入：更清楚每一列是什么")

# 数据用字典表示，更清晰
fieldnames = ['姓名', '水果', '数量', '价格']
fruits = [
    {'姓名': '小明', '水果': '苹果', '数量': 3, '价格': 5.5},
    {'姓名': '小红', '水果': '香蕉', '数量': 6, '价格': 3.0},
    {'姓名': '小刚', '水果': '橙子', '数量': 4, '价格': 8.0},
]

with open('fruits.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()  # 先写表头
    for fruit in fruits:
        writer.writerow(fruit)

print("✅ 已创建文件 'fruits.csv'，用字典方式写入完成！")
print()

# ==================== 4. 用字典方式读取 ====================
print("4. 🔍 用字典读取：按列名读数据")

with open('fruits.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        # 可以直接用列名取值
        print(f"{row['姓名']} 买了 {row['数量']} 个 {row['水果']}，单价 {row['价格']} 元")

print()

# ==================== 5. 简单练习：筛选数据 ====================
print("5. 🔎 练习：从 students.csv 中找出数学成绩 > 90 的学生")

with open('students.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)  # 读表头
    print("数学成绩优秀的学生：")
    for row in reader:
        name = row[0]
        math_score = int(row[3])  # 数学在第4列（索引3）
        if math_score > 90:
            print(f"  ✅ {name} : {math_score} 分")

print()

# ==================== 6. 小贴士 ====================
print("💡 小贴士：")
print("  - 写文件时一定要加 newline=''，否则可能多空行")
print("  - 读写都推荐用 encoding='utf-8'，支持中文")
print("  - csv.reader() 适合按行读")
print("  - csv.DictReader() 适合按列名读，更清晰")
print("  - csv.writer() 写列表")
print("  - csv.DictWriter() 写字典，记得先 writeheader()")

print("\n🎉 学习完成！快去试试用 CSV 保存你的数据吧！")