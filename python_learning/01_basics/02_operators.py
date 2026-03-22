"""
Python基础 - 运算符
运行此文件学习Python的各种运算符
"""

# ============ 1. 算术运算符 ============
print("=" * 40)
print("1. 算术运算符")
print("=" * 40)

a, b = 10, 3
print(f"a = {a}, b = {b}")
print(f"a + b = {a + b}")   # 加法: 13
print(f"a - b = {a - b}")   # 减法: 7
print(f"a * b = {a * b}")   # 乘法: 30
print(f"a / b = {a / b}")   # 除法: 3.3333...
print(f"a // b = {a // b}") # 整除: 3 (向下取整)
print(f"a % b = {a % b}")   # 取余: 1
print(f"a ** b = {a ** b}") # 幂运算: 1000


# ============ 2. 比较运算符 ============
print("\n" + "=" * 40)
print("2. 比较运算符")
print("=" * 40)

a, b = 5, 10
print(f"a = {a}, b = {b}")
print(f"a == b: {a == b}")   # 等于: False
print(f"a != b: {a != b}")   # 不等于: True
print(f"a < b: {a < b}")     # 小于: True
print(f"a > b: {a > b}")     # 大于: False
print(f"a <= b: {a <= b}")   # 小于等于: True
print(f"a >= b: {a >= b}")   # 大于等于: False

# 字符串比较
str1, str2 = "apple", "banana"
print(f"\n'{str1}' < '{str2}': {str1 < str2}")  # 按字母顺序比较


# ============ 3. 逻辑运算符 ============
print("\n" + "=" * 40)
print("3. 逻辑运算符")
print("=" * 40)

a, b = True, False
print(f"a = {a}, b = {b}")
print(f"a and b: {a and b}")  # 与: False
print(f"a or b: {a or b}")    # 或: True
print(f"not a: {not a}")       # 非: False

# 实际应用示例
age = 20
has_license = True
can_drive = age >= 18 and has_license
print(f"\n年龄={age}, 有驾照={has_license}")
print(f"可以开车: {can_drive}")

# 短路求值
print(f"\n短路求值示例:")
print(f"False and print('不会执行') = {False and print('不会执行')}")
print(f"True or print('不会执行') = {True or print('不会执行')}")


# ============ 4. 赋值运算符 ============
print("\n" + "=" * 40)
print("4. 赋值运算符")
print("=" * 40)

x = 10
print(f"x = {x}")

x += 5   # x = x + 5
print(f"x += 5 => x = {x}")

x -= 3   # x = x - 3
print(f"x -= 3 => x = {x}")

x *= 2   # x = x * 2
print(f"x *= 2 => x = {x}")

x /= 4   # x = x / 4
print(f"x /= 4 => x = {x}")

x //= 2  # x = x // 2
print(f"x //= 2 => x = {x}")

x **= 3  # x = x ** 3
print(f"x **= 3 => x = {x}")


# ============ 5. 运算符优先级 ============
print("\n" + "=" * 40)
print("5. 运算符优先级")
print("=" * 40)

# 优先级：括号 > 幂运算 > 乘除 > 加减 > 比较 > 逻辑
result = 2 + 3 * 4
print(f"2 + 3 * 4 = {result}")  # 14 (先乘后加)

result = (2 + 3) * 4
print(f"(2 + 3) * 4 = {result}")  # 20

result = 10 > 5 and 3 < 8
print(f"10 > 5 and 3 < 8 = {result}")  # True


# ============ 练习题 ============
print("\n" + "=" * 40)
print("练习题")
print("=" * 40)

# 练习1：判断闰年
year = 2024
is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
print(f"\n练习1: {year}年是闰年吗? {is_leap}")

# 练习2：判断三角形是否为直角三角形
a, b, c = 3, 4, 5
is_right_triangle = (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2)
print(f"练习2: 边长({a},{b},{c})是直角三角形吗? {is_right_triangle}")

# 练习3：计算购物折扣
original_price = 100
is_member = True
quantity = 5
final_price = original_price * quantity * (0.9 if is_member else 1) * (0.95 if quantity >= 5 else 1)
print(f"练习3: 原价¥{original_price}, 会员={is_member}, 数量={quantity}")
print(f"最终价格: ¥{final_price:.2f}")


# ============ 你来试试 ============
print("\n" + "=" * 40)
print("你来试试")
print("=" * 40)

# 编写代码：计算二次方程 ax² + bx + c = 0 的解
# a=1, b=-3, c=2
# 提示：判别式 delta = b² - 4ac
# 在这里写你的代码...

# 你的解：x1 = ?, x2 = ?
