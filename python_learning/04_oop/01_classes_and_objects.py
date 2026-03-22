"""
Python面向对象编程 (OOP)
面向对象是Python的重要特性，让你能够创建可重用、可维护的代码
"""

# ============ 1. 类与对象基础 ============
print("=" * 40)
print("1. 类与对象基础")
print("=" * 40)

class Person:
    """人类"""

    def __init__(self, name, age):
        """初始化方法"""
        self.name = name
        self.age = age

    def introduce(self):
        """自我介绍"""
        return f"我是{self.name}，今年{self.age}岁"

    def have_birthday(self):
        """过生日"""
        self.age += 1
        print(f"生日快乐！{self.name}现在{self.age}岁了")

# 创建对象
person1 = Person("张三", 25)
person2 = Person("李四", 30)

print(person1.introduce())
print(person2.introduce())

person1.have_birthday()


# ============ 2. 类属性 vs 实例属性 ============
print("\n" + "=" * 40)
print("2. 类属性 vs 实例属性")
print("=" * 40)

class Dog:
    """狗类"""
    species = "犬科动物"  # 类属性 - 所有实例共享

    def __init__(self, name, breed):
        self.name = name  # 实例属性 - 每个实例独立
        self.breed = breed

dog1 = Dog("旺财", "金毛")
dog2 = Dog("小黑", "哈士奇")

print(f"{dog1.name}是{dog1.species}")
print(f"{dog2.name}是{dog2.species}")

# 类属性可以被修改（影响所有实例）
Dog.species = "汪星人"
print(f"修改后: {dog1.species}, {dog2.species}")


# ============ 3. 私有属性和封装 ============
print("\n" + "=" * 40)
print("3. 私有属性和封装")
print("=" * 40)

class BankAccount:
    """银行账户类"""

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # 私有属性（双下划线）

    def deposit(self, amount):
        """存款"""
        if amount > 0:
            self.__balance += amount
            print(f"存款¥{amount}成功，余额¥{self.__balance}")

    def withdraw(self, amount):
        """取款"""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"取款¥{amount}成功，余额¥{self.__balance}")
        else:
            print("取款失败：余额不足或金额无效")

    def get_balance(self):
        """查询余额"""
        return self.__balance

account = BankAccount("张三", 1000)
account.deposit(500)
account.withdraw(200)
print(f"当前余额: ¥{account.get_balance()}")


# ============ 4. 继承 ============
print("\n" + "=" * 40)
print("4. 继承")
print("=" * 40)

class Animal:
    """动物基类"""
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    """狗 - 继承自Animal"""
    def speak(self):
        return f"{self.name}说：汪汪汪！"

class Cat(Animal):
    """猫 - 继承自Animal"""
    def speak(self):
        return f"{self.name}说：喵喵喵！"

dog = Dog("旺财")
cat = Cat("咪咪")

print(dog.speak())
print(cat.speak())


# ============ 5. 多态 ============
print("\n" + "=" * 40)
print("5. 多态")
print("=" * 40)

class Shape:
    """形状基类"""
    def area(self):
        pass

class Rectangle(Shape):
    """矩形"""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    """圆形"""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * self.radius ** 2

shapes = [
    Rectangle(5, 4),
    Rectangle(3, 6),
    Circle(2),
    Circle(3)
]

print("各种形状的面积:")
for shape in shapes:
    print(f"  {shape.__class__.__name__}: {shape.area():.2f}")


# ============ 6. 类方法和静态方法 ============
print("\n" + "=" * 40)
print("6. 类方法和静态方法")
print("=" * 40)

class Student:
    """学生类"""
    school = "第一中学"
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1

    def introduce(self):
        """实例方法"""
        return f"我是{Student.school}的{self.name}"

    @classmethod
    def get_count(cls):
        """类方法"""
        return f"学校共有{cls.count}名学生"

    @staticmethod
    def is_valid_age(age):
        """静态方法"""
        return 6 <= age <= 18

print(f"{Student.get_count()}")
student1 = Student("张三")
student2 = Student("李四")
print(f"{Student.get_count()}")
print(f"15岁是否有效: {Student.is_valid_age(15)}")
print(f"20岁是否有效: {Student.is_valid_age(20)}")


# ============ 7. 魔术方法 ============
print("\n" + "=" * 40)
print("7. 魔术方法")
print("=" * 40)

class Point:
    """点类"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        """字符串表示"""
        return f"Point({self.x}, {self.y})"

    def __repr__(self):
        """开发者表示"""
        return f"Point({self.x}, {self.y})"

    def __add__(self, other):
        """加法运算"""
        return Point(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        """相等比较"""
        return self.x == other.x and self.y == other.y

p1 = Point(3, 4)
p2 = Point(5, 6)
p3 = p1 + p2

print(f"p1: {p1}")
print(f"p2: {p2}")
print(f"p1 + p2: {p3}")
print(f"p1 == p2: {p1 == Point(3, 4)}")


# ============ 8. 综合练习 ============
print("\n" + "=" * 40)
print("综合练习：简单的图书管理系统")
print("=" * 40)

class Book:
    """书籍类"""
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
        self.is_borrowed = False

    def borrow(self):
        """借书"""
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False

    def return_book(self):
        """还书"""
        self.is_borrowed = False

    def __str__(self):
        status = "已借出" if self.is_borrowed else "可借"
        return f"《{self.title}》-{self.author}-¥{self.price}-[{status}]"

class Library:
    """图书馆类"""
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        """添加书籍"""
        self.books.append(book)

    def find_book(self, title):
        """查找书籍"""
        for book in self.books:
            if book.title == title:
                return book
        return None

    def borrow_book(self, title):
        """借书"""
        book = self.find_book(title)
        if book and book.borrow():
            print(f"成功借出: {book.title}")
        else:
            print(f"借书失败: {title}")

    def list_books(self):
        """列出所有书籍"""
        print(f"\n{self.name}藏书:")
        for book in self.books:
            print(f"  {book}")

# 使用示例
library = Library("社区图书馆")
library.add_book(Book("Python编程", "张三", 59))
library.add_book(Book("算法导论", "李四", 89))
library.add_book(Book("设计模式", "王五", 69))

library.list_books()
library.borrow_book("Python编程")
library.borrow_book("算法导论")
library.borrow_book("Python编程")  # 再次借阅
library.list_books()


# ============ 你来试试 ============
print("\n" + "=" * 40)
print("你来试试")
print("=" * 40)

# 练习：实现一个简单的计算器类
# 1. 支持加减乘除运算
# 2. 支持链式调用
# 3. 支持撤销操作
# 4. 实现 __str__ 方法显示当前结果

# 在这里写你的代码...
