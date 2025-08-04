class Small_Animal:
    def __init__(self, name, color, age):
        self.__name = name      # 动物名称
        self.__color = color    # 毛色
        self.__age = age        # 年龄
    def get_name(self):
        return self.__name
    def get_color(self):
        return self.__color
    def get_age(self):
        return self.__age

class Big_Animal(Small_Animal):
    def __init__(self,name,color,age,sound):
        super(Big_Animal,self).__init__(name,color,age)
        #私有属性，外部不可访问加"__"
        self.__sound = sound
    def get_sound(self):
        # 返回声音值，不直接打印
        return  self.__sound

Tiger = Big_Animal("Tiger","黄色","5","嗷呜")
name = Tiger.get_name()
color = Tiger.get_color()
age = Tiger.get_age()
sound = Tiger.get_sound()

print(f"姓名：{name}")
print(f"颜色：{color}")
print(f"年龄：{age}")
print(f"声音：{sound}")


