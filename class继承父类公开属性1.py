class Small_Animal:
    def __init__(self, name, color, age):
        self.name = name      # 动物名称
        self.color = color    # 毛色
        self.age = age        # 年龄

    def get_info(self):
        print(f"动物名称: {self.name}")
        print(f"毛色: {self.color}")
        print(f"年龄: {self.age}")

class Big_Animal(Small_Animal):
    def __init__(self,name,color,age,sound):
        super(Big_Animal,self).__init__(name,color,age)
        #私有属性，外部不可访问加"__"
        self.sound = sound

    def get_sound(self):
        print(f"声音：{self.sound}")

Tiger = Big_Animal("Tiger","黄色","5","嗷呜")
Tiger.name = 9999999
Tiger.get_info()
Tiger.get_sound()
