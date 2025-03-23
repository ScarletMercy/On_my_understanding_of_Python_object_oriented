from pprint import pprint


class Lei:
    change_value = 1


def main():
    print(Lei.__name__)
    print(Lei.change_value)
    print(getattr(Lei, 'change_value'))
    print(getattr(Lei, 'Null', 2))
    setattr(Lei,'change_value',3)
    print(Lei.change_value)
    Lei.change_value=4
    print(Lei.change_value)
    pprint(Lei.__dict__)
    del Lei.change_value
    pprint(Lei.__dict__)
    Lei.change_value2=5
    pprint(Lei.__dict__)
    print(Lei.change_value2)
    delattr(Lei,'change_value2')
    pprint(Lei.__dict__)


if __name__ == '__main__':
    main()

# 类.__name__	获取类名称（字符串）	Lei.__name__ → "Lei"
# getattr()	安全获取属性值（支持默认值）	getattr(Lei, 'Null', 2) → 2
# setattr()	动态设置或修改类/实例属性	setattr(Lei, 'change_value', 3)
# del 语句	直接删除属性	del Lei.change_value
# delattr()	动态删除属性（等效于 del）	delattr(Lei, 'change_value2')
# 类.__dict__	查看类的命名空间字典（含所有属性）	pprint(Lei.__dict__)
# 直接属性赋值	显式修改或添加属性	Lei.change_value  = 4
