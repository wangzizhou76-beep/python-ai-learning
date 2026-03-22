"""
Python基础 - 控制流
运行此文件学习Python的条件语句和循环
"""

# ============ 1. if 条件语句 ============
print("=" * 40)
print("1. if 条件语句")
print("=" * 40)

age = 18

if age < 18:
    print("你是未成年人")
elif age == 18:
    print("你刚满18岁，是成年人了！")
else:
    print("你是成年人")

# 多条件判断
score = 85
if score >= 90:
    grade = "优秀"
elif score >= 80:
    grade = "良好"
elif score >= 60:
    grade = "及格"
else:
    grade = "不及格"
print(f"分数 {score} 的等级是: {grade}")


# ============ 2. for 循环 ============
print("\n" + "=" * 40)
print("2. for 循环")
print("=" * 40)

# 遍历列表
fruits = ["苹果", "香蕉", "橙子"]
print("遍历水果列表:")
for fruit in fruits:
    print(f"  - {fruit}")

# 使用 range()
print("\n使用 range():")
for i in range(5):
    print(f"  i = {i}")

# range(start, stop, step)
print("\nrange(1, 10, 2):")
for i in range(1, 10, 2):
    print(f"  i = {i}")

# 同时获取索引和值
print("\n使用 enumerate():")
for index, fruit in enumerate(fruits):
    print(f"  {index}: {fruit}")


# ============ 3. while 循环 ============
print("\n" + "=" * 40)
print("3. while 循环")
print("=" * 40)

# 基本用法
count = 0
print("从0数到4:")
while count < 5:
    print(f"  count = {count}")
    count += 1

# 实际应用：猜数字游戏逻辑
import random
secret = random.randint(1, 10)
print(f"\n猜数字游戏 (秘密数字: {secret}):")
# 这里只是演示逻辑，实际使用时需要输入
print("  (在真实游戏中，这里会循环直到猜对)")


# ============ 4. break 和 continue ============
print("\n" + "=" * 40)
print("4. break 和 continue")
print("=" * 40)

# break - 跳出循环
print("使用 break 查找特定数字:")
numbers = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
target = 7
for num in numbers:
    if num == target:
        print(f"  找到目标数字 {num}!")
        break
    print(f"  检查 {num}...")

# continue - 跳过本次迭代
print("\n使用 continue 跳过偶数:")
for num in range(1, 6):
    if num % 2 == 0:
        continue
    print(f"  {num} 是奇数")


# ============ 5. 嵌套循环 ============
print("\n" + "=" * 40)
print("5. 嵌套循环")
print("=" * 40)

# 打印乘法表
print("九九乘法表 (部分):")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i}×{j}={i*j:2}", end=" ")
    print()  # 换行


# ============ 6. 综合练习 ============
print("\n" + "=" * 40)
print("综合练习")
print("=" * 40)

# 练习1：找出列表中所有偶数
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = []
for num in numbers:
    if num % 2 == 0:
        evens.append(num)
print(f"练习1: {numbers} 中的偶数: {evens}")

# 练习2：计算斐波那契数列前10项
fib = [0, 1]
for i in range(2, 10):
    fib.append(fib[i-1] + fib[i-2])
print(f"练习2: 斐波那契数列前10项: {fib}")

# 练习3：找出3到100之间的素数
primes = []
for num in range(3, 101):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)
print(f"练习3: 3-100之间的素数有 {len(primes)} 个")
print(f"前10个素数: {primes[:10]}")


# ============ 你来试试 ============
print("\n" + "=" * 40)
print("你来试试")
print("=" * 40)

# 练习：实现一个简单的成绩统计系统
# 已知学生成绩列表，计算：
# 1. 最高分、最低分、平均分
# 2. 及格的人数
# 3. 优秀(>=90)的人数

scores = [65, 78, 90, 45, 88, 92, 55, 70, 85, 95]

# 在这里写你的代码...

# 预期输出：
# 最高分: 95, 最低分: 45, 平均分: 76.3
# 及格人数: 8, 优秀人数: 3
