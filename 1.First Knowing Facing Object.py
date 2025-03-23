# 定义一个空类 Student，默认继承 object
class Student:
    pass


def main():
    # 打印类对象 Student 本身（调用其 __repr__ 方法）
    # 输出示例：<class '__main__.Student'>
    print(f'Student:\t{Student}')

    # id(Student)：获取 Student 类对象的内存地址标识符（整数形式）
    # 该地址在 Python 进程生命周期内唯一标识该对象
    print(f'Student的标识符：\t{id(Student)}')

    # hex(id(Student))：将内存地址转换为十六进制字符串
    # 常用于调试场景（如 CPython 源码中对象地址对比）
    print(f'Student的标识符转16进制：\t{hex(id(Student))}')

    # type(Student)：获取 Student 的类型
    # 所有类（包括内置类）的类型均为 type，体现"类即类型"的元类模型
    print(f'Student的类型：\t{type(Student)}')

    # isinstance(Student, type)：验证 Student 是否为 type 的实例
    # 类的本质是 type 元类的实例对象，此处返回 True
    print(f'Student是不是type类型：\t{isinstance(Student, type)}')

    # Student()：实例化操作，调用 __new__ 和 __init__ 方法
    # 输出示例：<__main__.Student object at 0x...>
    print(f'Student():\t{Student()}')

    # id(Student())：获取实例对象的内存地址
    # 每次实例化生成新地址，除非单例模式干预
    print(f'Student()的标识符:\t{id(Student())}')

    # hex(id(Student()))：实例地址的十六进制表示
    # 与类地址对比可观察内存分配规律
    print(f'Student()的标识符转16进制：\t{hex(id(Student()))}')

    # type(Student())：获取实例的类型
    # 实例的类型是其所属类（即 Student），体现"实例是类的实例"
    print(f'Student()的类型：\t{type(Student())}')

    # isinstance(Student(), Student)：验证实例是否属于 Student 类
    # 此处返回 True，但若存在继承关系需注意子类判断
    print(f'Student()是不是Student类型:\t{isinstance(Student(), Student)}')

    # type(type)：探究 type 元类自身的类型
    # type 是所有元类的根，其类型指向自身，形成闭环
    print(f'type是什么类型：\t{type(type)}')


if __name__ == '__main__':
    main()

#yongdaodefangfa
# id()
# type()
# hex()
# isinstance()
