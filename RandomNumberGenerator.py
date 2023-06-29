import random

def generate_random_numbers():
    # 获取用户输入的范围和个数
    start = int(input("请输入随机数的起始范围: "))
    end = int(input("请输入随机数的结束范围: "))
    count = int(input("请输入随机数的个数: "))

    # 生成指定范围和个数的随机数
    random_numbers = [random.randint(start, end) for _ in range(count)]

    # 打印生成的随机数
    print("生成的随机数为:")
    for num in random_numbers:
        print(num)

generate_random_numbers()
