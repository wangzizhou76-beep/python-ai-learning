"""
═══════════════════════════════════════════════════════════════
  Pandas 核心基础 — 第二课
  目标：掌握 Series、DataFrame、数据清洗、groupby、merge
  建议学习时间：4-5 天
  前置：完成第一课 NumPy 基础
═══════════════════════════════════════════════════════════════
"""

import pandas as pd
import numpy as np

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 第 1 节：Pandas 两大核心数据结构
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
print("=" * 60)
print("第 1 节：Series 与 DataFrame")
print("=" * 60)

# ── 1.1 Series：带标签的一维数组 ──
print("\n--- Series ---")

# 创建方式
s1 = pd.Series([10, 20, 30, 40])                    # 默认索引 0,1,2,3
s2 = pd.Series([10, 20, 30, 40],
               index=['a', 'b', 'c', 'd'])           # 自定义索引
s3 = pd.Series({'苹果': 5, '香蕉': 3, '橙子': 8}) # 从字典创建

print("默认索引 Series:\n", s1)
print("\n字符串索引 Series:\n", s2)
print("\n从字典创建:\n", s3)

# 访问数据
print("\ns2['b']:", s2['b'])          # 用标签访问
print("s2[1]:", s2[1])               # 用位置访问（和列表一样）
print("s2[['a','c']]:\n", s2[['a','c']])  # 多标签
print("s2 > 15:\n", s2[s2 > 15])    # 布尔过滤

# Series 运算（自动按索引对齐！这是 Pandas 最独特的特性）
s4 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
s5 = pd.Series([10, 20, 30], index=['b', 'c', 'd'])
print("\nSeries 相加（自动对齐，缺失用 NaN）:\n", s4 + s5)
# 注意：a 和 d 都是 NaN，因为另一个 Series 没有对应的索引


# ── 1.2 DataFrame：带标签的二维表格（最常用）──
print("\n--- DataFrame ---")

# 创建方式1：从字典创建（每个键是列名）
students = pd.DataFrame({
    '姓名': ['张三', '李四', '王五', '赵六', '陈七'],
    '年龄': [22, 24, 21, 23, 25],
    '成绩': [85, 92, 78, 88, 95],
    '城市': ['北京', '上海', '北京', '广州', '上海'],
    '是否通过': [True, True, False, True, True]
})
print(students)
print("\n形状:", students.shape)
print("列名:", list(students.columns))
print("行索引:", students.index.tolist())

# 创建方式2：从 NumPy 数组
np.random.seed(42)
df2 = pd.DataFrame(
    np.random.randn(5, 3),
    index=['r1','r2','r3','r4','r5'],
    columns=['特征A', '特征B', '特征C']
)
print("\nNumPy数组创建的DataFrame:\n", df2.round(3))

# 基本信息查看
print("\n\n--- DataFrame 基本信息 ---")
print("df.info()：")
students.info()
print("\ndf.describe()（只对数值列）:\n", students.describe())
print("\n前3行:\n", students.head(3))
print("\n后2行:\n", students.tail(2))


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 第 2 节：索引与选取 — loc vs iloc
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
print("\n" + "=" * 60)
print("第 2 节：数据选取 loc / iloc / []")
print("=" * 60)

df = students.copy()
df.index = ['s1', 's2', 's3', 's4', 's5']  # 设置自定义行索引

# ── 选取列 ──
print("单列（返回Series）:\n", df['姓名'])
print("\n多列（返回DataFrame）:\n", df[['姓名', '成绩']])

# ── loc：用标签选取（行标签 + 列名）──
print("\n--- loc（标签索引）---")
print("df.loc['s1']（第1行）:\n", df.loc['s1'])
print("\ndf.loc['s2':'s4', '姓名':'成绩']:\n", df.loc['s2':'s4', '姓名':'成绩'])
# 注意：loc 的切片是两端都包含的！

# ── iloc：用位置选取（纯数字位置）──
print("\n--- iloc（位置索引）---")
print("df.iloc[0]（第0行）:\n", df.iloc[0])
print("\ndf.iloc[1:4, 0:3]（第1-3行，第0-2列）:\n", df.iloc[1:4, 0:3])
print("\ndf.iloc[[0,2,4], [0,2]]（指定行列）:\n", df.iloc[[0,2,4], [0,2]])

