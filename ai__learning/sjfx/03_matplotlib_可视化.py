"""
═══════════════════════════════════════════════════════════════
  Matplotlib & Seaborn 可视化 — 第三课
  目标：掌握 AI 领域最常用的图表类型，输出专业级图形
  建议学习时间：3-4 天
  前置：完成第一课和第二课
═══════════════════════════════════════════════════════════════
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

# 解决中文显示问题（必须放在所有 plt 操作之前）
plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.dpi'] = 100

print("=" * 60)
print("matplotlib 版本:", mpl.__version__)
print("=" * 60)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 第 1 节：核心概念 — Figure / Axes 是什么
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
print("\n第 1 节：核心概念")
print("""
Matplotlib 的层次结构：
  Figure（画布）
    └── Axes（坐标系/子图）  ← 这才是真正的"图"
          ├── x轴、y轴
          ├── 标题、图例
          └── 数据（线、点、柱等）

两种写法：
  1. plt.xxx()  — 简洁，适合单图
  2. fig, ax = plt.subplots() — 推荐！更灵活，可以画多子图
""")

# ── 写法1：pyplot 风格（简洁）──
x = np.linspace(0, 2*np.pi, 100)
plt.plot(x, np.sin(x))
plt.title('正弦波（pyplot风格）')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.savefig('01_基础折线图.png', bbox_inches='tight')
plt.close()
print("保存：01_基础折线图.png")

# ── 写法2：面向对象风格（推荐）──
fig, ax = plt.subplots(figsize=(8, 4))  # 指定画布大小（英寸）
ax.plot(x, np.sin(x), label='sin(x)')
ax.plot(x, np.cos(x), label='cos(x)')
ax.set_title('正弦与余弦（面向对象风格）', fontsize=14)
ax.set_xlabel('x 轴')
ax.set_ylabel('y 轴')
ax.legend()  # 显示图例
ax.grid(True, alpha=0.3)  # 网格线（半透明）
plt.savefig('02_正弦余弦.png', bbox_inches='tight')
plt.close()
print("保存：02_正弦余弦.png")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 第 2 节：折线图 — 最常用于时序和训练曲线
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
print("\n第 2 节：折线图（AI训练曲线）")

np.random.seed(42)
epochs = np.arange(1, 51)
train_loss = np.exp(-epochs/15) + np.random.normal(0, 0.02, 50)
val_loss   = np.exp(-epochs/18) + np.random.normal(0, 0.03, 50) + 0.05

fig, axes = plt.subplots(1, 2, figsize=(14, 5))
fig.suptitle('模型训练曲线', fontsize=16, fontweight='bold')

# 左图：Loss 曲线
ax1 = axes[0]
ax1.plot(epochs, train_loss, color='steelblue', linewidth=2,
         label='训练集 Loss', marker='o', markersize=3)
ax1.plot(epochs, val_loss, color='tomato', linewidth=2,
         label='验证集 Loss', linestyle='--')
ax1.set_title('Loss 曲线')
ax1.set_xlabel('Epoch')
ax1.set_ylabel('Loss')
ax1.legend(loc='upper right')
ax1.grid(True, alpha=0.3)
# 标注最低点
best_epoch = np.argmin(val_loss) + 1
best_loss = val_loss[best_epoch-1]
ax1.annotate(f'最佳: Epoch {best_epoch}',
             xy=(best_epoch, best_loss),
             xytext=(best_epoch+5, best_loss+0.05),
             arrowprops=dict(arrowstyle='->', color='gray'),
             fontsize=9)

# 右图：Accuracy 曲线（假设 acc = 1 - loss归一化）
acc_max = 0.95
train_acc = acc_max * (1 - np.exp(-epochs/10)) + np.random.normal(0, 0.01, 50)
val_acc   = acc_max * (1 - np.exp(-epochs/12)) + np.random.normal(0, 0.015, 50) - 0.02

ax2 = axes[1]
ax2.plot(epochs, np.clip(train_acc, 0, 1), color='steelblue', linewidth=2, label='训练集 Acc')
ax2.plot(epochs, np.clip(val_acc, 0, 1), color='tomato', linewidth=2,
         linestyle='--', label='验证集 Acc')
ax2.axhline(y=0.9, color='green', linestyle=':', alpha=0.7, label='目标 90%')
ax2.set_title('Accuracy 曲线')
ax2.set_xlabel('Epoch')
ax2.set_ylabel('Accuracy')
ax2.set_ylim(0, 1.05)
ax2.yaxis.set_major_formatter(mpl.ticker.PercentFormatter(xmax=1))  # 显示百分比
ax2.legend()
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('03_训练曲线.png', bbox_inches='tight')
plt.close()
print("保存：03_训练曲线.png")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 第 3 节：散点图 — 最常用于特征分布和相关性
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
print("\n第 3 节：散点图")

np.random.seed(42)
n = 300

# 生成两类数据（二分类场景）
class0_x = np.random.randn(n//2) * 1.5 - 1
class0_y = np.random.randn(n//2) * 1.5 - 1
class1_x = np.random.randn(n//2) * 1.5 + 1.5
class1_y = np.random.randn(n//2) * 1.5 + 1.5

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# 左图：基础散点图
ax = axes[0]
ax.scatter(class0_x, class0_y, c='steelblue', alpha=0.6,
           label='类别 0', s=40, edgecolors='white', linewidths=0.5)
ax.scatter(class1_x, class1_y, c='tomato', alpha=0.6,
           label='类别 1', s=40, edgecolors='white', linewidths=0.5)
ax.set_title('二分类数据分布')
ax.set_xlabel('特征 1')
ax.set_ylabel('特征 2')
ax.legend()
ax.grid(True, alpha=0.3)
ax.set_aspect('equal')

# 右图：气泡图（第三维度用大小表示）
ax = axes[1]
n_points = 50
x = np.random.randn(n_points)
y = np.random.randn(n_points)
size = np.random.randint(50, 500, n_points)     # 点的大小
color = np.random.randn(n_points)               # 点的颜色（连续值）

sc = ax.scatter(x, y, s=size, c=color, cmap='RdYlBu',
                alpha=0.7, edgecolors='gray', linewidths=0.5)
plt.colorbar(sc, ax=ax, label='第三维度（颜色）')
ax.set_title('气泡图（三维数据可视化）')
ax.set_xlabel('特征 X')
ax.set_ylabel('特征 Y')
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('04_散点图.png', bbox_inches='tight')
plt.close()
print("保存：04_散点图.png")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 第 4 节：柱状图 — 比较类别数据
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
print("\n第 4 节：柱状图")

categories = ['电子', '服装', '食品', '图书', '家居']
sales_2022  = [320, 180, 150, 95, 210]
sales_2023  = [410, 230, 180, 88, 265]

fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# 左图：单组柱状图
ax = axes[0]
bars = ax.bar(categories, sales_2023, color='steelblue',
              edgecolor='white', linewidth=0.5)
ax.set_title('2023年各类别销售额')
ax.set_xlabel('商品类别')
ax.set_ylabel('销售额（万元）')
# 在柱子上方添加数值标签
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 3,
            f'{height}', ha='center', va='bottom', fontsize=9)
ax.set_ylim(0, max(sales_2023) * 1.15)
ax.grid(True, axis='y', alpha=0.3)

# 中图：分组柱状图（对比两年数据）
ax = axes[1]
x = np.arange(len(categories))
width = 0.35
bars1 = ax.bar(x - width/2, sales_2022, width, label='2022年',
               color='steelblue', alpha=0.8)
bars2 = ax.bar(x + width/2, sales_2023, width, label='2023年',
               color='tomato', alpha=0.8)
ax.set_title('两年销售额对比')
ax.set_xlabel('商品类别')
ax.set_ylabel('销售额（万元）')
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.legend()
ax.grid(True, axis='y', alpha=0.3)

# 右图：水平柱状图（类别名长时更清晰）
ax = axes[2]
growth = [(b-a)/a*100 for a, b in zip(sales_2022, sales_2023)]
colors = ['tomato' if g > 10 else 'steelblue' for g in growth]
ax.barh(categories, growth, color=colors, edgecolor='white')
ax.axvline(x=0, color='black', linewidth=0.8)
ax.set_title('销售额增长率（%）')
ax.set_xlabel('增长率（%）')
ax.grid(True, axis='x', alpha=0.3)
for i, (cat, g) in enumerate(zip(categories, growth)):
    ax.text(g + 0.3 if g >= 0 else g - 0.3, i,
            f'{g:.1f}%', va='center', ha='left' if g >= 0 else 'right', fontsize=9)

plt.tight_layout()
plt.savefig('05_柱状图.png', bbox_inches='tight')
plt.close()
print("保存：05_柱状图.png")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 第 5 节：直方图 — 查看数据分布
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
print("\n第 5 节：直方图与分布")

np.random.seed(42)
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# 左图：基础直方图
ax = axes[0]
data = np.random.normal(100, 15, 1000)  # 均值100，标准差15
ax.hist(data, bins=30, color='steelblue', edgecolor='white',
        linewidth=0.5, alpha=0.8)
ax.axvline(data.mean(), color='red', linestyle='--',
           linewidth=2, label=f'均值={data.mean():.1f}')
ax.axvline(data.median(), color='orange', linestyle='-.',
           linewidth=2, label=f'中位数={data.median():.1f}')
ax.set_title('正态分布直方图')
ax.set_xlabel('值')
ax.set_ylabel('频次')
ax.legend()

# 中图：多组对比直方图
ax = axes[1]
group_a = np.random.normal(70, 10, 500)
group_b = np.random.normal(85, 8, 500)
ax.hist(group_a, bins=25, alpha=0.6, color='steelblue', label='A组', density=True)
ax.hist(group_b, bins=25, alpha=0.6, color='tomato', label='B组', density=True)
ax.set_title('两组成绩分布对比')
ax.set_xlabel('成绩')
ax.set_ylabel('概率密度')
ax.legend()

# 右图：直方图 + 核密度估计（KDE）
from scipy import stats  # 如果没有请 pip install scipy
ax = axes[2]
data3 = np.concatenate([np.random.normal(-2, 1, 400),
                         np.random.normal(3, 0.8, 600)])
ax.hist(data3, bins=40, density=True, color='steelblue',
        alpha=0.5, edgecolor='white', label='直方图')
# 绘制 KDE 曲线
kde_x = np.linspace(data3.min()-1, data3.max()+1, 300)
kde = stats.gaussian_kde(data3)
ax.plot(kde_x, kde(kde_x), 'r-', linewidth=2, label='KDE 曲线')
ax.set_title('直方图 + 核密度估计')
ax.set_xlabel('值')
ax.set_ylabel('密度')
ax.legend()

plt.tight_layout()
plt.savefig('06_直方图.png', bbox_inches='tight')
plt.close()
print("保存：06_直方图.png")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 第 6 节：热力图 — 可视化矩阵（相关性、混淆矩阵）
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
print("\n第 6 节：热力图（相关矩阵 & 混淆矩阵）")

fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# 左图：相关矩阵热力图
np.random.seed(42)
n = 200
features = pd.DataFrame({
    '身高': np.random.normal(170, 10, n),
    '体重': np.random.normal(65, 12, n),
    '年龄': np.random.randint(18, 60, n),
    '收入': np.random.exponential(5000, n) + 2000,
    '消费': np.random.exponential(2000, n) + 1000
})
features['体重'] = features['体重'] + features['身高'] * 0.3  # 制造相关性
features['消费'] = features['消费'] + features['收入'] * 0.4

corr_matrix = features.corr()

ax = axes[0]
im = ax.imshow(corr_matrix, cmap='RdBu_r', vmin=-1, vmax=1, aspect='auto')
plt.colorbar(im, ax=ax)
ax.set_xticks(range(len(corr_matrix.columns)))
ax.set_yticks(range(len(corr_matrix.columns)))
ax.set_xticklabels(corr_matrix.columns, rotation=45, ha='right')
ax.set_yticklabels(corr_matrix.columns)
ax.set_title('特征相关性矩阵')
# 在格子中添加数值
for i in range(len(corr_matrix)):
    for j in range(len(corr_matrix.columns)):
        val = corr_matrix.iloc[i, j]
        color = 'white' if abs(val) > 0.5 else 'black'
        ax.text(j, i, f'{val:.2f}', ha='center', va='center',
                fontsize=9, color=color)

# 右图：混淆矩阵（分类模型评估）
confusion = np.array([[85,  3,  2],
                       [ 4, 72,  8],
                       [ 1,  5, 91]])
class_names = ['猫', '狗', '鸟']

ax = axes[1]
im2 = ax.imshow(confusion, cmap='Blues', aspect='auto')
plt.colorbar(im2, ax=ax)
ax.set_xticks(range(3))
ax.set_yticks(range(3))
ax.set_xticklabels(['预测:猫', '预测:狗', '预测:鸟'])
ax.set_yticklabels(['实际:猫', '实际:狗', '实际:鸟'])
ax.set_title('混淆矩阵')
ax.set_xlabel('预测标签')
ax.set_ylabel('真实标签')
# 在每格显示数量和百分比
for i in range(3):
    row_total = confusion[i].sum()
    for j in range(3):
        color = 'white' if confusion[i,j] > confusion.max()/2 else 'black'
        ax.text(j, i, f'{confusion[i,j]}\n({confusion[i,j]/row_total:.0%})',
                ha='center', va='center', color=color, fontsize=10)

plt.tight_layout()
plt.savefig('07_热力图.png', bbox_inches='tight')
plt.close()
print("保存：07_热力图.png")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 第 7 节：子图布局 — 组合多个图表
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
print("\n第 7 节：子图布局")

np.random.seed(42)

# 使用 GridSpec 实现复杂布局
fig = plt.figure(figsize=(16, 10))
fig.suptitle('数据分析综合面板', fontsize=16, fontweight='bold', y=1.01)
gs = fig.add_gridspec(3, 3, hspace=0.4, wspace=0.35)

# 大图（占左侧2行2列）
ax_main = fig.add_subplot(gs[:2, :2])
x = np.linspace(0, 10, 200)
ax_main.plot(x, np.sin(x) * np.exp(-x/10), linewidth=2, color='steelblue')
ax_main.fill_between(x, np.sin(x) * np.exp(-x/10), alpha=0.2, color='steelblue')
ax_main.set_title('主图：衰减正弦波', fontsize=12)
ax_main.set_xlabel('时间 (s)')
ax_main.set_ylabel('振幅')
ax_main.grid(True, alpha=0.3)

# 右上：柱状图
ax_bar = fig.add_subplot(gs[0, 2])
vals = [23, 45, 12, 67, 34]
labs = ['A','B','C','D','E']
ax_bar.bar(labs, vals, color='tomato', alpha=0.8)
ax_bar.set_title('类别统计', fontsize=10)
ax_bar.grid(True, axis='y', alpha=0.3)

# 右中：散点图
ax_scat = fig.add_subplot(gs[1, 2])
x_s = np.random.randn(100)
y_s = x_s * 1.5 + np.random.randn(100) * 0.5
ax_scat.scatter(x_s, y_s, alpha=0.5, s=20, color='green')
ax_scat.set_title('相关性', fontsize=10)

# 下左：直方图
ax_hist = fig.add_subplot(gs[2, 0])
ax_hist.hist(np.random.normal(0, 1, 500), bins=30,
             color='steelblue', edgecolor='white', alpha=0.8)
ax_hist.set_title('分布', fontsize=10)

# 下中：箱线图
ax_box = fig.add_subplot(gs[2, 1])
data_box = [np.random.normal(loc, 1, 100) for loc in [1, 3, 2, 4]]
bp = ax_box.boxplot(data_box, patch_artist=True,
                    boxprops=dict(facecolor='steelblue', alpha=0.6))
ax_box.set_xticklabels(['Q1','Q2','Q3','Q4'])
ax_box.set_title('箱线图', fontsize=10)

# 下右：饼图
ax_pie = fig.add_subplot(gs[2, 2])
sizes = [35, 25, 20, 15, 5]
lbls  = ['A','B','C','D','其他']
ax_pie.pie(sizes, labels=lbls, autopct='%1.1f%%',
           colors=['steelblue','tomato','green','orange','purple'])
ax_pie.set_title('占比', fontsize=10)

plt.savefig('08_综合面板.png', bbox_inches='tight')
plt.close()
print("保存：08_综合面板.png")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 第 8 节：Seaborn — 统计可视化利器
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
print("\n第 8 节：Seaborn 统计可视化")

try:
    import seaborn as sns
    sns.set_theme(style='whitegrid', font='SimHei')

    np.random.seed(42)
    n = 300

    # 创建示例数据
    df = pd.DataFrame({
        '分组': np.repeat(['A组','B组','C组'], n//3),
        '成绩': np.concatenate([
            np.random.normal(78, 12, n//3),
            np.random.normal(85, 10, n//3),
            np.random.normal(72, 15, n//3)
        ]),
        '练习时间': np.random.exponential(3, n) + 1,
        '性别': np.random.choice(['男','女'], n)
    })

    fig, axes = plt.subplots(2, 3, figsize=(18, 11))
    fig.suptitle('Seaborn 统计图表示例', fontsize=16, fontweight='bold')

    # 1. 箱线图（带分组）
    ax = axes[0, 0]
    sns.boxplot(data=df, x='分组', y='成绩', hue='性别',
                palette='Set2', ax=ax)
    ax.set_title('各组成绩箱线图（按性别分组）')

    # 2. 小提琴图（分布更直观）
    ax = axes[0, 1]
    sns.violinplot(data=df, x='分组', y='成绩',
                   palette='husl', inner='box', ax=ax)
    ax.set_title('成绩分布小提琴图')

    # 3. 带抖动的条带图（适合小数据集）
    ax = axes[0, 2]
    df_small = df.sample(60)
    sns.stripplot(data=df_small, x='分组', y='成绩',
                  hue='性别', dodge=True, alpha=0.6,
                  palette='Set1', ax=ax)
    ax.set_title('成绩条带图')

    # 4. 散点图 + 回归线
    ax = axes[1, 0]
    sns.regplot(data=df, x='练习时间', y='成绩',
                scatter_kws={'alpha':0.3, 's':20},
                line_kws={'color':'red', 'linewidth':2},
                ax=ax)
    ax.set_title('练习时间 vs 成绩（回归线）')
    ax.set_xlabel('练习时间（小时/天）')

    # 5. 分布图（KDE + 直方图）
    ax = axes[1, 1]
    for grp, color in zip(['A组','B组','C组'], ['steelblue','tomato','green']):
        subset = df[df['分组'] == grp]['成绩']
        sns.kdeplot(subset, label=grp, color=color, linewidth=2, ax=ax)
    ax.set_title('各组成绩核密度分布')
    ax.legend()
    ax.set_xlabel('成绩')

    # 6. 计数图（类别频次）
    ax = axes[1, 2]
    sns.countplot(data=df, x='分组', hue='性别',
                  palette='Set2', ax=ax)
    ax.set_title('各组人数统计')
    for container in ax.containers:
        ax.bar_label(container, fontsize=9)

    plt.tight_layout()
    plt.savefig('09_seaborn统计图.png', bbox_inches='tight')
    plt.close()
    print("保存：09_seaborn统计图.png")

except ImportError:
    print("提示：请先安装 seaborn：pip install seaborn")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 第 9 节：图表美化 — 输出专业级图形
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
print("\n第 9 节：图表美化技巧")

# 创建一张"简陋版"和"专业版"的对比
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

x = np.linspace(0, 4*np.pi, 200)
y1 = np.sin(x)
y2 = np.sin(x) * 0.7 + 0.3

# 左图：简陋版（初学者常见写法）
ax = axes[0]
ax.plot(x, y1)
ax.plot(x, y2)
ax.set_title('简陋版')

# 右图：专业版
ax = axes[1]
# 去除上右边框
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('#aaa')
ax.spines['bottom'].set_color('#aaa')

# 精心选色，线条加粗
ax.plot(x, y1, color='#2E86AB', linewidth=2.5, label='信号 A',
        solid_capstyle='round')
ax.plot(x, y2, color='#E84855', linewidth=2.5, linestyle='--',
        label='信号 B', solid_capstyle='round')

# 填充区域
ax.fill_between(x, y1, y2, where=(y1>y2), alpha=0.15,
                color='#2E86AB', label='A > B')

# 精细调整标签
ax.set_title('专业版', fontsize=14, fontweight='bold', pad=15)
ax.set_xlabel('时间 (s)', fontsize=11, labelpad=8)
ax.set_ylabel('振幅', fontsize=11, labelpad=8)
ax.tick_params(colors='#555', labelsize=9)

# 图例放在最佳位置
ax.legend(loc='upper right', frameon=True, framealpha=0.9,
          edgecolor='#ddd', fontsize=10)

# 精细网格（只有横线，半透明）
ax.yaxis.grid(True, color='#ddd', linewidth=0.8)
ax.set_axisbelow(True)  # 网格在数据下面

# 添加说明文字
ax.text(0.02, 0.98, '振幅比较实验', transform=ax.transAxes,
        fontsize=10, color='gray', va='top')

plt.tight_layout()
plt.savefig('10_图表美化对比.png', bbox_inches='tight', dpi=150)
plt.close()
print("保存：10_图表美化对比.png")

print("\n" + "=" * 60)
print("📌 图表样式速查表")
print("=" * 60)
print("""
常用颜色方案：
  单色：'steelblue', 'tomato', '#2E86AB'
  色板：plt.cm.tab10, plt.cm.Set2, plt.cm.RdBu_r

