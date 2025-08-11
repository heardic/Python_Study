#continue后 → 循环变量更新，继续检测条件
for num in [1,2,3]:
  if num==2:
      continue  # 跳过2，但3仍会处理
  print(num)  # 输出1和3

#break后 → 立即退出循环体
for num in [1,2,3]:
  if num==2:
      break    # 完全终止
  print(num)  # 只输出1



for i in range(1,101):
    if i %2 != 0:
        continue
    print(i)

    if i == 100:
        print("已达到100，break终止")
        break