# ── 布尔索引 ──
print("\n--- 条件过滤 ---")
print("成绩大于85分的学生:\n", df[df['成绩'] > 85])
print("\n来自北京或成绩超过90的学生:\n",
      df[(df['城市'] == '北京') | (df['成绩'] > 90)])

# query 方法（更直观的条件查询）
print("\nquery 写法:\n", df.query("城市 == '北京' and 成绩 > 80"))


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 第 3 节：添加/修改/删除数据
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
print("\n" + "=" * 60)
print("第 3 节：增删改操作")
print("=" * 60)

df = students.copy()

# 添加新列
df['等级'] = df['成绩'].apply(lambda x: 'A' if x >= 90 else ('B' if x >= 80 else 'C'))
df['成绩×2'] = df['成绩'] * 2
print("添加列后:\n", df)

# 修改数据
df.loc[df['成绩'] < 80, '成绩'] = 80  # 把不及格的成绩改为80
print("\n修改后:\n", df[['姓名', '成绩']])

# 删除列/行
df2 = df.drop(columns=['成绩×2'])                    # 删除列
df3 = df.drop(index=[0, 1])                           # 删除行（默认数字索引）
print("\n删除列后的列:", df2.columns.tolist())

# 重命名
df.rename(columns={'姓名': 'name', '年龄': 'age'}, inplace=True)
print("\n重命名后:\n", df.head(2))

# 重置索引
df.reset_index(drop=True, inplace=True)  # drop=True 不把旧索引加入列
print("重置索引后索引:", df.index.tolist())


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 第 4 节：数据清洗 — 真实数据 80% 时间在干这个
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
print("\n" + "=" * 60)
print("第 4 节：数据清洗")
print("=" * 60)

# 创建一个"脏"数据集
dirty_data = pd.DataFrame({
    '姓名': ['张三', '李四', None, '张三', '王五', '赵六'],
    '年龄': [22, None, 21, 22, 200, 23],   # 200是异常值
    '成绩': [85.0, 92.0, 78.0, 85.0, None, 88.0],
    '城市': ['北京', '上海 ', 'beijing', '北京', '广州', '上海'],  # 有空格和大小写问题
})
print("原始脏数据:\n", dirty_data)

# ── 4.1 处理缺失值（NaN）──
print("\n--- 缺失值处理 ---")
print("每列缺失数量:\n", dirty_data.isnull().sum())
print("缺失值位置:\n", dirty_data.isnull())

# 删除含缺失值的行（谨慎使用！会丢数据）
df_dropped = dirty_data.dropna()
print(f"\n删除后剩余行数: {len(df_dropped)} （原{len(dirty_data)}行）")

# 填充缺失值（推荐）
df_filled = dirty_data.copy()
df_filled['年龄'].fillna(df_filled['年龄'].median(), inplace=True)  # 中位数填充
df_filled['成绩'].fillna(df_filled['成绩'].mean(), inplace=True)    # 均值填充
df_filled['姓名'].fillna('未知', inplace=True)                       # 固定值填充
print("\n填充后:\n", df_filled)

# ── 4.2 处理重复值 ──
print("\n--- 重复值处理 ---")
print("是否有重复行:\n", dirty_data.duplicated())
print("重复行:\n", dirty_data[dirty_data.duplicated()])
df_unique = dirty_data.drop_duplicates()
print(f"去重后行数: {len(df_unique)}")

# 按指定列去重
df_unique2 = dirty_data.drop_duplicates(subset=['姓名'], keep='first')

# ── 4.3 数据类型转换 ──
print("\n--- 数据类型 ---")
df_temp = dirty_data.copy()
df_temp['年龄'].fillna(0, inplace=True)
df_temp['年龄'] = df_temp['年龄'].astype(int)
print("年龄列类型:", df_temp['年龄'].dtype)

# ── 4.4 字符串清洗 ──
print("\n--- 字符串清洗 ---")
cities = dirty_data['城市'].copy()
cities_clean = (cities
                .str.strip()            # 去除首尾空格
                .str.lower()            # 统一小写
                .str.replace('beijing', '北京'))  # 替换英文
