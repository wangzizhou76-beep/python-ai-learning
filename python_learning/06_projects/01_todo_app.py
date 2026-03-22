"""
项目1: 待办事项管理器
实战练习：综合运用Python基础、数据结构、文件操作
"""

import json
import os
import sys
from datetime import datetime

# Windows命令行编码设置
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

class TodoApp:
    """待办事项管理器"""

    def __init__(self, file_path="todos.json"):
        self.file_path = file_path
        # 确保文件路径存在
        import os
        os.makedirs(os.path.dirname(file_path) if os.path.dirname(file_path) else ".", exist_ok=True)
        self.todos = self.load_todos()

    def load_todos(self):
        """加载待办事项"""
        if os.path.exists(self.file_path):
            with open(self.file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        return []

    def save_todos(self):
        """保存待办事项"""
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(self.todos, f, ensure_ascii=False, indent=2)

    def add(self, title, description=""):
        """添加待办事项"""
        todo = {
            "id": len(self.todos) + 1,
            "title": title,
            "description": description,
            "completed": False,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.todos.append(todo)
        self.save_todos()
        return todo

    def complete(self, todo_id):
        """标记完成"""
        for todo in self.todos:
            if todo["id"] == todo_id:
                todo["completed"] = not todo["completed"]
                todo["completed_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.save_todos()
                return True
        return False

    def delete(self, todo_id):
        """删除待办事项"""
        for i, todo in enumerate(self.todos):
            if todo["id"] == todo_id:
                del self.todos[i]
                self.save_todos()
                return True
        return False

    def list_todos(self, status="all"):
        """列出待办事项"""
        filtered = self.todos
        if status == "completed":
            filtered = [t for t in self.todos if t["completed"]]
        elif status == "pending":
            filtered = [t for t in self.todos if not t["completed"]]

        if not filtered:
            print("暂无待办事项")
            return

        print(f"\n待办事项列表 ({status}):")
        print("=" * 60)
        for todo in filtered:
            status_mark = "[OK]" if todo["completed"] else "[  ]"
            print(f"{status_mark} [{todo['id']}] {todo['title']}")
            if todo["description"]:
                print(f"    描述: {todo['description']}")
            print(f"    创建时间: {todo['created_at']}")
            if todo.get("completed_at"):
                print(f"    完成时间: {todo['completed_at']}")
            print()

    def get_stats(self):
        """获取统计信息"""
        total = len(self.todos)
        completed = sum(1 for t in self.todos if t["completed"])
        pending = total - completed

        return {
            "total": total,
            "completed": completed,
            "pending": pending,
            "completion_rate": (completed / total * 100) if total > 0 else 0
        }

    def print_stats(self):
        """打印统计信息"""
        stats = self.get_stats()
        print("\n统计信息:")
        print("=" * 40)
        print(f"总计: {stats['total']} 项")
        print(f"已完成: {stats['completed']} 项")
        print(f"未完成: {stats['pending']} 项")
        print(f"完成率: {stats['completion_rate']:.1f}%")

    def interactive_mode(self):
        """交互式模式"""
        print("欢迎使用待办事项管理器！")
        print("命令: add/list/complete/delete/stats/quit")

        while True:
            command = input("\n> ").strip().lower()

            if command == "quit" or command == "q":
                print("再见！")
                break

            elif command == "list" or command == "l":
                status = input("筛选 (all/completed/pending): ").lower()
                self.list_todos(status)

            elif command == "add" or command == "a":
                title = input("标题: ")
                description = input("描述 (可选): ")
                todo = self.add(title, description)
                print(f"添加成功: {todo['title']}")

            elif command == "complete" or command == "c":
                todo_id = int(input("输入ID: "))
                if self.complete(todo_id):
                    print("状态已更新")
                else:
                    print("未找到该待办事项")

            elif command == "delete" or command == "d":
                todo_id = int(input("输入ID: "))
                if self.delete(todo_id):
                    print("删除成功")
                else:
                    print("未找到该待办事项")

            elif command == "stats" or command == "s":
                self.print_stats()

            elif command == "help" or command == "h":
                print("\n可用命令:")
                print("  add/a      - 添加待办事项")
                print("  list/l     - 列出待办事项")
                print("  complete/c - 切换完成状态")
                print("  delete/d   - 删除待办事项")
                print("  stats/s    - 显示统计信息")
                print("  quit/q     - 退出")

            else:
                print("未知命令，输入 help 查看帮助")


# 测试代码
if __name__ == "__main__":
    # 创建应用实例
    app = TodoApp("python_learning/06_projects/todos.json")

    # 添加一些示例数据
    if len(app.todos) == 0:
        app.add("学习Python基础", "完成所有基础练习")
        app.add("阅读《Python编程》", "前5章")
        app.add("完成小项目", "待办事项管理器")
        app.complete(1)  # 标记第一个为完成

    # 显示列表
    app.list_todos()

    # 显示统计
    app.print_stats()

    # 启动交互模式（取消注释以启用）
    app.interactive_mode()
