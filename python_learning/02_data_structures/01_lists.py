"""
Python数据结构 - 列表 (List)
列表是Python中最常用的数据结构之一
"""

# ============ 1. 列表基础 ============
print("=" * 40)
print("1. 列表基础")
print("=" * 40)

# 创建列表
numbers = [1, 2, 3, 4, 5]
fruits = ["苹果", "香蕉", "橙子"]
mixed = [1, "Hello", 3.14, True]  # 可以存储不同类型

print(f"数字列表: {numbers}")
print(f"水果列表: {fruits}")
print(f"混合列表: {mixed}")

# 访问元素 (索引从0开始)
print(f"\n第一个元素: {numbers[0]}")
print(f"最后一个元素: {numbers[-1]}")
print(f"倒数第二个: {numbers[-2]}")

# 获取列表长度
print(f"列表长度: {len(numbers)}")


# ============ 2. 列表切片 ============
print("\n" + "=" * 40)
print("2. 列表切片")
print("=" * 40)

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(f"完整列表: {nums}")
print(f"nums[2:5]: {nums[2:5]}")      # [2, 3, 4]
print(f"nums[:3]: {nums[:3]}")        # [0, 1, 2]
print(f"nums[7:]: {nums[7:]}")        # [7, 8, 9]
print(f"nums[::2]: {nums[::2]}")      # [0, 2, 4, 6, 8] 步长为2
print(f"nums[::-1]: {nums[::-1]}")    # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] 反转


# ============ 3. 常用方法 ============
print("\n" + "=" * 40)
print("3. 常用方法")
print("=" * 40)

colors = ["红", "绿", "蓝"]

# 添加元素
colors.append("黄")
print(f"append后: {colors}")

# 插入元素
colors.insert(1, "紫")
print(f"insert后: {colors}")

# 删除元素
colors.remove("绿")
print(f"remove后: {colors}")

# 弹出元素 (返回并删除)
removed = colors.pop()
print(f"pop('{removed}')后: {colors}")

# 排序
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers.sort()
print(f"排序后: {numbers}")

# 反转
numbers.reverse()
print(f"反转后: {numbers}")

# 统计
nums = [1, 2, 2, 3, 3, 3]
print(f"nums中2的个数: {nums.count(2)}")
print(f"nums中3的索引: {nums.index(3)}")


# ============ 4. 列表操作 ============
print("\n" + "=" * 40)
print("4. 列表操作")
print("=" * 40)

# 列表拼接
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(f"列表拼接: {combined}")

# 列表复制
original = [1, 2, 3]
copy_list = original.copy()
copy_list[0] = 99
print(f"原列表: {original}, 复制列表: {copy_list}")

# 清空列表
nums = [1, 2, 3]
nums.clear()
print(f"clear后: {nums}")

# 检查元素是否存在
fruits = ["苹果", "香蕉", "橙子"]
print(f"'苹果' 在列表中: {'苹果' in fruits}")
print(f"'葡萄' 在列表中: {'葡萄' in fruits}")


# ============ 5. 列表推导式 ============
print("\n" + "=" * 40)
print("5. 列表推导式")
print("=" * 40)

# 创建1-10的平方列表
squares = [x**2 for x in range(1, 11)]
print(f"平方列表: {squares}")

# 过滤偶数
evens = [x for x in range(1, 21) if x % 2 == 0]
print(f"1-20的偶数: {evens}")

# 条件表达式
result = ["偶数" if x % 2 == 0 else "奇数" for x in range(1, 6)]
print(f"奇偶判断: {result}")

# 嵌套推导式 - 生成乘法表的一部分
multiplication = [f"{i}×{j}={i*j}" for i in range(1, 4) for j in range(1, 4)]
print(f"乘法表: {multiplication}")


# ============ 6. 综合练习 ============
print("\n" + "=" * 40)
print("综合练习")
print("=" * 40)

# 练习1：找出列表中最大的3个数
numbers = [23, 45, 67, 12, 89, 34, 56, 78, 90, 1]
numbers.sort(reverse=True)
top3 = numbers[:3]
print(f"练习1: 最大的3个数: {top3}")

# 练习2：删除列表中所有偶数
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_nums = [x for x in nums if x % 2 != 0]
print(f"练习2: 删除偶数后: {odd_nums}")

# 练习3：合并两个列表并去重
list_a = [1, 2, 3, 4, 5]
list_b = [3, 4, 5, 6, 7]
unique = list(set(list_a + list_b))
unique.sort()
print(f"练习3: 合并去重后: {unique}")

# 练习4：列表分组
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
groups = {
    "偶数": [x for x in nums if x % 2 == 0],
    "奇数": [x for x in nums if x % 2 != 0]
}
print(f"练习4: 分组结果: {groups}")



# ============ 你来试试 ============
print("\n" + "=" * 40)
print("你来试试")
print("=" * 40)

# 练习：实现一个简单的学生成绩管理
# 1. 创建一个包含5个学生成绩的列表
# 2. 添加一个新的成绩
# 3. 删除不及格的成绩(<60)
# 4. 计算剩余成绩的平均分
# 5. 找出最高分和最低分

# 在这里写你的代码...