print("清洗前:", cities.tolist())
print("清洗后:", cities_clean.tolist())

# 常用字符串方法
s = pd.Series(['Alice Smith', 'Bob Jones', 'Carol White'])
print("\n提取名字（第一个单词）:", s.str.split(' ').str[0].tolist())
print("是否包含 'Smith':", s.str.contains('Smith').tolist())
print("转大写:", s.str.upper().tolist())

# ── 4.5 异常值处理 ──
print("\n--- 异常值检测 ---")
ages = pd.Series([22, 23, 21, 200, 22, 23, 24, 22])
Q1 = ages.quantile(0.25)
Q3 = ages.quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
print(f"Q1={Q1}, Q3={Q3}, IQR={IQR}")
print(f"正常范围: [{lower}, {upper}]")
print("异常值:", ages[(ages < lower) | (ages > upper)].tolist())


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 第 5 节：apply 与向量化操作
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
print("\n" + "=" * 60)
print("第 5 节：apply 与函数应用")
print("=" * 60)

df = pd.DataFrame({
    '数学': [85, 92, 78, 88, 95],
    '英语': [72, 88, 91, 76, 82],
    '物理': [90, 85, 70, 93, 88]
})

# apply：对列或行应用函数
print("每列最大值:\n", df.apply(np.max, axis=0))
print("\n每行总分:\n", df.apply(np.sum, axis=1))

# apply + lambda（超常用）
df['总分'] = df.apply(lambda row: row.sum(), axis=1)
df['等级'] = df['总分'].apply(lambda x:
    'A' if x >= 260 else ('B' if x >= 230 else 'C'))
print("\n加工后:\n", df)

# applymap（对每个元素）
grade_df = df[['数学', '英语', '物理']].applymap(
    lambda x: '优' if x >= 90 else ('良' if x >= 80 else '差'))
print("\n等级转换:\n", grade_df)

# 向量化 vs apply（性能对比）
big_df = pd.DataFrame({'val': np.random.randn(100000)})

import time
t = time.time()
big_df['val'].apply(lambda x: x**2 + 2*x + 1)
print(f"\napply 耗时: {time.time()-t:.4f}s")

t = time.time()
big_df['val']**2 + 2*big_df['val'] + 1
print(f"向量化 耗时: {time.time()-t:.4f}s")
# 结论：能用向量化就不用 apply！apply 慢10-100倍


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 第 6 节：groupby — 分组聚合（SQL group by 的 Python 版）
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
print("\n" + "=" * 60)
print("第 6 节：groupby 分组聚合")
print("=" * 60)

sales = pd.DataFrame({
    '城市': ['北京','北京','上海','上海','广州','广州','北京'],
    '季度': ['Q1','Q2','Q1','Q2','Q1','Q2','Q1'],
    '销售额': [100, 150, 200, 180, 80, 120, 130],
    '利润':   [20, 35, 50, 40, 15, 28, 25]
})
print("原始数据:\n", sales)

# 6.1 基础聚合
print("\n按城市分组，各列均值:\n",
      sales.groupby('城市')[['销售额', '利润']].mean())

print("\n按城市分组，销售额总和:\n",
      sales.groupby('城市')['销售额'].sum())

# 6.2 多列分组
print("\n按城市+季度分组:\n",
      sales.groupby(['城市', '季度'])['销售额'].sum())

# 6.3 agg：一次应用多个聚合函数
result = sales.groupby('城市').agg(
    销售额总和=('销售额', 'sum'),
    销售额均值=('销售额', 'mean'),
    利润最大=('利润', 'max'),
    记录数=('销售额', 'count')
)
print("\nagg 多函数聚合:\n", result)

# 6.4 transform：保留原始行数（常用于添加分组统计列）
sales['城市平均销售额'] = sales.groupby('城市')['销售额'].transform('mean')
sales['超过城市平均'] = sales['销售额'] > sales['城市平均销售额']
print("\n添加分组统计列:\n", sales)

# 6.5 filter：保留满足条件的分组
big_cities = sales.groupby('城市').filter(lambda g: g['销售额'].sum() > 300)
print("\n销售额总和大于300的城市:\n", big_cities)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 第 7 节：数据合并 — merge / join / concat
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
print("\n" + "=" * 60)
print("第 7 节：数据合并")
print("=" * 60)

