class Students:
    def __init__(self, name: str, age: int):
        if not isinstance(name, str):  # 名称类型校验（对象创建时触发）
            raise TypeError('名称必须是字符串')
        elif len(name.strip()) == 0:  # 名称长度校验（对象创建时触发）
            raise ValueError('名称长度必须大于0')
        else:
            self.__name = name  # 私有属性：名称修饰为_Students__name（强封装）
        if age < 0:  # 年龄非负校验（对象创建时触发）
            raise ValueError('年龄必须是非负数！！！')
        else:
            self.__age = age  # 私有属性：名称修饰为_Students__age

    @property
    def name(self):
        """只读属性：提供姓名访问接口（无setter）"""
        return self.__name

    @property
    def age(self):
        """可读属性：返回当前年龄值"""
        return self.__age

    @age.setter
    def age(self, new_age):
        """可写属性：修改年龄时触发二次校验"""
        if new_age < 0:
            raise ValueError('年龄必须是非负数！！！')
        self.__age = new_age


def main():
    s1 = Students('超能┗|｀O′|┛', 6)
    print(s1.name)  # 输出：超能┗|｀O′|┛（通过@property访问）
    s1.age = 10  # 通过@age.setter 修改年龄
    print(s1.age)  # 输出：10


if __name__ == '__main__':
    main()
