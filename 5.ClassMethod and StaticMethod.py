class M:
    var = 6  # 类属性，所有实例和类方法共享

    @classmethod
    def cla(cls):
        """类方法：通过cls访问类属性"""
        return cls.var  # 正确操作类属性

    @staticmethod
    def sta():
        """静态方法：无需访问类/实例状态"""
        return 'This'  # 返回固定值，与类逻辑无关

    def com(self, num):
        """实例方法：操作实例或传入参数"""
        return num + 2  # 依赖参数而非实例属性,不推荐

    @staticmethod
    def stacom(num):
        """静态方法：功能与实例无关"""
        return num + 2  # 纯数学运算，无状态依赖


def main():
    print(M.cla())  # 输出6（类方法直接调用）
    print(M.sta())  # 输出'This'（静态方法调用）
    print(M().com(3))  # 输出5（实例方法需实例化）
    print(M.stacom(5))  # 输出7（静态方法直接调用）


if __name__ == '__main__':
    main()

# 1. 类方法 cla()
# 推荐场景：
# 需要读取或修改类级别状态（如计数器、全局配置）
# 实现工厂模式创建不同子类实例
# Python
# 复制
# @classmethod
# def from_config(cls, config):
#     return cls(config.param)
# 不推荐场景：
# 仅返回固定类属性值（可直接通过 M.var 访问）
# 2. 静态方法 sta()
# 推荐场景：
# 提供与类逻辑相关的工具函数（如数据格式转换）
# 替代全局函数，增强代码组织性
# Python
# 复制
# @staticmethod
# def validate_email(email):
#     return re.match(r'^[\w\.-]+@[\w\.-]+$',  email)
# 不推荐场景：
# 方法内容与类职责无关（应移至模块级函数）
# 3. 实例方法 com()
# 推荐场景：
# 操作实例特有属性（如对象状态修改）
# 实现面向对象的多态行为
# Python
# 复制
# def save(self, db):
#     db.insert(self.id,  self.data)
# 不推荐场景：
# 仅处理参数不涉及实例属性（可用静态方法替代）
# 4. 静态方法 stacom()
# 推荐场景：
# 实现无状态计算（如数学公式、类型转换）
# 与类功能紧密相关的辅助逻辑
# Python
# 复制
# @staticmethod
# def celsius_to_fahrenheit(c):
#     return c * 9/5 + 32
# 不推荐场景：
# 需要访问类属性时（应改用类方法）
