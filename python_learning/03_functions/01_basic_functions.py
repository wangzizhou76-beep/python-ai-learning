"""
Python函数基础
函数是可重用代码块，是Python编程的核心
"""

# ============ 1. 函数定义 ============
print("=" * 40)
print("1. 函数定义")
print("=" * 40)

def greet():
    """这是一个简单的问候函数"""
    print("你好，Python！")

# 调用函数
greet()


# ============ 2. 参数和返回值 ============
print("\n" + "=" * 40)
print("2. 参数和返回值")
print("=" * 40)

def add(a, b):
    """两个数相加"""
    return a + b

result = add(3, 5)
print(f"3 + 5 = {result}")

# 默认参数
def greet_person(name, greeting="你好"):
    """带默认参数的函数"""
    return f"{greeting}，{name}！"

print(greet_person("张三"))
print(greet_person("李四", "早上好"))


# ============ 3. 多种参数类型 ============
print("\n" + "=" * 40)
print("3. 多种参数类型")
print("=" * 40)

# 关键字参数
def describe_person(name, age, city):
    return f"{name}，{age}岁，住在{city}"

print(describe_person("王五", 25, "上海"))
print(describe_person(age=30, city="北京", name="赵六"))

# *args - 可变位置参数
def sum_all(*numbers):
    """求所有数字的和"""
    return sum(numbers)

print(f"sum_all(1, 2, 3, 4, 5) = {sum_all(1, 2, 3, 4, 5)}")

# **kwargs - 可变关键字参数
def print_info(**kwargs):
    """打印所有键值对"""
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

print("\n学生信息:")
print_info(姓名="小明", 年龄=18, 班级="高三(1)")


# ============ 4. 函数文档字符串 ============
print("\n" + "=" * 40)
print("4. 函数文档字符串")
print("=" * 40)

def calculate_circle(radius):
    """
    计算圆的面积和周长

    参数:
        radius (float): 圆的半径

    返回:
        tuple: (面积, 周长)
    """
    import math
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

area, circ = calculate_circle(5)
print(f"半径为5的圆: 面积={area:.2f}, 周长={circ:.2f}")
print(f"函数文档: {calculate_circle.__doc__}")


# ============ 5. Lambda 函数 ============
print("\n" + "=" * 40)
print("5. Lambda 函数")
print("=" * 40)

# lambda 表达式
square = lambda x: x ** 2
print(f"square(5) = {square(5)}")

# 与内置函数配合使用
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(f"平方列表: {squared}")

evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"偶数列表: {evens}")


# ============ 6. 常用内置函数 ============
print("\n" + "=" * 40)
print("6. 常用内置函数")
print("=" * 40)

# map - 对每个元素应用函数
words = ["hello", "world", "python"]
upper_words = list(map(str.upper, words))
print(f"map转大写: {upper_words}")

# filter - 过滤元素
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"filter偶数: {evens}")

# reduce - 归约
from functools import reduce
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(f"reduce求积: {product}")

# zip - 组合多个序列
names = ["张三", "李四", "王五"]
ages = [25, 30, 28]
combined = list(zip(names, ages))
print(f"zip组合: {combined}")

# sorted - 排序
students = [("张三", 85), ("李四", 92), ("王五", 78)]
sorted_by_score = sorted(students, key=lambda x: x[1], reverse=True)
print(f"按成绩排序: {sorted_by_score}")


# ============ 7. 装饰器基础 ============
print("\n" + "=" * 40)
print("7. 装饰器基础")
print("=" * 40)

def timer(func):
    """简单的计时装饰器"""
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"  执行时间: {end - start:.6f}秒")
        return result
    return wrapper

@timer
def slow_function():
    """模拟一个慢函数"""
    import time
    time.sleep(0.1)
    return "完成"

print("运行带装饰器的函数:")
slow_function()


# ============ 8. 综合练习 ============
print("\n" + "=" * 40)
print("综合练习")
print("=" * 40)

# 练习1：编写判断素数的函数
def is_prime(n):
    """判断是否为素数"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = [n for n in range(2, 50) if is_prime(n)]
print(f"练习1: 2-50之间的素数: {primes}")

# 练习2：编写统计函数
def analyze_numbers(numbers):
    """分析数字列表"""
    return {
        "最大值": max(numbers),
        "最小值": min(numbers),
        "平均值": sum(numbers) / len(numbers),
        "和": sum(numbers),
        "个数": len(numbers)
    }

nums = [23, 45, 12, 67, 34, 89, 56]
stats = analyze_numbers(nums)
print(f"练习2: 统计结果: {stats}")

# 练习3：斐波那契数列生成器
def fibonacci(n):
    """生成前n项斐波那契数列"""
    if n <= 0:
        return []
    if n == 1:
        return [0]
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

print(f"练习3: 斐波那契数列前10项: {fibonacci(10)}")


# ============ 你来试试 ============
print("\n" + "=" * 40)
print("你来试试")
print("=" * 40)

# 练习：编写以下函数
# 1. celsius_to_fahrenheit(c) - 摄氏度转华氏度
# 2. find_max_min(numbers) - 返回最大值和最小值
# 3. is_palindrome(s) - 判断字符串是否为回文

# 在这里写你的代码...
