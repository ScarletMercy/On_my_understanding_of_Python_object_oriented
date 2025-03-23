class Pri:
    def __init__(self, name, weight):
        self._name = name  # 单下划线：受保护属性（约定内部使用）
        self.__weight = weight  # 双下划线：触发名称修饰（伪私有属性）

    def get_name(self):  # 推荐方法：通过方法访问受保护属性
        return self._name

    def get_weight(self):  # 推荐方法：安全获取私有属性
        return self.__weight

    def set_weight(self, new_weight):  # 推荐方法：控制属性修改逻辑
        self.__weight = new_weight


def main():
    p = Pri('南德飞', 166)

    # 不推荐操作：直接访问受保护属性（破坏封装性）
    print(p._name)  # 输出"南德飞"（语法允许，但违反约定）

    # 推荐操作：通过公共方法访问属性
    print(p.get_name())  # 输出"南德飞"

    try:
        # 非法操作：直接访问私有属性（触发名称修饰）
        print(p.__weight)  # 抛出 AttributeError
    except AttributeError:
        # 安全回退：通过方法获取私有属性
        print(p.get_weight())  # 输出166

    # 危险操作：通过名称修饰强制访问私有属性
    print(p._Pri__weight)  # 输出166（绕过封装，高度不推荐）

    # 推荐操作：通过方法获取最新值
    print(p.get_weight())  # 输出166

    # 推荐操作：通过方法修改私有属性
    p.set_weight(199)
    print(p.get_weight())  # 输出199


if __name__ == '__main__':
    main()  
