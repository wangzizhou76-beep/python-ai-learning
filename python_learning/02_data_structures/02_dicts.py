"""
Python数据结构 - 字典 (Dict)
字典是键值对的无序集合，是Python中非常重要的数据结构
"""

# ============ 1. 字典基础 ============
print("=" * 40)
print("1. 字典基础")
print("=" * 40)

# 创建字典
person = {
    "name": "张三",
    "age": 25,
    "city": "北京"
}
print(f"字典: {person}")

# 访问值
print(f"姓名: {person['name']}")
print(f"年龄: {person['age']}")

# 使用 get() 方法 (推荐，不会报错)
print(f"城市: {person.get('city', '未知')}")
print(f"职业: {person.get('job', '未填写')}")

# 添加键值对
person["job"] = "程序员"
print(f"添加职业后: {person}")


# ============ 2. 字典常用方法 ============
print("\n" + "=" * 40)
print("2. 字典常用方法")
print("=" * 40)

scores = {"数学": 90, "语文": 85, "英语": 88}

# 获取所有键
print(f"所有键: {list(scores.keys())}")

# 获取所有值
print(f"所有值: {list(scores.values())}")

# 获取所有键值对
print(f"所有键值对: {list(scores.items())}")

# 删除键值对
removed = scores.pop("语文")
print(f"删除 '{removed}' 后: {scores}")

# 更新字典
scores.update({"数学": 95, "物理": 82})
print(f"更新后: {scores}")


# ============ 3. 字典的遍历 ============
print("\n" + "=" * 40)
print("3. 字典的遍历")
print("=" * 40)

student = {
    "姓名": "李四",
    "年龄": 20,
    "专业": "计算机",
    "成绩": 88.5
}

# 遍历键
print("遍历键:")
for key in student:
    print(f"  {key}")

# 遍历值
print("\n遍历值:")
for value in student.values():
    print(f"  {value}")

# 遍历键值对
print("\n遍历键值对:")
for key, value in student.items():
    print(f"  {key}: {value}")


# ============ 4. 字典推导式 ============
print("\n" + "=" * 40)
print("4. 字典推导式")
print("=" * 40)

# 创建平方字典
squares = {x: x**2 for x in range(1, 6)}
print(f"平方字典: {squares}")

# 过滤字典
scores = {"张三": 85, "李四": 92, "王五": 58, "赵六": 78}
passed = {name: score for name, score in scores.items() if score >= 60}
print(f"及格学生: {passed}")

# 转换字典大小写
words = {"Hello": "你好", "World": "世界"}
upper_words = {k.upper(): v for k, v in words.items()}
print(f"大写键: {upper_words}")


# ============ 5. 嵌套字典 ============
print("\n" + "=" * 40)
print("5. 嵌套字典")
print("=" * 40)

# 复杂数据结构
class_info = {
    "班级": "计算机1班",
    "学生": [
        {"姓名": "张三", "年龄": 20, "成绩": 90},
        {"姓名": "李四", "年龄": 21, "成绩": 85},
        {"姓名": "王五", "年龄": 20, "成绩": 92}
    ],
    "老师": {
        "班主任": "刘老师",
        "任课老师": ["张老师", "王老师", "李老师"]
    }
}

print(f"班级信息:")
print(f"  班级: {class_info['班级']}")
print(f"  学生人数: {len(class_info['学生'])}")
print(f"  第一个学生: {class_info['学生'][0]['姓名']}")
print(f"  班主任: {class_info['老师']['班主任']}")


# ============ 6. 综合练习 ============
print("\n" + "=" * 40)
print("综合练习")
print("=" * 40)

# 练习1：统计字符出现次数
text = "hello world"
char_count = {}
for char in text:
    char_count[char] = char_count.get(char, 0) + 1
print(f"练习1: 字符统计: {char_count}")

# 练习2：找出成绩最高的学生
students = {
    "张三": 85,
    "李四": 92,
    "王五": 78,
    "赵六": 95,
    "钱七": 88
}
top_student = max(students.items(), key=lambda x: x[1])
print(f"练习2: 最高分学生: {top_student[0]} - {top_student[1]}分")

# 练习3：分组成绩
scores = {"张三": 85, "李四": 92, "王五": 58, "赵六": 95, "钱七": 45}
groups = {
    "优秀": {n: s for n, s in scores.items() if s >= 90},
    "及格": {n: s for n, s in scores.items() if 60 <= s < 90},
    "不及格": {n: s for n, s in scores.items() if s < 60}
}
print(f"练习3: 成绩分组:")
for level, data in groups.items():
    print(f"  {level}: {data}")


# ============ 你来试试 ============
print("\n" + "=" * 40)
print("你来试试")
print("=" * 40)

# 练习：实现一个简单的商品购物车
# 1. 创建商品字典（名称: 价格）
# 2. 创建购物车字典（商品: 数量）
# 3. 计算购物车总金额
# 4. 如果某商品数量>2，打9折

# 商品字典
products = {
    "苹果": 5,
    "香蕉": 3,
    "橙子": 4,
    "牛奶": 6
}

# 在这里写你的代码...
