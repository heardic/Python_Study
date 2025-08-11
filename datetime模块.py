from datetime import datetime

now = datetime.now()
format_time = now.strftime('%Y年%m月%d日 %H:%M:%S')
print(format_time)

filename = f"report_{format_time}.txt"
print('生成的文件是：',filename)



# 口诀：p = parse（解析），f = format（格式化）
# strptime()	string parse time	字符串 → 时间	把字符串“解析”成时间对象
# strftime()	string format time	时间 → 字符串	把时间“格式化”成字符串

date_str = "2025-04-05 10:30:00"
date  =  datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
print('年份是：',date.year)
print('月份是：',date.month)

