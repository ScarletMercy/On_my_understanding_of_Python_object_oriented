class Students:
    def __init__(self, name: str, age: int):
        self.__name = name  # 双下划线私有化属性（名称修饰为_Students__name）
        if age < 0:
            raise ValueError('年龄必须是非负数！！！')  # 数据有效性校验
        else:
            self.__age = age

    def get_name(self):  # 仅提供name的读访问接口
        return self.__name

    def get_age(self):  # 传统getter方法（通过property优化）
        return self.__age

    def set_age(self, new_age):  # 传统setter方法（含业务逻辑验证）
        if new_age < 0:
            raise ValueError('年龄必须是非负数！！！')
        else:
            self.__age = new_age

    age = property(fget=get_age, fset=set_age)  # 创建age属性绑定getter/setter


def main():
    s1 = Students('超能┗|｀O′|┛', 6)
    print(s1.get_name())  # 输出：超能┗|｀O′|┛
    print(s1.get_age())  # 输出：6
    s1.set_age(9)  # 通过方法修改年龄
    print(s1.get_age())  # 输出：9
    s1.age = 10  # 通过property属性直接赋值  
    print(s1.age)  # 输出：10


if __name__ == '__main__':
    main()
