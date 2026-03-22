"""
项目2: 简易计算器
实战练习：函数、条件判断、循环、异常处理
"""

class Calculator:
    """简易计算器"""

    def add(self, a, b):
        """加法"""
        return a + b

    def subtract(self, a, b):
        """减法"""
        return a - b

    def multiply(self, a, b):
        """乘法"""
        return a * b

    def divide(self, a, b):
        """除法"""
        if b == 0:
            raise ValueError("除数不能为零")
        return a / b

    def power(self, a, b):
        """幂运算"""
        return a ** b

    def sqrt(self, a):
        """开平方"""
        if a < 0:
            raise ValueError("不能对负数开平方")
        return a ** 0.5

    def percentage(self, a, b):
        """计算百分比: a是b的百分之几"""
        if b == 0:
            raise ValueError("除数不能为零")
        return (a / b) * 100

    def clear_history(self):
        """清空历史记录"""
        self.history = []
        return self.history

    def get_history(self):
        """获取历史记录"""
        return self.history


class ScientificCalculator(Calculator):
    """科学计算器 - 继承自基础计算器"""

    def __init__(self):
        self.history = []

    def log(self, a, base=10):
        """对数"""
        import math
        if a <= 0 or base <= 0 or base == 1:
            raise ValueError("对数参数无效")
        return math.log(a, base)

    def ln(self, a):
        """自然对数"""
        import math
        if a <= 0:
            raise ValueError("对数参数无效")
        return math.log(a)

    def sin(self, a):
        """正弦 (角度)"""
        import math
        return math.sin(math.radians(a))

    def cos(self, a):
        """余弦 (角度)"""
        import math
        return math.cos(math.radians(a))

    def tan(self, a):
        """正切 (角度)"""
        import math
        return math.tan(math.radians(a))

    def factorial(self, n):
        """阶乘"""
        if n < 0:
            raise ValueError("不能计算负数的阶乘")
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

    def _add_to_history(self, operation, result):
        """添加到历史记录"""
        self.history.append({
            "operation": operation,
            "result": result,
            "time": self._get_current_time()
        })

    def _get_current_time(self):
        """获取当前时间"""
        from datetime import datetime
        return datetime.now().strftime("%H:%M:%S")

    def calculate(self, operation, a, b=None):
        """执行计算并记录历史"""
        operations = {
            "+": lambda: self.add(a, b),
            "-": lambda: self.subtract(a, b),
            "*": lambda: self.multiply(a, b),
            "/": lambda: self.divide(a, b),
            "^": lambda: self.power(a, b),
            "%": lambda: self.percentage(a, b),
            "sqrt": lambda: self.sqrt(a),
            "sin": lambda: self.sin(a),
            "cos": lambda: self.cos(a),
            "tan": lambda: self.tan(a),
            "log": lambda: self.log(a, b) if b else self.ln(a),
            "factorial": lambda: self.factorial(int(a)),
        }

        if operation not in operations:
            raise ValueError(f"未知操作: {operation}")

        try:
            result = operations[operation]()
            op_str = f"{a} {operation}" + (f" {b}" if b is not None else "")
            self._add_to_history(op_str, result)
            return result
        except Exception as e:
            raise ValueError(f"计算错误: {e}")

    def print_history(self):
        """打印历史记录"""
        if not self.history:
            print("暂无历史记录")
            return

        print("\n历史记录:")
        print("=" * 50)
        for i, record in enumerate(self.history, 1):
            print(f"{i}. [{record['time']}] {record['operation']} = {record['result']}")


def display_menu():
    """显示菜单"""
    print("\n" + "=" * 50)
    print("简易计算器")
    print("=" * 50)
    print("基础运算:")
    print("  +  加法          /  除法")
    print("  -  减法          ^  幂运算")
    print("  *  乘法          %  百分比")
    print("\n科学运算:")
    print("  sqrt   开平方    sin   正弦 (角度)")
    print("  log    对数      cos   余弦 (角度)")
    print("  factorial 阶乘   tan   正切 (角度)")
    print("\n其他:")
    print("  h      历史记录    q     退出")
    print("=" * 50)


def get_input(prompt):
    """获取用户输入"""
    try:
        value = input(prompt)
        if value.lower() in ['q', 'quit']:
            return None
        return float(value)
    except ValueError:
        print("请输入有效的数字")
        return None


def interactive_calculator():
    """交互式计算器"""
    calc = ScientificCalculator()

    print("欢迎使用计算器！输入 q 退出")

    while True:
        display_menu()
        operation = input("\n选择运算: ").strip().lower()

        if operation in ['q', 'quit']:
            print("再见！")
            break

        if operation == 'h':
            calc.print_history()
            continue

        # 获取第一个数字
        a = get_input("第一个数字: ")
        if a is None:
            continue

        # 获取第二个数字（如果需要）
        b = None
        if operation not in ['sqrt', 'sin', 'cos', 'tan', 'factorial']:
            b = get_input("第二个数字: ")
            if b is None:
                continue

        # 执行计算
        try:
            result = calc.calculate(operation, a, b)
            print(f"\n结果: {result}")
        except ValueError as e:
            print(f"错误: {e}")


# 测试代码
if __name__ == "__main__":
    # 基础计算器测试
    print("基础计算器测试:")
    print("=" * 40)
    calc = Calculator()
    print(f"5 + 3 = {calc.add(5, 3)}")
    print(f"10 - 4 = {calc.subtract(10, 4)}")
    print(f"6 * 7 = {calc.multiply(6, 7)}")
    print(f"15 / 3 = {calc.divide(15, 3)}")
    print(f"2 ^ 8 = {calc.power(2, 8)}")
    print(f"√16 = {calc.sqrt(16)}")

    # 科学计算器测试
    print("\n科学计算器测试:")
    print("=" * 40)
    scalc = ScientificCalculator()
    print(f"sin(30°) = {scalc.sin(30)}")
    print(f"cos(60°) = {scalc.cos(60)}")
    print(f"tan(45°) = {scalc.tan(45)}")
    print(f"log100(10) = {scalc.log(100, 10)}")
    print(f"ln(e) = {scalc.ln(2.71828):.4f}")
    print(f"5! = {scalc.factorial(5)}")

    # 启动交互模式（取消注释以启用）
    interactive_calculator()