线型：'-'（实线）, '--'（虚线）, '-.'（点划线）, ':'（点线）
标记：'o'（圆）, 's'（方）, '^'（三角）, 'D'（菱形）, '*'（星）

常用参数：
  linewidth=2, markersize=8, alpha=0.7
  color=, linestyle=, marker=, label=

保存图片：
  plt.savefig('图片.png', dpi=150, bbox_inches='tight')
  plt.savefig('图片.pdf', bbox_inches='tight')  # 矢量图
""")

print("\n" + "=" * 60)
print("🏋️  课后练习题")
print("=" * 60)
print("""
使用如下数据完成练习：
  months = ['1月','2月','3月','4月','5月','6月']
  product_a = [120, 132, 101, 134, 90, 130]
  product_b = [220, 182, 191, 234, 290, 330]
  product_c = [150, 232, 201, 154, 190, 330]

1. 画一张折线图，展示三种产品 6 个月的销售趋势
   要求：有图例、网格线、标题、坐标轴标签

2. 画一张堆叠柱状图（stacked bar），展示每月三种产品的销售构成
   提示：ax.bar(x, a); ax.bar(x, b, bottom=a); ax.bar(x, c, bottom=[a+b for ...])

3. 画一张 2×3 的子图网格，每个子图显示一个月份的产品销售饼图

4. 生成 1000 个随机数据点（两个特征），用不同颜色画出训练集（80%）和测试集（20%）
   提示：先 np.random.shuffle，再按比例切分

5. 挑战题：模拟 5 个 Epoch 的训练过程，画出 Loss 随 Batch 变化的曲线
   要求：每个 Epoch 结束用竖线标出，图例注明各 Epoch
""")
