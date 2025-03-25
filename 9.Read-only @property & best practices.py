import math


def radius_judgement(radius):
    """半径合法性校验函数"""
    if not isinstance(radius, (int, float)):  # 类型校验：仅接受整型和浮点型
        raise TypeError('半径必须是整型或浮点型')
    elif radius >= 0:  # 值域校验：非负数
        return radius
    else:
        raise ValueError('半径必须是非负数')


class MyClass:
    def __init__(self, radius: int or float):
        self.__radius = radius_judgement(radius)  # 初始化时触发校验
        self.__area = None  # 面积缓存（延迟计算）

    @property
    def radius(self):
        """只读属性：获取当前半径值"""
        return self.__radius

    @radius.setter
    def radius(self, new_radius):
        """可写属性：修改半径时触发校验并重置缓存"""
        self.__radius = radius_judgement(new_radius)
        self.__area = None  # 清除旧面积缓存

    @property
    def area(self):
        """计算属性：动态生成面积（惰性求值）"""
        if self.__area is None:
            self.__area = round(self.__radius ** 2 * math.pi, 2)  # 保留两位小数
        return self.__area


def main():
    mc = MyClass(2)
    print(mc.area)  # 输出：12.57（首次计算）
    mc.radius = 6  # 修改半径触发缓存清除
    print(mc.area)  # 输出：113.1（重新计算）


if __name__ == '__main__':
    main()

# 方法/属性	适用场景	行业案例
# radius_judgement	输入参数合法性校验	金融系统金额校验、医疗数据范围检查
# @property	计算属性或敏感数据保护	电商库存实时统计、用户隐私数据脱敏
# 惰性计算 (area)	计算成本高的属性（如数据库查询、复杂运算）	物流路径优化、科学仿真模型
