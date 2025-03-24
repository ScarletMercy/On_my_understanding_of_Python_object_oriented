class Lei():
    def __init__(self, num):
        self.num = num  # 实例属性初始化

    def __str__(self):
        """对象字符串表示（用户友好）"""
        return f'此数为{self.num}'  # 输出示例：此数为5

    def __eq__(self, other):
        """相等性判断（覆盖默认的对象ID比较）"""
        if not isinstance(other, self.__class__):
            return False  # 类型不同直接返回False
        return self.num == other.num  # 值相等则视为同一对象

    def __bool__(self):
        """布尔上下文转换（如if判断）"""
        return self.num > 0  # 正数为True，0或负数为False

    def __hash__(self):
        """自定义哈希值（影响字典/集合中的存储）"""
        return hash(self.num * 1012)  # 通过数值计算唯一哈希

    def __del__(self):
        """析构方法（对象销毁时触发）"""
        print('__del__被调用了')  # 对象回收时输出提示


def main():
    a = Lei(0)
    b = Lei(5)
    print(a == b)  # 输出 False（值不同）
    print(bool(a))  # 输出 False（a.num=0 ）
    print(hash(b))  # 输出 b.num*1012 的哈希值


if __name__ == '__main__':
    main()
    # 程序结束时，a和b的__del__会触发（输出顺序不确定）

# 1. __str__
# 推荐场景：
# 需要人类可读的对象描述（如日志、调试信息）
# 替代默认的 <__main__.Lei object at 0x...> 输出
# 不推荐操作：
# 在业务逻辑中依赖其返回值（应通过属性或方法获取数据）
# 2. __eq__
# 推荐实现：
# 类型检查：isinstance(other, self.__class__) 避免跨类误判
# 属性对比：基于核心属性（如num）而非全部属性（提升性能）
# 风险规避：
# 若类存在继承关系，需谨慎处理子类实例的对比逻辑
# 3. __bool__
# 推荐场景：
# 简化条件判断（如 if Lei(5): 等价于 if Lei(5).num > 0:）
# 替代显式的 is_valid() 方法（符合Pythonic风格）
# 注意事项：
# 未定义__bool__时，默认调用__len__，均未定义则始终返回True
# 4. __hash__
# 推荐场景：
# 对象需作为字典键或存入集合（需保证哈希值唯一且稳定）
# 风险提示：
# 若属性num可变，哈希值变化将导致集合/字典中的对象丢失
# 此处*1012的操作需文档化说明，避免维护者误解
# 5. __del__
# 不推荐场景：
# 资源释放（如文件关闭、网络连接断开），因调用时机不可控
# 替代方案：显式定义close()方法，结合上下文管理器使用
# 特殊用途：
# 调试阶段追踪对象生命周期（如本代码示例）