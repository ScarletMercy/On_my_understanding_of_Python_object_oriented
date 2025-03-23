class Kind:
    def __init__(self, num):
        self.num = num  # 初始化实例属性 num

    def speak_num(self):
        print(f'This is {self.num}')  # 访问实例属性并输出


def main():
    k = Kind(6)  # 创建实例 k，num 初始化为 6
    k.speak_num()  # 输出：This is 6
    k.num = 7  # 直接修改实例属性
    k.speak_num()  # 输出：This is 7


if __name__ == '__main__':
    main()
