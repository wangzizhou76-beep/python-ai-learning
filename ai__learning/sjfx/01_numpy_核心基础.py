"""
═══════════════════════════════════════════════════════════════
  NumPy 核心基础 — 第一课
  目标：掌握数组创建、索引、运算、广播、线代
  建议学习时间：3-4 天，每天边看边动手敲代码
═══════════════════════════════════════════════════════════════
"""

import numpy as np

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 第 1 节：为什么需要 NumPy？
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
print("=" * 60)
print("第 1 节：NumPy vs 原生 Python 的速度差异")
print("=" * 60)

import time

# 用原生 Python 做 100万次加法
py_list = list(range(1_000_000))
start = time.time()
result = [x * 2 for x in py_list]
python_time = time.time() - start

# 用 NumPy 做同样的事
np_array = np.arange(1_000_000)
start = time.time()
result = np_array * 2
numpy_time = time.time() - start

print(f"Python 列表耗时: {python_time:.4f} 秒")
print(f"NumPy 数组耗时:  {numpy_time:.4f} 秒")
print(f"NumPy 快了约:    {python_time / numpy_time:.0f} 倍")
print()
# 核心原因：NumPy 底层是 C 语言，向量化运算避免了 Python 的循环开销
# 作为通信工程背景，你可以理解为：NumPy 就是 MATLAB 矩阵运算的 Python 版本


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 第 2 节：数组创建 — 最常用的 10 种方式
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
print("=" * 60)
print("第 2 节：数组创建")
print("=" * 60)

# 2.1 从列表/嵌套列表创建
a1 = np.array([1, 2, 3, 4, 5])               # 一维数组
a2 = np.array([[1, 2, 3], [4, 5, 6]])         # 二维数组（矩阵）
a3 = np.array([[[1,2],[3,4]], [[5,6],[7,8]]]) # 三维数组
print("一维:", a1)
print("二维:\n", a2)
print("三维形状:", a3.shape)  # (2, 2, 2)

# 2.2 特殊数组（AI 中超常用）
zeros = np.zeros((3, 4))          # 全 0 矩阵，初始化权重常用
ones  = np.ones((2, 3))           # 全 1 矩阵
eye   = np.eye(4)                 # 单位矩阵（线代里的 I）
full  = np.full((3, 3), 7)        # 全部填充为 7
rand  = np.random.rand(3, 3)      # 0~1 均匀随机数
randn = np.random.randn(3, 3)     # 标准正态随机数（均值0方差1）
print("\n单位矩阵:\n", eye)
print("正态随机数:\n", np.round(randn, 2))

# 2.3 等差/等比序列（信号处理必用）
linspace = np.linspace(0, 2*np.pi, 100)  # 0到2π之间取100个均匀点
arange   = np.arange(0, 10, 0.5)         # 从0开始步长0.5到10
logspace = np.logspace(0, 3, 4)          # 10^0 到 10^3 的等比序列
print("\nlinspace 前5个值:", linspace[:5])
print("logspace:", logspace)  # [1, 10, 100, 1000]

# 重要属性
print("\n--- 数组重要属性 ---")
m = np.random.randn(4, 5)
print(f"形状 shape:    {m.shape}")    # (4, 5)
print(f"维度 ndim:     {m.ndim}")     # 2
print(f"元素数 size:   {m.size}")     # 20
print(f"数据类型 dtype:{m.dtype}")    # float64
print(f"字节数 nbytes: {m.nbytes}")   # 160 (20个float64 × 8字节)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 第 3 节：数据类型 — 一个容易踩的坑
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
print("\n" + "=" * 60)
print("第 3 节：数据类型 dtype")
print("=" * 60)

# 常见类型
int_arr   = np.array([1, 2, 3], dtype=np.int32)    # 整数
float_arr = np.array([1, 2, 3], dtype=np.float64)  # 浮点（默认）
bool_arr  = np.array([1, 0, 1], dtype=bool)        # 布尔
cmplx_arr = np.array([1+2j, 3+4j], dtype=complex)  # 复数（通信场景！）
print("复数数组:", cmplx_arr)
print("实部:", cmplx_arr.real, "虚部:", cmplx_arr.imag)

# 类型转换
a = np.array([1.7, 2.9, 3.1])
print("\n原始 float:", a)
print("转为 int:", a.astype(int))   # 注意：直接截断，不四舍五入！

