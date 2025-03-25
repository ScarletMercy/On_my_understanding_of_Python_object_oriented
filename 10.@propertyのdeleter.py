import math
from typing import Union  # 引入类型注解标准库 


def radius_judgement(radius):
    """半径合法性校验函数（优化版）
    ✅ 支持int/float类型校验
    """
    if not isinstance(radius, (int, float)):
        raise TypeError('半径必须是整型或浮点型')  # ✅ 修正了错误提示语 
    elif radius >= 0:
        return radius
    else:
        raise ValueError('半径必须是非负数')  # ✅ 正确的值域校验 


class MyClass:
    """圆形类（缓存优化版）
    - ✅ 私有属性实现封装 
    - ✅ 类型注解使用 Union[int, float]
    - ✅ 修改半径自动清除面积缓存"""

    def __init__(self, radius: Union[int, float]):  # ✅ 类型校验：仅接受整型和浮点型
        self.__radius = radius_judgement(radius)  # ✅ 初始化校验 
        self.__area = None  # ✅ 延迟计算优化 

    @property
    def radius(self):
        """只读属性访问器 
        - ✅ 防止外部直接修改私有属性 
        - 📌 通过setter方法控制修改逻辑"""
        return self.__radius

    @radius.setter
    def radius(self, new_radius):
        """属性修改器（联动缓存控制）
        - ✅ 修改时触发合法性校验 
        - ✅ 删除缓存触发重新计算 
        - ⚠️ del语句实际调用area.deleter"""
        self.__radius = radius_judgement(new_radius)
        del self.area  # ✅ 清除缓存（触发area.deleter ）

    @property
    def area(self):
        """动态计算属性（带缓存）
        - ✅ 使用round控制精度（2位小数）
        - 📌 圆周率精度依赖math.pi 常量"""
        if self.__area is None:
            self.__area = round(self.__radius ** 2 * math.pi, 2)  # ✅ 标准数学计算
        return self.__area

    @area.deleter
    def area(self):
        """缓存清除器 
        - ✅ 安全重置缓存状态 
        - 📌 实际存储于私有变量__area"""
        self.__area = None  # ✅ 正确缓存清除方式 


def main():
    """功能演示 
    - ✅ 首次计算输出12.57 
    - ⚠️ 修改半径后未自动更新缓存（需触发del或依赖setter清除）
    - 📌 因setter已包含del，实际输出113.1"""
    mc = MyClass(2)
    print(mc.area)  # 12.57
    mc.radius = 6  # ✅ 触发setter清除缓存
    print(mc.area)  # 113.1（自动重新计算）


if __name__ == '__main__':
    main()
