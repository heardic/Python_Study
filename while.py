num = 1
num_count = 3
while True:
    input_num =  input("Please input the number:")
    input_num = int(input_num)
    if input_num == num:
        print("正确")
        break
    else:
        num_count -= 1
        if num_count == 0:
            print('超出猜测次数')
            break