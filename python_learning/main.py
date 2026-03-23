from fastapi import FastAPI

# ==========================================
# 1. 这里原封不动粘贴你之前的核心业务代码
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None
# ==========================================

# 2. 初始化你的图书馆和书籍（存在内存中）
my_library = Library("社区线上图书馆")
my_library.add_book(Book("Python编程", "张三", 59))
my_library.add_book(Book("算法导论", "李四", 89))

# 3. 施展 FastAPI 魔法：创建一个 Web 实例
app = FastAPI()
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # 导入跨域模块

app = FastAPI()

# ===== 新增：配置跨域通行证 =====
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有网页调用（本地测试用，上线时要改成具体的网址）
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有请求方式 (GET, POST 等)
    allow_headers=["*"],
)
# ===============================

# 下面是你之前写的 Book, Library 类以及 @app.get 等接口代码，保持不变...
# 4. 配置接口（API）
@app.get("/books")
def list_all_books():
    """查看所有书籍的接口"""
    # 将面向对象的对象转换为字典，因为网页传输通用 JSON 格式
    return [{"书名": b.title, "作者": b.author, "已借出": b.is_borrowed} for b in my_library.books]

@app.post("/borrow/{book_title}")
def borrow_book_api(book_title: str):
    """借书的接口"""
    book = my_library.find_book(book_title)
    if book and book.borrow():
        return {"状态": "成功", "信息": f"你已成功借阅《{book_title}》"}
    else:
        return {"状态": "失败", "信息": f"《{book_title}》不存在或已被借走"}