class Small_Animals:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age

class Big_Animals(Small_Animals):
    def __init__(self,name,age,color):
        super(Big_Animals, self).__init__(name,age)
        self.__color = color
    def get_color(self):
        return self.__color


sheep = Big_Animals("羊","5","白")
name = sheep.get_name()
age = sheep.get_age()
color = sheep.get_color()

print(f"名字：{name}")
print(f"年龄：{age}")
print(f"颜色：{color}")
