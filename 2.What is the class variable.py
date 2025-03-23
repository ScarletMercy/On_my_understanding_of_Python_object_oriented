from pprint import pprint  # 导入美化输出模块，用于格式化字典


class Lei:
    change_value = 1  # 定义类属性，初始值为1


def main():
    # 打印类名（通过 __name__ 内置属性）
    print(Lei.__name__)  # 输出: Lei

    # 直接访问类属性
    print(Lei.change_value)  # 输出: 1

    # 使用 getattr 安全获取属性（属性存在时返回其值）
    print(getattr(Lei, 'change_value'))  # 输出: 1

    # 获取不存在的属性，返回默认值2
    print(getattr(Lei, 'Null', 2))  # 输出: 2

    # 动态修改类属性值为3
    setattr(Lei, 'change_value', 3)
    print(Lei.change_value)  # 输出: 3

    # 直接赋值修改类属性为4
    Lei.change_value = 4
    print(Lei.change_value)  # 输出: 4

    # 打印类的属性字典（包含所有类属性和方法）
    pprint(Lei.__dict__)  # 输出包含 'change_value': 4 的字典

    # 删除类属性 change_value
    del Lei.change_value
    pprint(Lei.__dict__)  # 输出不再包含 change_value

    # 动态添加新类属性 change_value2
    Lei.change_value2 = 5
    pprint(Lei.__dict__)  # 输出新增 'change_value2': 5

    # 访问新增属性
    print(Lei.change_value2)  # 输出: 5

    # 使用 delattr 删除属性
    delattr(Lei, 'change_value2')
    pprint(Lei.__dict__)  # 输出恢复为初始空属性（除内置属性）


if __name__ == '__main__':
    main()
# 类.__name__	获取类名称（字符串）	Lei.__name__ → "Lei"
# getattr()	安全获取属性值（支持默认值）	getattr(Lei, 'Null', 2) → 2
# setattr()	动态设置或修改类/实例属性	setattr(Lei, 'change_value', 3)
# del 语句	直接删除属性	del Lei.change_value
# delattr()	动态删除属性（等效于 del）	delattr(Lei, 'change_value2')
# 类.__dict__	查看类的命名空间字典（含所有属性）	pprint(Lei.__dict__)
# 直接属性赋值	显式修改或添加属性	Lei.change_value  = 4