# 两个相关表
students_info = pd.DataFrame({
    '学号': [1001, 1002, 1003, 1004],
    '姓名': ['张三', '李四', '王五', '赵六'],
    '年龄': [22, 23, 21, 24]
})
students_score = pd.DataFrame({
    '学号': [1001, 1002, 1003, 1005],  # 1004没有成绩，1005没有信息
    '课程': ['数学', '数学', '数学', '数学'],
    '成绩': [85, 92, 78, 88]
})
print("学生信息表:\n", students_info)
print("\n成绩表:\n", students_score)

# ── 7.1 merge（类似 SQL JOIN）──
inner = pd.merge(students_info, students_score, on='学号', how='inner')
left  = pd.merge(students_info, students_score, on='学号', how='left')
right = pd.merge(students_info, students_score, on='学号', how='right')
outer = pd.merge(students_info, students_score, on='学号', how='outer')

print("\ninner join（只保留两边都有的）:\n", inner)
print("\nleft join（以左表为主）:\n", left)
print("\nouter join（保留所有）:\n", outer)

# ── 7.2 concat（堆叠拼接）──
df1 = pd.DataFrame({'A': [1,2], 'B': [3,4]})
df2 = pd.DataFrame({'A': [5,6], 'B': [7,8]})
df3 = pd.DataFrame({'C': [9,10], 'D': [11,12]})

print("\n纵向拼接（行方向）:\n", pd.concat([df1, df2], ignore_index=True))
print("\n横向拼接（列方向）:\n", pd.concat([df1, df3], axis=1))


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 第 8 节：排序与排名
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
print("\n" + "=" * 60)
print("第 8 节：排序与排名")
print("=" * 60)

df = pd.DataFrame({
    '姓名': ['张三','李四','王五','赵六','陈七'],
    '成绩': [85, 92, 85, 78, 92],
    '年龄': [22, 23, 21, 24, 22]
})

print("按成绩降序:\n",
      df.sort_values('成绩', ascending=False))

print("\n按成绩降序、年龄升序（多键排序）:\n",
      df.sort_values(['成绩','年龄'], ascending=[False, True]))

df['成绩排名'] = df['成绩'].rank(method='min', ascending=False).astype(int)
print("\n添加排名列:\n", df)

print("\n最高成绩的3位学生:\n",
      df.nlargest(3, '成绩'))


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 第 9 节：数据透视表
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
print("\n" + "=" * 60)
print("第 9 节：数据透视表 pivot_table")
print("=" * 60)

data = pd.DataFrame({
    '城市': ['北京','北京','北京','上海','上海','广州'],
    '季度': ['Q1','Q2','Q3','Q1','Q2','Q1'],
    '产品': ['A','B','A','B','A','A'],
    '销售额': [100,150,120,200,180,80]
})

pivot = pd.pivot_table(
    data,
    values='销售额',      # 聚合什么
    index='城市',         # 行
    columns='季度',       # 列
    aggfunc='sum',        # 聚合方式
    fill_value=0          # 缺失值填充
)
print("透视表:\n", pivot)

# 交叉制表（统计频次）
crosstab = pd.crosstab(data['城市'], data['产品'])
print("\n交叉表（各城市各产品记录数）:\n", crosstab)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 第 10 节：读写文件
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
print("\n" + "=" * 60)
print("第 10 节：读写文件")
print("=" * 60)

# 创建示例 DataFrame
sample_df = pd.DataFrame({
    '姓名': ['张三', '李四', '王五'],
    '成绩': [85, 92, 78],
    '城市': ['北京', '上海', '广州']
})

# CSV 读写（最常用）
sample_df.to_csv('sample_data.csv', index=False, encoding='utf-8-sig')  # utf-8-sig 支持中文 Excel 打开
df_loaded = pd.read_csv('sample_data.csv', encoding='utf-8-sig')
print("从 CSV 读取:\n", df_loaded)

