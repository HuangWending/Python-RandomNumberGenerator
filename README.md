# Python-RandomNumberGenerator
Python随机数程序
import random
导入Python的random模块，用于生成随机数。

def generate_random_numbers():
定义一个名为generate_random_numbers的函数，用于生成随机数。

start = int(input("请输入随机数的起始范围: "))
使用input函数获取用户输入的起始范围，并使用int函数将输入转换为整数类型，存储在start变量中。

end = int(input("请输入随机数的结束范围: "))
使用input函数获取用户输入的结束范围，并使用int函数将输入转换为整数类型，存储在end变量中。

count = int(input("请输入随机数的个数: "))
使用input函数获取用户输入的随机数个数，并使用int函数将输入转换为整数类型，存储在count变量中。

random_numbers = [random.randint(start, end) for _ in range(count)]
使用列表推导式和random.randint()函数生成指定范围和个数的随机数，并将结果存储在random_numbers列表中。列表推导式的循环变量_在这里没有被使用，它的作用是表示循环次数而不使用循环变量本身。

print("生成的随机数为:")
打印提示信息，表示接下来要打印生成的随机数。

for num in random_numbers:
    print(num)
使用for循环遍历random_numbers列表中的每个元素，并逐行打印每个随机数。

generate_random_numbers()
调用generate_random_numbers函数，开始执行生成随机数的操作。
