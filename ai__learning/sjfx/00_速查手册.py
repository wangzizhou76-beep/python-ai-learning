"""
═══════════════════════════════════════════════════════════════
  NumPy / Pandas / Matplotlib 速查手册
  建议打印出来放在手边，随时查阅
═══════════════════════════════════════════════════════════════
"""

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# NumPy 速查
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
import numpy as np

── 创建数组 ──────────────────────────────────────────────────
np.array([1,2,3])               # 从列表创建
np.zeros((m, n))                # 全零矩阵
np.ones((m, n))                 # 全一矩阵
np.eye(n)                       # 单位矩阵
np.arange(start, stop, step)    # 等差序列（整数友好）
np.linspace(start, stop, num)   # 均匀取 num 个点
np.random.randn(m, n)           # 标准正态随机数
np.random.randint(low, high, n) # 随机整数
np.random.seed(42)              # 设随机种子

── 属性 ──────────────────────────────────────────────────────
a.shape   a.ndim   a.size   a.dtype   a.T

── 索引与切片 ────────────────────────────────────────────────
a[i]         a[-1]           a[i:j]        a[::2]
a[i, j]      a[i, :]         a[:, j]       a[i:j, k:l]
a[a > 0]     a[[0,2,4]]      np.where(cond, x, y)

── 形状操作 ──────────────────────────────────────────────────
a.reshape(m, n)   a.reshape(-1, n)   a.flatten()   a.ravel()
np.vstack([a,b])  np.hstack([a,b])   np.concatenate([a,b], axis=0)
np.newaxis        np.expand_dims(a, 0)   a.squeeze()
np.split(a, n)    np.split(a, n, axis=1)

── 运算 ──────────────────────────────────────────────────────
a + b   a - b   a * b   a / b   a ** 2   a @ b  # @是矩阵乘法
np.sum(a)         np.sum(a, axis=0)   np.sum(a, axis=1)
np.mean   np.std   np.max   np.min   np.argmax   np.argmin
np.sort(a)   np.argsort(a)   np.unique(a)
np.sqrt   np.exp   np.log   np.abs   np.sin   np.cos

── 线性代数 ──────────────────────────────────────────────────
np.dot(A, B)   A @ B            # 矩阵乘法
np.linalg.inv(A)                # 逆矩阵
np.linalg.det(A)                # 行列式
np.linalg.eig(A)                # 特征值/特征向量
np.linalg.svd(A)                # SVD分解
np.linalg.solve(A, b)           # 解方程 Ax=b
np.linalg.norm(v)               # 向量范数
"""

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Pandas 速查
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
import pandas as pd

── 创建 ──────────────────────────────────────────────────────
pd.Series([1,2,3], index=['a','b','c'])
pd.DataFrame({'A': [1,2], 'B': [3,4]})
pd.DataFrame(np.array([[1,2],[3,4]]), columns=['x','y'])

── 读取文件 ──────────────────────────────────────────────────
pd.read_csv('file.csv', sep=',', encoding='utf-8', nrows=100)
pd.read_excel('file.xlsx', sheet_name='Sheet1')
df.to_csv('out.csv', index=False, encoding='utf-8-sig')
df.to_excel('out.xlsx', index=False)

── 查看数据 ──────────────────────────────────────────────────
df.head(n)   df.tail(n)   df.sample(n)
df.shape     df.dtypes    df.columns    df.index
df.info()    df.describe()
df.value_counts()   df['col'].value_counts()

── 选取数据 ──────────────────────────────────────────────────
df['col']                       # 单列 → Series
df[['col1','col2']]             # 多列 → DataFrame
df.loc['行标签', '列名']        # 标签索引（两端含）
df.iloc[0, 1]                   # 位置索引（行,列）
df.loc['r1':'r3', 'A':'C']      # 标签切片
df.iloc[0:3, 0:2]               # 位置切片
df[df['col'] > 0]               # 布尔过滤
df.query("col > 0 and city=='北京'")

── 修改数据 ──────────────────────────────────────────────────
df['new_col'] = ...             # 添加新列
df.drop(columns=['col'])        # 删列
df.drop(index=[0,1])            # 删行
df.rename(columns={'old':'new'})
df.reset_index(drop=True)       # 重置索引
df.set_index('col')             # 设置索引

── 缺失值 ────────────────────────────────────────────────────
df.isnull()   df.isnull().sum()
df.dropna()   df.dropna(subset=['col'])
df.fillna(value)   df['col'].fillna(df['col'].mean())

── 数据清洗 ──────────────────────────────────────────────────
df.duplicated()   df.drop_duplicates()
df['col'].astype(int)
df['col'].str.strip()   .str.lower()   .str.contains('x')
pd.to_datetime(df['date'])
pd.cut(df['col'], bins=[0,10,20], labels=['低','高'])

── 运算与变换 ────────────────────────────────────────────────
df.apply(func, axis=0/1)        # 对列或行
df['col'].apply(lambda x: ...)  # 对元素
df.applymap(func)               # 对每个元素（弃用→改用.map）
df['col'].map({'a':1, 'b':2})  # 值映射

── 聚合 ──────────────────────────────────────────────────────
df.groupby('col').agg({'A':'sum', 'B':'mean'})
df.groupby(['c1','c2']).agg(新名=('col','sum'))
df.groupby('col').transform('mean')    # 保留原行数
df.pivot_table(values, index, columns, aggfunc)
pd.crosstab(df['A'], df['B'])

── 合并 ──────────────────────────────────────────────────────
pd.merge(df1, df2, on='key', how='inner/left/right/outer')
pd.concat([df1, df2], axis=0, ignore_index=True)   # 纵向
pd.concat([df1, df2], axis=1)                       # 横向

── 排序 ──────────────────────────────────────────────────────
df.sort_values('col', ascending=False)
df.sort_values(['c1','c2'], ascending=[True, False])
df['col'].rank(method='min')
df.nlargest(n, 'col')   df.nsmallest(n, 'col')
"""

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Matplotlib 速查
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
import matplotlib.pyplot as plt

