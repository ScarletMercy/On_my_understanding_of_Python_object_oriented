from typing import Union


class Animal:
    """动物基类（核心数据封装）
    - ✅ 强制类型校验：名称必须是非空字符串，体重必须为正数 
    - ⚠️ 子类需自行扩展属性校验逻辑"""

    def __init__(self, name: str, height: Union[int, float]):
        # 名称校验逻辑（严格空值检测）
        if not isinstance(name, str):  # 类型检查 
            raise TypeError('动物名称必须是字符串')
        elif len(name.strip()) == 0:  # 内容有效性检测
            raise ValueError('名称格式错误')
        else:
            self.__name = name  # 私有属性强封装 

        # 体重校验逻辑（支持int/float类型）
        if not isinstance(height, (int, float)):  # 数值类型检测 
            raise TypeError('体重必须是数字')
        elif height <= 0:  # 业务逻辑校验 
            raise ValueError('体重必须大于0')
        else:
            self.__height = height  # 私有存储 

    @property
    def name(self):
        """只读属性访问器 
        - ✅ 防止名称被意外修改 
        - 📌 需通过子类方法扩展修改逻辑"""
        return self.__name

    @property
    def height(self):
        """可监控的数值属性 
        - ✅ 通过setter方法实现安全修改"""
        return self.__height

    @height.setter
    def height(self, new_height):
        """体重修改器（复用初始化校验逻辑）
        - ✅ 确保数值合法性的统一校验 
        - ⚠️ 未实现修改日志等扩展功能"""
        if not isinstance(new_height, (int, float)):
            raise TypeError('体重必须是数字')
        elif new_height <= 0:
            raise ValueError('体重必须大于0')
        else:
            self.__height = new_height  # 安全更新 


class Dog(Animal):
    """犬科动物子类（基础实现）
    - ⚠️ 未扩展特有属性和方法 
    - 📌 直接继承父类的所有特性"""
    pass  # 空实现需后续扩展 


class Cat(Animal):
    """猫科动物子类（扩展实现）
    - ✅ 新增毛色属性及校验逻辑
    """

    def __init__(self, name, height, color):
        super().__init__(name, height)  # 调用父类初始化 
        # 毛色校验逻辑（严格字符串检测）
        if isinstance(color, str) and len(color.strip()) != 0:
            self.__color = color  # 私有存储 
        else:
            raise Exception('输入错误')  # ⚠️ 应使用具体异常类型 
        self.__live = 9  # ⚠️ 隐藏属性不公开

    @property
    def color(self):
        """毛色访问器 
        - ✅ 封装颜色数据 
        - 📌 未实现颜色枚举限制"""
        return self.__color

    @color.setter
    def color(self, new_color):
        """毛色修改器（复用校验逻辑）
        - ✅ 确保颜色非空 
        - ⚠️ 异常类型不明确"""
        if isinstance(new_color, str) and len(new_color.strip()) != 0:
            self.__color = new_color
        else:
            raise Exception('输入错误')  # ⚠️ 应细分异常类型 


def main():
    """功能测试模块 
    - ✅ 验证属性访问和修改逻辑 
    - ⚠️ 未包含异常处理测试"""
    dog1 = Dog('地狱三头犬', 99)  # ✅ 正常实例化 
    print(dog1.height)  # 输出:99

    cat1 = Cat('炼狱九头猫', 299, 'black')  # ✅ 扩展类实例化
    cat1.height = 399  # ✅ 调用父类setter
    print(cat1.height)  # 输出:399

    cat1.color = 'red'  # ✅ 调用子类setter
    print(cat1.color)  # 输出:red 


if __name__ == '__main__':
    main()  # 执行测试用例
