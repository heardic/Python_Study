class Animals():
    def __init__(self, name ,age ,color):
        self.name = name
        self.age = age
        self.color = color
    def get_info(self):
        print(f"名字是{self.name}")
        print(f"年龄是{self.age}")
        print(f"颜色是{self.color}")

    def new_age(self,new_age):
        self.age = new_age

my_Animals = Animals("兔兔","1","白色")
print("原始信息:")
my_Animals.get_info()

my_Animals.new_age(4)

print("\n修改后的信息:")
my_Animals.get_info()





'''
代码	含义
class Car:	定义一个类，是一个“模板”
def __init__(self, color, name):	初始化方法，用来设置初始属性
self.color = color	保存颜色
self.name = name	保存品牌
def info(self):	定义一个方法，实例可以调用它
print(...)	输出实例的属性
c = Car(...)	创建一个实例
c.info()	调用这个实例的方法
'''