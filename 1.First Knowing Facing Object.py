class Student:
    pass


def main():
    print(f'Student:\t{Student}')

    print(f'Student的标识符：\t{id(Student)}')

    print(f'Student的标识符转16进制：\t{hex(id(Student))}')

    print(f'Student的类型：\t{type(Student)}')

    print(f'Student是不是type类型：\t{isinstance(Student, type)}')

    print(f'Student():\t{Student()}')

    print(f'Student()的标识符:\t{id(Student())}')

    print(f'Student()的标识符转16进制：\t{hex(id(Student()))}')

    print(f'Student()的类型：\t{type(Student())}')

    print(f'Student()是不是Student类型:\t{isinstance(Student(), Student)}')

    print(f'type是什么类型：\t{type(type)}')


if __name__ == '__main__':
    main()

# id()
# type()
# hex()
# isinstance()
