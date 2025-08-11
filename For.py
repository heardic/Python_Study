phone = {
    '张三':'11111111111',
    '李四':'22222222222',
    '王五':'33333333333',
    '赵六':'44444444444',
}

find_phone = input("请输入要查询的姓名:")

for key,value in phone.items():
    if key == find_phone:
        print("您查询的机主电话为:" +value)