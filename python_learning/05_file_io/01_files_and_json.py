"""
Python文件操作和JSON处理
学习如何读写文件和处理JSON数据
"""

import json
import os

# ============ 1. 文本文件读写 ============
print("=" * 40)
print("1. 文本文件读写")
print("=" * 40)

# 写入文件
content = """Python文件操作
这是第一行
这是第二行
这是第三行
"""

# 使用 with 语句（推荐，自动关闭文件）
with open("05_file_io/test.txt", "w", encoding="utf-8") as f:
    f.write(content)
print("文件写入成功")

# 读取文件
with open("05_file_io/test.txt", "r", encoding="utf-8") as f:
    # 读取全部内容
    all_content = f.read()
    print("读取全部内容:")
    print(all_content)

# 逐行读取
print("逐行读取:")
with open("05_file_io/test.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(f"  {line.strip()}")


# ============ 2. 不同的读取模式 ============
print("\n" + "=" * 40)
print("2. 不同的读取模式")
print("=" * 40)

# read() - 全部读取
with open("05_file_io/test.txt", "r", encoding="utf-8") as f:
    full = f.read()
    print(f"read() 长度: {len(full)}")

# readline() - 读取一行
with open("05_file_io/test.txt", "r", encoding="utf-8") as f:
    first_line = f.readline()
    print(f"readline(): {first_line.strip()}")

# readlines() - 读取所有行到列表
with open("05_file_io/test.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    print(f"readlines() 行数: {len(lines)}")


# ============ 3. JSON处理 ============
print("\n" + "=" * 40)
print("3. JSON处理")
print("=" * 40)

# Python对象转JSON
data = {
    "name": "张三",
    "age": 25,
    "skills": ["Python", "Java", "C++"],
    "address": {
        "city": "北京",
        "district": "朝阳区"
    }
}

# 写入JSON文件
with open("05_file_io/data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("JSON文件写入成功")

# 读取JSON文件
with open("05_file_io/data.json", "r", encoding="utf-8") as f:
    loaded_data = json.load(f)
print(f"读取JSON: {loaded_data}")

# JSON字符串转换
json_str = json.dumps(data, ensure_ascii=False, indent=2)
print(f"\nJSON字符串:\n{json_str}")

parsed = json.loads(json_str)
print(f"\n解析后: {parsed}")


# ============ 4. CSV文件处理 ============
print("\n" + "=" * 40)
print("4. CSV文件处理")
print("=" * 40)

import csv

# 写入CSV
with open("05_file_io/students.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["姓名", "年龄", "成绩"])
    writer.writerow(["张三", 20, 85])
    writer.writerow(["李四", 21, 92])
    writer.writerow(["王五", 19, 78])
print("CSV文件写入成功")

# 读取CSV
with open("05_file_io/students.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    print("CSV内容:")
    for row in reader:
        print(f"  {row}")


# ============ 5. 文件和目录操作 ============
print("\n" + "=" * 40)
print("5. 文件和目录操作")
print("=" * 40)

# 获取当前目录
current_dir = os.getcwd()
print(f"当前目录: {current_dir}")

# 检查文件是否存在
file_path = "05_file_io/test.txt"
print(f"文件存在: {os.path.exists(file_path)}")

# 获取文件信息
if os.path.exists(file_path):
    print(f"文件大小: {os.path.getsize(file_path)} 字节")

# 列出目录内容
dir_path = "05_file_io"
if os.path.exists(dir_path):
    files = os.listdir(dir_path)
    print(f"目录内容: {files}")


# ============ 6. 配置文件处理 ============
print("\n" + "=" * 40)
print("6. 配置文件处理 (ConfigParser)")
print("=" * 40)

import configparser

# 创建配置
config = configparser.ConfigParser()
config["database"] = {
    "host": "localhost",
    "port": "3306",
    "username": "admin",
    "password": "secret"
}
config["app"] = {
    "name": "MyApp",
    "version": "1.0.0",
    "debug": "True"
}

# 写入配置文件
with open("05_file_io/config.ini", "w", encoding="utf-8") as f:
    config.write(f)
print("配置文件写入成功")

# 读取配置文件
config = configparser.ConfigParser()
config.read("05_file_io/config.ini", encoding="utf-8")

print(f"数据库主机: {config['database']['host']}")
print(f"应用名称: {config['app']['name']}")


# ============ 7. 综合练习 ============
print("\n" + "=" * 40)
print("综合练习：学生成绩管理系统")
print("=" * 40)

class StudentManager:
    """学生成绩管理系统"""

    def __init__(self, file_path):
        self.file_path = file_path
        self.students = self.load_students()

    def load_students(self):
        """从JSON文件加载学生数据"""
        if os.path.exists(self.file_path):
            with open(self.file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        return []

    def save_students(self):
        """保存学生数据到JSON文件"""
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(self.students, f, ensure_ascii=False, indent=2)

    def add_student(self, name, age, score):
        """添加学生"""
        self.students.append({
            "name": name,
            "age": age,
            "score": score
        })
        self.save_students()

    def get_average_score(self):
        """获取平均分"""
        if not self.students:
            return 0
        return sum(s["score"] for s in self.students) / len(self.students)

    def get_top_students(self, n=3):
        """获取前n名"""
        sorted_students = sorted(self.students, key=lambda x: x["score"], reverse=True)
        return sorted_students[:n]

    def print_summary(self):
        """打印摘要"""
        print(f"学生总数: {len(self.students)}")
        print(f"平均分: {self.get_average_score():.1f}")
        print(f"前3名:")
        for i, student in enumerate(self.get_top_students(), 1):
            print(f"  {i}. {student['name']}: {student['score']}分")

# 使用示例
manager = StudentManager("05_file_io/students.json")
manager.add_student("张三", 20, 85)
manager.add_student("李四", 21, 92)
manager.add_student("王五", 19, 78)
manager.add_student("赵六", 20, 95)
manager.add_student("钱七", 22, 88)

manager.print_summary()


# ============ 你来试试 ============
print("\n" + "=" * 40)
print("你来试试")
print("=" * 40)

# 练习：实现一个简单的待办事项管理器
# 1. 支持添加、删除、标记完成
# 2. 数据持久化到JSON文件
# 3. 支持按状态筛选（全部/已完成/未完成）

# 在这里写你的代码...
