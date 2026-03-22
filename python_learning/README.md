# Python 快速学习指南

欢迎来到Python学习之旅！本指南将帮助你在一周内从零开始，掌握Python并能使用PyCharm上手做项目。

## 环境准备

你已安装：
- Python 3.14.3 ✅
- PyCharm 2025.3.3 ✅

## 学习目录结构

```
python_learning/
├── README.md                    # 本文件 - 学习指南
├── 00_learning_path.md          # 详细学习路径
├── 01_basics/                   # 基础语法
│   ├── 01_variables_and_types.py
│   ├── 02_operators.py
│   └── 03_control_flow.py
├── 02_data_structures/          # 数据结构
│   ├── 01_lists.py
│   └── 02_dicts.py
├── 03_functions/                # 函数
│   └── 01_basic_functions.py
├── 04_oop/                      # 面向对象
│   └── 01_classes_and_objects.py
├── 05_file_io/                  # 文件操作
│   └── 01_files_and_json.py
└── 06_projects/                 # 实战项目
    ├── 01_todo_app.py          # 待办事项管理器
    ├── 02_calculator.py        # 简易计算器
    └── 03_simple_game.py       # 小游戏
```

## 一周学习计划

### Day 1-2: Python基础 (3个文件)

**目标**: 掌握Python基本语法

1. **变量与数据类型** (`01_basics/01_variables_and_types.py`)
   - 变量定义
   - 基本数据类型 (int, float, str, bool)
   - 类型转换
   - f-string 格式化

2. **运算符** (`01_basics/02_operators.py`)
   - 算术运算符
   - 比较运算符
   - 逻辑运算符
   - 运算符优先级

3. **控制流** (`01_basics/03_control_flow.py`)
   - if/elif/else
   - for 循环
   - while 循环
   - break 和 continue

**练习**: 运行每个文件，阅读代码，完成"你来试试"部分

### Day 3: 数据结构 (2个文件)

**目标**: 掌握列表和字典

1. **列表** (`02_data_structures/01_lists.py`)
   - 创建和访问
   - 切片操作
   - 常用方法
   - 列表推导式

2. **字典** (`02_data_structures/02_dicts.py`)
   - 创建和访问
   - 常用方法
   - 字典推导式
   - 嵌套字典

### Day 4: 函数 (1个文件)

**目标**: 掌握函数定义和调用

**基础函数** (`03_functions/01_basic_functions.py`)
   - 函数定义
   - 参数和返回值
   - 默认参数
   - *args 和 **kwargs
   - Lambda 表达式
   - 高阶函数 (map, filter, reduce)

### Day 5: 面向对象 (1个文件)

**目标**: 理解类和对象

**类与对象** (`04_oop/01_classes_and_objects.py`)
   - 类的定义
   - __init__ 方法
   - 实例属性和方法
   - 继承
   - 多态
   - 魔术方法

### Day 6: 文件操作 (1个文件)

**目标**: 掌握文件读写和数据处理

**文件和JSON** (`05_file_io/01_files_and_json.py`)
   - 读写文本文件
   - JSON 处理
   - CSV 处理
   - 配置文件

### Day 7: 实战项目 (3个项目)

**目标**: 综合运用所学知识

1. **待办事项管理器** (`06_projects/01_todo_app.py`)
   - 综合练习：列表、字典、函数、文件操作
   - 功能：添加、删除、完成、持久化

2. **简易计算器** (`06_projects/02_calculator.py`)
   - 综合练习：函数、异常处理、类
   - 功能：基础运算、科学计算、历史记录

3. **小游戏** (`06_projects/03_simple_game.py`)
   - 综合练习：循环、条件判断、随机数
   - 功能：猜数字、井字棋

## PyCharm使用技巧

### 运行代码
1. 在PyCharm中打开项目文件夹
2. 右键点击文件 → Run 'filename'
3. 或者按 `Shift + F10`

### 调试技巧
- 设置断点：点击行号旁边
- 开始调试：`Shift + F9`
- 单步执行：`F8`

### 常用快捷键
| 快捷键 | 功能 |
|--------|------|
| `Ctrl+D` | 复制行 |
| `Ctrl+Y` | 删除行 |
| `Ctrl+Alt+L` | 格式化代码 |
| `Alt+Enter` | 快速修复 |
| `Shift+F10` | 运行 |
| `Ctrl+Shift+F10` | 运行当前文件 |

## 学习建议

1. **动手实践**: 每个知识点都要自己写代码验证
2. **逐步深入**: 先掌握基础，再学习高级特性
3. **调试技巧**: 学会使用 print() 查看变量值
4. **阅读代码**: 运行示例文件，观察输出结果
5. **做练习**: 每个文件末尾都有"你来试试"部分，务必完成
6. **做项目**: 完成基础后，尝试修改和扩展项目代码

## 学习顺序建议

1. 阅读本文档了解整体结构
2. 打开 `00_learning_path.md` 查看详细知识点
3. 从 `01_basics` 开始，逐个文件学习
4. 每个文件运行一次，观察输出
5. 完成"你来试试"部分的练习
6. 进阶到下一目录
7. 最后完成三个实战项目

## 遇到问题怎么办？

1. 检查代码缩进（Python对缩进敏感）
2. 仔细阅读错误信息
3. 使用 print() 调试
4. 查看示例代码
5. 官方文档: https://docs.python.org/

## 下一步

完成本教程后，你可以：
1. 学习更多Python标准库
2. 学习Web框架 (Flask/Django)
3. 学习数据分析 (Pandas/Numpy)
4. 学习机器学习
5. 参与开源项目

祝你学习愉快！🐍
