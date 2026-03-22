"""
Python基础 - 变量与数据类型
运行此文件学习Python的基础语法
"""

# ============ 1. 变量定义 ============
print("=" * 40)
print("1. 变量定义")
print("=" * 40)

# Python是动态类型语言，不需要声明类型
name = "张三"
age = 25
height = 1.75
is_student = True

print(f"姓名: {name}, 年龄: {age}, 身高: {height}m, 是学生: {is_student}")

# 同时赋值多个变量
x, y, z = 1, 2, 3
print(f"x={x}, y={y}, z={z}")


# ============ 2. 数据类型 ============
print("\n" + "=" * 40)
print("2. 数据类型")
print("=" * 40)

# 整数
integer_num = 42
print(f"整数: {integer_num}, 类型: {type(integer_num)}")

# 浮点数
float_num = 3.14159
print(f"浮点数: {float_num}, 类型: {type(float_num)}")

# 字符串
text = "Hello, Python!"
print(f"字符串: {text}, 类型: {type(text)}")

# 布尔值
bool_val = True
print(f"布尔值: {bool_val}, 类型: {type(bool_val)}")


# ============ 3. 类型转换 ============
print("\n" + "=" * 40)
print("3. 类型转换")
print("=" * 40)

str_num = "100"
print(f"字符串 '{str_num}' 转整数: {int(str_num)}")

float_num = 3.7
print(f"浮点数 {float_num} 转整数: {int(float_num)}")

num = 2024
print(f"整数 {num} 转字符串: '{str(num)}'")

# ============ 4. 字符串格式化 ============
print("\n" + "=" * 40)
print("4. 字符串格式化")
print("=" * 40)

# f-string (推荐方式，Python 3.6+)
name = "李四"
age = 30
print(f"我的名字是{name}，今年{age}岁")

# 格式化数字
price = 19.99
print(f"价格: {price:.2f}元")

# 计算表达式
a, b = 5, 3
print(f"{a} + {b} = {a + b}")
print(f"{a} 的平方是 {a**2}")


# ============ 5. 获取用户输入 ============
print("\n" + "=" * 40)
print("5. 用户输入交互示例")
print("=" * 40)

# 注意：在PyCharm中运行时，输入内容后按回车
# 取消下面的注释来测试交互输入
# user_name = input("请输入你的名字: ")
# user_age = int(input("请输入你的年龄: "))
# print(f"你好 {user_name}，你今年 {user_age} 岁")


# ============ 练习题 ============
print("\n" + "=" * 40)
print("练习题")
print("=" * 40)

# 练习1：计算圆的面积和周长
radius = 5
pi = 3.14159
area = pi * radius ** 2
circumference = 2 * pi * radius
print(f"\n练习1: 半径为{radius}的圆")
print(f"面积: {area:.2f}")
print(f"周长: {circumference:.2f}")

# 练习2：温度转换
celsius = 25
fahrenheit = celsius * 9/5 + 32
print(f"\n练习2: {celsius}°C = {fahrenheit:.1f}°F")

# ============ 你来试试 ============
print("\n" + "=" * 40)
print("你来试试")
print("=" * 40)
print("请在下面编写你的代码：")
# 在这里写你的代码...

# 提示：尝试计算矩形面积
# 长度 = 10，宽度 = 5，计算面积
