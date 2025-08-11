import sys模块

daan = input("你想继续吗？(y/n): ")
daan = daan.lower()  # 把输入变成小写

if daan != 'y':
    print("退出")
    sys.exit(0)
else:
    print("程序运行")


if len(sys.argv) < 2:
    print("正确用法为./脚本 + 参数")
    sys.exit(1)

shuchu = sys.argv[1]

print(f"你好,{shuchu}")