# 常用参数
"""
pd.read_csv(
    'file.csv',
    sep=',',           # 分隔符（也可以是 '\t' 等）
    header=0,          # 第几行作为列名，None 表示没有列名
    index_col=0,       # 哪列作为行索引
    nrows=100,         # 只读前100行（大文件常用）
    skiprows=[1,2],    # 跳过某些行
    usecols=['A','B'], # 只读某些列
    dtype={'col': str},# 指定某列的数据类型
    na_values=['NA','缺失'], # 哪些值当作 NaN
    encoding='utf-8'
)
"""

# Excel 读写
sample_df.to_excel('sample_data.xlsx', sheet_name='学生数据', index=False)
df_excel = pd.read_excel('sample_data.xlsx', sheet_name='学生数据')
print("从 Excel 读取:\n", df_excel)

print("\n常用格式总结：")
print("  CSV:   read_csv / to_csv（最通用）")
print("  Excel: read_excel / to_excel（需要 openpyxl）")
print("  JSON:  read_json / to_json")
print("  Parquet: read_parquet / to_parquet（大数据推荐，压缩+快速）")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 第 11 节：综合实战 — 分析电商销售数据
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
print("\n" + "=" * 60)
print("第 11 节：综合实战 — 电商销售分析")
print("=" * 60)

np.random.seed(42)
n = 500

# 模拟数据集
ecommerce = pd.DataFrame({
    '订单ID':  range(1001, 1001+n),
    '用户ID':  np.random.randint(1, 101, n),
    '商品类别': np.random.choice(['电子','服装','食品','图书','家居'], n,
                                p=[0.3, 0.25, 0.2, 0.1, 0.15]),
    '城市':    np.random.choice(['北京','上海','广州','深圳','成都'], n),
    '金额':    np.round(np.random.exponential(200, n) + 20, 2),
    '是否退款': np.random.choice([True, False], n, p=[0.1, 0.9]),
    '月份':    np.random.choice(range(1, 13), n)
})

# 故意制造一些缺失值
ecommerce.loc[np.random.choice(n, 20), '金额'] = np.nan

print(f"数据集规模: {ecommerce.shape}")
print("前3行:\n", ecommerce.head(3))

# 分析1：数据质量检查
print(f"\n缺失值: {ecommerce.isnull().sum().sum()} 个")
print(f"重复行: {ecommerce.duplicated().sum()} 行")

# 分析2：清洗数据
ecommerce.dropna(inplace=True)
print(f"清洗后行数: {len(ecommerce)}")

# 分析3：各城市销售额统计
city_stats = ecommerce.groupby('城市').agg(
    总订单数=('订单ID', 'count'),
    总销售额=('金额', 'sum'),
    平均订单金额=('金额', 'mean'),
    退款率=('是否退款', 'mean')
).round(2).sort_values('总销售额', ascending=False)
print("\n各城市销售统计:\n", city_stats)

# 分析4：各类别月度趋势
monthly = ecommerce.groupby(['月份', '商品类别'])['金额'].sum().unstack()
print("\n各类别月度销售额（前3月）:\n", monthly.head(3).round(0))

# 分析5：找出高价值用户（总消费额 top 10%）
user_total = ecommerce.groupby('用户ID')['金额'].sum()
threshold = user_total.quantile(0.9)
high_value_users = user_total[user_total >= threshold]
print(f"\n高价值用户（top 10%）门槛: {threshold:.2f} 元")
print(f"高价值用户数量: {len(high_value_users)} 人")
print(f"高价值用户贡献: {high_value_users.sum()/user_total.sum():.1%} 的销售额")


print("\n" + "=" * 60)
print("🏋️  课后练习题")
print("=" * 60)
print("""
用上面的 ecommerce 数据集完成以下分析：

1. 找出销售额最高的商品类别，并计算该类别占总销售额的比例

2. 找出退款率最高的城市，退款主要集中在哪个商品类别？

3. 用 pivot_table 展示每个城市在每个月的销售额总和（行=城市，列=月份）

4. 找出既在北京又在上海有订单的用户ID（使用集合操作）
   提示：set(df1['用户ID']) & set(df2['用户ID'])

5. 对金额列进行分箱（pd.cut），分为 低(<100)、中(100-300)、高(>300) 三档，
   统计各档位的订单数量和平均金额
   提示：pd.cut(ecommerce['金额'], bins=[0,100,300,float('inf')], labels=['低','中','高'])
""")