── 基础模板 ──────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(x, y, color='steelblue', linewidth=2, label='标签',
        linestyle='--', marker='o', markersize=5, alpha=0.8)
ax.set_title('标题', fontsize=14)
ax.set_xlabel('x轴')   ax.set_ylabel('y轴')
ax.legend()            ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('图.png', dpi=150, bbox_inches='tight')
plt.close()   # 或 plt.show()

── 常用图表 ──────────────────────────────────────────────────
ax.plot(x, y)                         # 折线图
ax.scatter(x, y, c=colors, s=sizes)  # 散点图
ax.bar(x, height)                     # 垂直柱状图
ax.barh(y, width)                     # 水平柱状图
ax.hist(data, bins=30)                # 直方图
ax.boxplot(data)                      # 箱线图
ax.pie(sizes, labels=..., autopct='%1.1f%%')  # 饼图
ax.imshow(matrix, cmap='RdBu_r')     # 热力图
ax.fill_between(x, y1, y2, alpha=0.2)  # 填充区域

── 多子图 ────────────────────────────────────────────────────
fig, axes = plt.subplots(2, 3, figsize=(16,8))   # 2行3列
fig, axes = plt.subplots(1, 2, figsize=(12,5))
ax = axes[0]    # 访问第一个子图

# GridSpec 自定义布局
gs = fig.add_gridspec(3, 3)
ax1 = fig.add_subplot(gs[0, :2])   # 第0行，跨前两列
ax2 = fig.add_subplot(gs[0, 2])

── 装饰 ──────────────────────────────────────────────────────
ax.axhline(y=0.5, color='red', linestyle='--')   # 水平参考线
ax.axvline(x=10, color='gray')                    # 垂直参考线
ax.annotate('注释', xy=(x,y), xytext=(x2,y2),
            arrowprops=dict(arrowstyle='->'))
ax.text(x, y, '文字', fontsize=10, ha='center')
ax.set_xlim(0, 10)   ax.set_ylim(-1, 1)
ax.set_xticks([0,2,4,6])   ax.set_xticklabels(['a','b','c','d'])
plt.colorbar(im, ax=ax)
ax.spines['top'].set_visible(False)

── 样式 ──────────────────────────────────────────────────────
plt.style.use('seaborn-v0_8-whitegrid')   # 风格切换
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['figure.dpi'] = 100

常用颜色：'steelblue' 'tomato' 'green' 'orange' 'purple' 'gray'
          '#2E86AB' '#E84855' '#3BB273'（自定义hex）
色图(cmap)：'RdBu_r' 'Blues' 'YlOrRd' 'viridis' 'tab10'
线型：'-' '--' '-.' ':'
标记：'o' 's' '^' 'D' '*' '+'
"""

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 学习路线检查清单
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
checklist = """
═══════════════════════════════════════════════
  第一阶段学习检查清单
═══════════════════════════════════════════════

NumPy（目标：1-2周）
  [ ] 能创建各种形状的数组
  [ ] 熟练使用布尔索引过滤数据
  [ ] 理解广播机制并能应用
  [ ] 能做基本的矩阵运算（@、inv、eig）
  [ ] 刷完文末5道练习题

Pandas（目标：2-3周）
  [ ] 能从CSV创建DataFrame并查看基本信息
  [ ] 区分 loc 和 iloc 的用法
  [ ] 能处理缺失值（dropna、fillna）
  [ ] 能做 groupby 聚合分析
  [ ] 能做两表 merge
  [ ] 用真实数据集做一次完整分析（推荐 Kaggle Titanic）

Matplotlib（目标：1-2周）
  [ ] 掌握 fig, ax = plt.subplots() 写法
  [ ] 能画折线图、散点图、柱状图、直方图
  [ ] 能创建多子图布局
  [ ] 能加标题、坐标轴、图例、网格
  [ ] 能保存高质量图片

综合项目
  [ ] 完成 04_综合实战项目.py
  [ ] 能独立找一个感兴趣的数据集，完成完整分析

推荐真实数据集练习来源：
  https://www.kaggle.com/datasets
  https://archive.ics.uci.edu/
  国家统计局开放数据：data.stats.gov.cn
"""

print(checklist)