# 坑：整数除法
a = np.array([1, 2, 3], dtype=np.int32)
print("\n整数数组 / 2:", a / 2)     # 结果是 float，NumPy 会自动升级
print("整数数组 // 2:", a // 2)    # 地板除，结果是整数


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 第 4 节：索引与切片 — 最核心的操作
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
print("\n" + "=" * 60)
print("第 4 节：索引与切片")
print("=" * 60)

# 4.1 一维数组索引（和 Python list 完全一样）
a = np.array([10, 20, 30, 40, 50, 60, 70, 80])
print("原数组:", a)
print("a[2]:", a[2])         # 30（正向索引）
print("a[-1]:", a[-1])       # 80（反向索引）
print("a[2:5]:", a[2:5])     # [30 40 50]（切片，左闭右开）
print("a[::2]:", a[::2])     # [10 30 50 70]（步长为2）
print("a[::-1]:", a[::-1])   # 反转数组

# ⚠️ 重要：NumPy 切片是视图，不是拷贝！
b = a[2:5]
b[0] = 999          # 修改 b 会影响 a！
print("修改切片后 a:", a)     # a[2] 变成了 999

# 如果不想影响原数组，用 .copy()
c = a[2:5].copy()
c[0] = 0
print("使用copy后 a不变:", a)

# 4.2 二维数组索引（矩阵操作，AI 最常用）
M = np.array([[1,  2,  3,  4],
              [5,  6,  7,  8],
              [9,  10, 11, 12]])
print("\n矩阵 M:\n", M)
print("M[1,2]:", M[1,2])          # 第2行第3列 = 7
print("M[0,:]:", M[0,:])          # 第1行所有列 [1 2 3 4]
print("M[:,2]:", M[:,2])          # 所有行第3列 [3 7 11]
print("M[1:,1:3]:\n", M[1:,1:3]) # 子矩阵（AI中经常用到）

# 4.3 花式索引（整数数组作为索引）
a = np.array([10, 20, 30, 40, 50])
idx = np.array([0, 2, 4])
print("\n花式索引 a[[0,2,4]]:", a[idx])  # [10 30 50]

# 多维花式索引
M = np.arange(16).reshape(4, 4)
rows = np.array([0, 1, 2])
cols = np.array([1, 2, 3])
print("矩阵对角线元素:", M[rows, cols])  # M[0,1], M[1,2], M[2,3]

# 4.4 布尔索引（条件过滤，超常用！）
a = np.array([15, 3, 28, 7, 42, 1, 19])
mask = a > 10
print("\n大于10的掩码:", mask)
print("大于10的元素:", a[mask])          # [15 28 42 19]
print("简写方式:", a[a > 10])            # 等价写法

# 多条件组合
print("10<x<30:", a[(a > 10) & (a < 30)])  # 注意用 & 不用 and！

# 实际应用：批量修改满足条件的元素
a[a > 20] = 0
print("大于20的置零后:", a)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 第 5 节：数组运算 — 向量化是核心思想
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
print("\n" + "=" * 60)
print("第 5 节：数组运算")
print("=" * 60)

a = np.array([1.0, 2.0, 3.0, 4.0])
b = np.array([10.0, 20.0, 30.0, 40.0])

# 5.1 基础四则运算（元素级别）
print("a + b:", a + b)
print("a * b:", a * b)
print("a ** 2:", a ** 2)    # 幂运算
print("b / a:", b / a)

# 5.2 通用函数 ufunc（对每个元素作用）
print("\nnp.sqrt(a):", np.sqrt(a))
print("np.exp(a):", np.round(np.exp(a), 2))
print("np.log(b):", np.round(np.log(b), 2))
print("np.sin(a):", np.round(np.sin(a), 2))
print("np.abs([-1,-2,3]):", np.abs([-1,-2,3]))

# 5.3 聚合运算（沿轴方向）
M = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
print("\n矩阵 M:\n", M)
print("全局求和:", np.sum(M))        # 45
print("按行求和(axis=1):", np.sum(M, axis=1))  # [6, 15, 24]
print("按列求均值(axis=0):", np.mean(M, axis=0))  # [4, 5, 6]
print("全局最大值:", np.max(M))
print("全局最大值位置:", np.argmax(M))  # 返回扁平索引
print("按列排序:\n", np.sort(M, axis=0))

# 5.4 比较运算
a = np.array([3, 1, 4, 1, 5, 9, 2, 6])
print("\n大于3的数量:", np.sum(a > 3))
print("所有元素都大于0?", np.all(a > 0))
print("有元素大于8?", np.any(a > 8))


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 第 6 节：广播机制 — NumPy 最神奇的特性
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
print("\n" + "=" * 60)
print("第 6 节：广播机制 Broadcasting")
print("=" * 60)

"""
广播规则（记住这3条）：
1. 如果两个数组维度数不同，在维度少的数组左边补1
2. 如果某个维度是1，自动扩展以匹配另一个数组的该维度
3. 如果维度不兼容且都不是1，报错

直觉理解：矩阵加一个向量，向量自动"复制"到每一行/列
"""

# 案例1：标量与数组运算（最简单的广播）
a = np.array([[1, 2, 3],
              [4, 5, 6]])
print("矩阵 a:\n", a)
print("a * 10:\n", a * 10)  # 10 广播到每个元素

# 案例2：(3,) 向量与 (2,3) 矩阵
row_vec = np.array([10, 20, 30])
print("\na + row_vec:\n", a + row_vec)  # 向量广播到每一行

# 案例3：列向量 (2,1) 与矩阵 (2,3)
col_vec = np.array([[100],
                    [200]])
print("a + col_vec:\n", a + col_vec)  # 列向量广播到每一列

# 案例4：行向量 + 列向量 = 矩阵（经典应用）
rows = np.array([[0], [1], [2], [3]])  # shape (4,1)
cols = np.array([0, 10, 20, 30])       # shape (4,)
result = rows + cols                    # shape (4,4)
print("\n行向量+列向量外积:\n", result)

# 实际应用：特征归一化（AI预处理必用）
data = np.array([[1.0, 200.0, 0.5],
                 [2.0, 150.0, 0.8],
                 [3.0, 300.0, 0.3]])
mean = data.mean(axis=0)    # 每列均值，shape (3,)
std  = data.std(axis=0)     # 每列标准差，shape (3,)
normalized = (data - mean) / std  # 广播：mean/std 自动匹配每一行
print("\n原始数据:\n", data)
print("归一化后:\n", np.round(normalized, 3))


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 第 7 节：形状操作 — reshape/stack/split
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
print("\n" + "=" * 60)
print("第 7 节：形状操作")
print("=" * 60)

# reshape（-1 让 NumPy 自动计算该维度）
a = np.arange(24)
b = a.reshape(4, 6)      # 4行6列
c = a.reshape(2, 3, 4)   # 三维张量
d = a.reshape(6, -1)     # -1 自动计算，结果是 (6,4)
print("原始:", a.shape)
print("reshape(4,6):", b.shape)
print("reshape(2,3,4):", c.shape)
print("reshape(6,-1):", d.shape)

# flatten / ravel（压平成一维）
m = np.array([[1,2,3],[4,5,6]])
print("flatten:", m.flatten())   # 返回副本
print("ravel:", m.ravel())       # 返回视图（更快）

# 转置
print("转置前:", m.shape, "\n转置后:", m.T.shape)
print("m.T:\n", m.T)

# 拼接
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
print("\n垂直拼接(vstack):\n", np.vstack([a, b]))   # 上下拼
print("水平拼接(hstack):\n", np.hstack([a, b]))     # 左右拼
print("沿轴0拼接:\n", np.concatenate([a, b], axis=0))

# 新增维度（AI 中超常用，给批次数据加维度）
vec = np.array([1, 2, 3])
print("\n原始 shape:", vec.shape)              # (3,)
print("np.newaxis 后:", vec[np.newaxis,:].shape)  # (1,3)
print("expand_dims 后:", np.expand_dims(vec, axis=0).shape)  # (1,3)

# 分割
a = np.arange(12).reshape(3, 4)
parts = np.split(a, 2, axis=1)   # 沿列方向分成2份
print("\n分割结果:")
for i, p in enumerate(parts):
    print(f"  部分{i}: shape={p.shape}\n{p}")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 第 8 节：线性代数 — 通信背景的你最熟悉这里
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
print("\n" + "=" * 60)
print("第 8 节：线性代数")
print("=" * 60)

A = np.array([[2.0, 1.0],
              [5.0, 3.0]])
B = np.array([[1.0, 2.0],
              [0.0, 1.0]])

# 矩阵乘法（注意：不是 A*B，那是元素乘法）
print("矩阵乘法 A @ B:\n", A @ B)         # @ 运算符（推荐）
print("矩阵乘法 np.dot:\n", np.dot(A, B)) # 等价写法

# 常用矩阵运算
print("\n矩阵行列式:", np.linalg.det(A))
print("矩阵的逆:\n", np.linalg.inv(A))
print("矩阵的迹（对角线和）:", np.trace(A))
print("矩阵的秩:", np.linalg.matrix_rank(A))

# 特征值与特征向量（通信里经常用，波束成形等）
eigenvalues, eigenvectors = np.linalg.eig(A)
print("\n特征值:", eigenvalues)
print("特征向量（列）:\n", eigenvectors)

# 奇异值分解 SVD（信号处理中降维利器）
U, S, Vt = np.linalg.svd(A)
print("\nSVD 分解:")
print("U:\n", U)
print("奇异值 S:", S)
print("Vt:\n", Vt)
print("验证重建:", np.allclose(A, U @ np.diag(S) @ Vt))

# 解线性方程组 Ax = b
b_vec = np.array([4.0, 11.0])
x = np.linalg.solve(A, b_vec)
print("\n解方程 Ax=b, x =", x)
print("验证 Ax =", A @ x)  # 应该等于 b

# 向量范数
v = np.array([3.0, 4.0])
print("\n向量 [3,4] 的 L2 范数:", np.linalg.norm(v))  # 5.0（勾股定理）
print("L1 范数:", np.linalg.norm(v, ord=1))            # 7.0
print("无穷范数:", np.linalg.norm(v, ord=np.inf))      # 4.0


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 第 9 节：随机数与概率 — AI 训练的基础
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
print("\n" + "=" * 60)
print("第 9 节：随机数")
print("=" * 60)

# 设置随机种子（实验可复现的关键！）
np.random.seed(42)

# 各种分布
uniform  = np.random.rand(5)              # 均匀分布 [0,1)
normal   = np.random.randn(5)             # 标准正态 N(0,1)
normal2  = np.random.normal(5, 2, size=5) # 指定均值5、标准差2
binomial = np.random.binomial(10, 0.3, 5) # 二项分布
poisson  = np.random.poisson(3, 5)        # 泊松分布
integers = np.random.randint(0, 100, 5)   # 整数随机

print("均匀分布:", np.round(uniform, 3))
print("正态分布:", np.round(normal, 3))
print("自定义正态:", np.round(normal2, 3))
print("随机整数:", integers)

# 打乱和采样
arr = np.arange(10)
np.random.shuffle(arr)          # 原地打乱
print("打乱后:", arr)

sample = np.random.choice(np.arange(100), size=5, replace=False)
print("无放回抽样5个:", sample)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 第 10 节：通信场景实战练习
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
print("\n" + "=" * 60)
print("第 10 节：实战练习 — 信号处理场景")
print("=" * 60)

# 练习1：模拟 AWGN 信道
t = np.linspace(0, 1, 1000)        # 时间轴，0到1秒，1000个采样点
freq = 5                             # 信号频率 5Hz
signal = np.sin(2 * np.pi * freq * t)  # 正弦信号

snr_db = 10                          # 信噪比 10dB
noise_power = 10 ** (-snr_db / 10)  # 噪声功率
noise = np.random.normal(0, np.sqrt(noise_power), len(t))
received = signal + noise            # 接收信号

print(f"发送信号功率: {np.mean(signal**2):.4f}")
print(f"接收信号 SNR: {10*np.log10(np.mean(signal**2)/np.mean(noise**2)):.2f} dB")

# 练习2：计算相关矩阵
data = np.random.randn(100, 4)      # 100个样本，4个特征
corr_matrix = np.corrcoef(data.T)   # 特征相关矩阵
print("\n特征相关矩阵:\n", np.round(corr_matrix, 2))

# 练习3：矩阵快速幂（信道矩阵计算）
H = np.random.randn(4, 4) + 1j * np.random.randn(4, 4)  # 复数信道矩阵
HH_H = H @ H.conj().T  # H × H 的共轭转置（MIMO信道容量计算基础）
print("\nH×H^H 形状:", HH_H.shape)
print("是否为厄米特矩阵:", np.allclose(HH_H, HH_H.conj().T))


print("\n" + "=" * 60)
print("🏋️  课后练习题（自己完成，答案在 01_numpy_答案.py）")
print("=" * 60)
print("""
1. 创建一个 5×5 的矩阵，主对角线为 [1,2,3,4,5]，其余为0
   提示：np.diag()

2. 给定数组 a = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
   - 找出所有唯一值（去重）
   - 找出每个元素出现的次数
   - 找出第3大的数
   提示：np.unique(), np.argsort()

3. 用 NumPy 实现两个向量的余弦相似度
   a = [1, 2, 3], b = [4, 5, 6]
   公式：cos(a,b) = (a·b) / (|a| × |b|)
   提示：np.dot(), np.linalg.norm()

4. 生成 10×10 的随机矩阵，将大于0的值替换为1，小于等于0的替换为-1
   （这就是符号函数，通信里常用）
   提示：np.where()

5. 实现简单的线性回归：给定 X=[1,2,3,4,5], y=[2,4,5,4,5]
   用最小二乘法求 w, b，使 y ≈ w*X + b
   提示：np.linalg.lstsq()
""")
