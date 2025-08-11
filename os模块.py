import os模块

# 获取当前目录
get_dir = os.getcwd()
print("当前目录是：", get_dir)
os.listdir()
print("当前文件夹有：",os.listdir())

file = '复习1.py'
if os.path.exists(file):
    print('存在')
else:
    print('Not Fount')


file = '复习.py'
# 然后检查
if os.path.isdir(file):
    print('是文件夹')
if os.path.isfile(file):
    print('是文件')

folder_name = 'Study'

if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f'{folder_name}创建成功')
else:
    print(f'{folder_name}已经存在')


# 正确拼接路径（自动适应 Windows/Mac/Linux）
path = os.path.join('data', 'config.txt')
print("路径：", path)


# 获取环境变量
username = os.environ.get('USERNAME')  # Windows
print("当前用户：", username)


# os.getcwd()	#获取当前目录
# os.listdir('.')	#列出当前文件夹内容
# os.path.exists('file')	#文件/文件夹是否存在
# os.path.isfile('x')	#是文件吗？
# os.path.isdir('x')	#是文件夹吗？
# os.mkdir('name')	#创建文件夹
# os.path.join('a', 'b')	#拼接路径（推荐！）
# os.environ.get('USERNAME')	#获取系统变量