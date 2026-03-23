"""
═══════════════════════════════════════════════════════════════
  综合实战项目 — 第四课（压轴）
  从零完成一个完整的数据分析项目
  主题：通信基站流量数据分析与异常检测
  
  这个项目会用到：NumPy + Pandas + Matplotlib + 统计分析
  完成本项目 = 拥有一个可以写进简历的作品
═══════════════════════════════════════════════════════════════
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from scipy import stats

# 中文支持
plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.dpi'] = 100

np.random.seed(42)
print("=" * 70)
print("  📡 通信基站流量数据分析 — 完整数据分析项目")
print("=" * 70)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Step 1：数据生成（模拟真实基站数据）
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
print("\n📥 Step 1: 生成模拟数据集")

# 参数设置
n_stations = 20       # 20个基站
n_days     = 30       # 30天
hours      = 24       # 每天24个时间点

# 生成时间序列
dates = pd.date_range('2024-01-01', periods=n_days, freq='D')
stations = [f'BS_{i:03d}' for i in range(1, n_stations+1)]
cities   = np.random.choice(['北京','上海','广州','深圳','成都'],
                              n_stations, p=[0.3,0.25,0.2,0.15,0.1])
station_city = dict(zip(stations, cities))

# 模拟基站流量数据（带时间规律）
records = []
for station in stations:
    city = station_city[station]
    base_traffic = np.random.uniform(50, 200)  # 每站基础流量不同

    for date in dates:
        for hour in range(hours):
            # 模拟流量的时间规律（早晚高峰）
            if 7 <= hour <= 9:       # 早高峰
                time_factor = 1.8
            elif 18 <= hour <= 21:   # 晚高峰
                time_factor = 2.2
            elif 0 <= hour <= 5:     # 深夜低谷
                time_factor = 0.2
            else:                    # 其他时段
                time_factor = 1.0

            # 周末流量稍低
            weekday_factor = 0.8 if date.weekday() >= 5 else 1.0

            # 添加随机波动和噪声
            noise = np.random.normal(0, base_traffic * 0.1)
            traffic = max(0, base_traffic * time_factor * weekday_factor + noise)

            # 随机注入异常值（约1%）
            if np.random.random() < 0.01:
                traffic *= np.random.choice([5.0, 0.0])  # 突增或断流

            records.append({
                '基站ID': station,
                '城市': city,
                '日期': date.date(),
                '小时': hour,
                '流量(Mbps)': round(traffic, 2),
                '在线用户数': int(traffic * np.random.uniform(8, 12))
            })

df_raw = pd.DataFrame(records)
df_raw['日期'] = pd.to_datetime(df_raw['日期'])
df_raw['时间'] = pd.to_datetime(df_raw['日期'].astype(str) +
                                  ' ' + df_raw['小时'].astype(str) + ':00:00')

print(f"数据集规模: {df_raw.shape[0]:,} 行 × {df_raw.shape[1]} 列")
print(f"时间范围: {df_raw['日期'].min().date()} 至 {df_raw['日期'].max().date()}")
print(f"基站数量: {df_raw['基站ID'].nunique()} 个")
print(f"覆盖城市: {sorted(df_raw['城市'].unique())}")
print("\n数据样例:")
print(df_raw.head(5).to_string(index=False))


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Step 2：数据质量检查与清洗
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
print("\n🔍 Step 2: 数据质量检查")

# 基本质量检查
print(f"缺失值: {df_raw.isnull().sum().sum()} 个")
print(f"重复行: {df_raw.duplicated().sum()} 行")
print(f"\n各列类型:")
print(df_raw.dtypes)

# 流量统计
print(f"\n流量统计:")
print(df_raw['流量(Mbps)'].describe().round(2))

# 检测异常值（使用 Z-score 方法）
print("\n异常值检测（Z-score > 3）:")
df_clean = df_raw.copy()
z_scores = np.abs(stats.zscore(df_clean['流量(Mbps)']))
anomaly_mask = z_scores > 3
n_anomalies = anomaly_mask.sum()
print(f"  检测到 {n_anomalies} 个异常值（占 {n_anomalies/len(df_clean):.2%}）")

# 记录异常，用3σ上界替换
upper_bound = df_clean['流量(Mbps)'].mean() + 3 * df_clean['流量(Mbps)'].std()
df_clean.loc[anomaly_mask, '流量(Mbps)'] = upper_bound
df_clean.loc[df_clean['流量(Mbps)'] < 0, '流量(Mbps)'] = 0
print(f"  已将异常值替换为上界: {upper_bound:.2f} Mbps")
print(f"清洗后数据规模: {df_clean.shape}")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Step 3：探索性数据分析（EDA）
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
print("\n📊 Step 3: 探索性数据分析（EDA）")

# ── 3.1 整体流量趋势 ──
daily_traffic = (df_clean.groupby('日期')['流量(Mbps)']
                 .agg(['sum', 'mean', 'max'])
                 .reset_index())
daily_traffic.columns = ['日期', '总流量', '平均流量', '峰值流量']
print("\n每日流量统计（前5天）:")
print(daily_traffic.head().to_string(index=False))

# ── 3.2 小时流量规律 ──
hourly_avg = df_clean.groupby('小时')['流量(Mbps)'].mean().reset_index()
peak_hour = hourly_avg.loc[hourly_avg['流量(Mbps)'].idxmax(), '小时']
valley_hour = hourly_avg.loc[hourly_avg['流量(Mbps)'].idxmin(), '小时']
print(f"\n流量高峰时段: {peak_hour}:00")
print(f"流量低谷时段: {valley_hour}:00")

# ── 3.3 各城市对比 ──
city_stats = (df_clean.groupby('城市')
              .agg(总流量=('流量(Mbps)', 'sum'),
                   基站数=('基站ID', 'nunique'),
                   平均流量=('流量(Mbps)', 'mean'))
              .round(2)
              .sort_values('总流量', ascending=False))
print("\n各城市流量统计:")
print(city_stats)

# ── 3.4 基站负载排名 ──
station_load = (df_clean.groupby('基站ID')
                .agg(平均流量=('流量(Mbps)', 'mean'),
                     峰值流量=('流量(Mbps)', 'max'),
                     总流量=('流量(Mbps)', 'sum'))
                .round(2)
                .sort_values('平均流量', ascending=False))
print("\n负载最高的5个基站:")
print(station_load.head())

# ── 3.5 工作日 vs 周末 ──
df_clean['是否周末'] = df_clean['日期'].dt.weekday >= 5
weekday_vs_weekend = (df_clean.groupby('是否周末')['流量(Mbps)']
                      .mean().round(2))
weekday_vs_weekend.index = ['工作日', '周末']
print(f"\n工作日 vs 周末 平均流量:")
print(weekday_vs_weekend)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Step 4：异常基站识别
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
print("\n🚨 Step 4: 异常基站识别")

# 方法：如果某基站某天的流量与其历史均值偏差过大，标记为异常
station_mean = df_clean.groupby('基站ID')['流量(Mbps)'].mean()
df_clean['基站均值'] = df_clean['基站ID'].map(station_mean)
df_clean['偏差比'] = (df_clean['流量(Mbps)'] - df_clean['基站均值']) / df_clean['基站均值']

# 每天每个基站的最大偏差
daily_anomaly = (df_clean.groupby(['日期', '基站ID'])['偏差比']
                 .agg(['max', 'min'])
                 .reset_index())
daily_anomaly.columns = ['日期', '基站ID', '最大正偏差', '最大负偏差']
daily_anomaly['异常'] = (daily_anomaly['最大正偏差'] > 3.0) | \
                         (daily_anomaly['最大负偏差'] < -0.9)

n_abnormal_events = daily_anomaly['异常'].sum()
abnormal_stations  = daily_anomaly[daily_anomaly['异常']]['基站ID'].unique()
print(f"异常事件总数: {n_abnormal_events}")
print(f"涉及基站: {len(abnormal_stations)} 个")
print(f"异常基站ID: {sorted(abnormal_stations)}")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Step 5：数据可视化 — 出最终分析报告图
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
print("\n🎨 Step 5: 生成分析报告图")

# ═══ 图1：综合分析仪表板 ═══
fig = plt.figure(figsize=(20, 16))
fig.patch.set_facecolor('#F8F9FA')
gs = gridspec.GridSpec(3, 3, figure=fig, hspace=0.45, wspace=0.35)
fig.suptitle('📡 通信基站流量分析报告', fontsize=20,
             fontweight='bold', y=0.98, color='#2C3E50')

# 子图1：每日总流量趋势（大图）
ax1 = fig.add_subplot(gs[0, :2])
ax1.plot(daily_traffic['日期'], daily_traffic['总流量']/1000,
         color='#2E86AB', linewidth=2, marker='o', markersize=4)
ax1.fill_between(daily_traffic['日期'],
                  daily_traffic['总流量']/1000,
                  alpha=0.15, color='#2E86AB')
# 标记周末
for i, row in daily_traffic.iterrows():
    if row['日期'].weekday() >= 5:
        ax1.axvspan(row['日期'] - pd.Timedelta(hours=12),
                    row['日期'] + pd.Timedelta(hours=12),
                    alpha=0.08, color='gray')
ax1.set_title('每日总流量趋势（灰色区域为周末）', fontsize=12, pad=10)
ax1.set_xlabel('日期')
ax1.set_ylabel('总流量（Gbps）')
ax1.grid(True, alpha=0.3)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
# 添加7日移动平均
ma7 = daily_traffic['总流量'].rolling(7, min_periods=1).mean()
ax1.plot(daily_traffic['日期'], ma7/1000, color='red',
         linewidth=1.5, linestyle='--', alpha=0.7, label='7日均线')
ax1.legend()
plt.setp(ax1.xaxis.get_majorticklabels(), rotation=30, ha='right')

# 子图2：每小时流量规律（24小时热力图风格）
ax2 = fig.add_subplot(gs[0, 2])
hourly_by_weekday = df_clean.groupby(['是否周末', '小时'])['流量(Mbps)'].mean().unstack()
weekday_pattern = hourly_by_weekday.loc[False]
weekend_pattern = hourly_by_weekday.loc[True]
ax2.plot(range(24), weekday_pattern, color='#2E86AB',
         linewidth=2.5, label='工作日', marker='o', markersize=3)
ax2.plot(range(24), weekend_pattern, color='#E84855',
         linewidth=2.5, label='周末', linestyle='--', marker='s', markersize=3)
ax2.fill_between(range(24), weekday_pattern, weekend_pattern,
                  alpha=0.1, color='gray')
ax2.set_title('工作日/周末流量模式', fontsize=12, pad=10)
ax2.set_xlabel('小时')
ax2.set_ylabel('平均流量（Mbps）')
ax2.set_xticks([0,6,12,18,23])
ax2.set_xticklabels(['0:00','6:00','12:00','18:00','23:00'])
ax2.legend(fontsize=9)
ax2.grid(True, alpha=0.3)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)

# 子图3：各城市流量对比（水平柱状图）
ax3 = fig.add_subplot(gs[1, 0])
city_plot = city_stats.sort_values('总流量')
colors_city = ['#2E86AB' if c == city_plot['总流量'].max() else '#A8C8E8'
               for c in city_plot['总流量']]
bars = ax3.barh(city_plot.index, city_plot['总流量']/1e6,
                color=colors_city, edgecolor='white')
ax3.set_title('各城市总流量（PB）', fontsize=12, pad=10)
ax3.set_xlabel('总流量（PB）')
for bar in bars:
    w = bar.get_width()
    ax3.text(w+0.005, bar.get_y() + bar.get_height()/2,
             f'{w:.2f}', va='center', fontsize=9)
ax3.spines['top'].set_visible(False)
ax3.spines['right'].set_visible(False)
ax3.grid(True, axis='x', alpha=0.3)

# 子图4：基站负载分布直方图
ax4 = fig.add_subplot(gs[1, 1])
ax4.hist(station_load['平均流量'], bins=15,
         color='#2E86AB', edgecolor='white', alpha=0.8)
avg_load = station_load['平均流量'].mean()
ax4.axvline(avg_load, color='red', linestyle='--',
            linewidth=2, label=f'均值={avg_load:.1f}')
ax4.set_title('基站平均流量分布', fontsize=12, pad=10)
ax4.set_xlabel('平均流量（Mbps）')
ax4.set_ylabel('基站数量')
ax4.legend()
ax4.spines['top'].set_visible(False)
ax4.spines['right'].set_visible(False)

# 子图5：热力图（每基站每日流量）
ax5 = fig.add_subplot(gs[1, 2])
heatmap_data = (df_clean.groupby(['基站ID', '日期'])['流量(Mbps)']
                .mean().unstack())
# 只取前10个基站，避免太密
heatmap_data = heatmap_data.head(10)
im = ax5.imshow(heatmap_data.values, cmap='YlOrRd',
                aspect='auto', interpolation='nearest')
plt.colorbar(im, ax=ax5, shrink=0.8, label='Mbps')
ax5.set_title('基站×日期流量热力图', fontsize=12, pad=10)
ax5.set_xlabel('日期（索引）')
ax5.set_ylabel('基站ID')
ax5.set_yticks(range(10))
ax5.set_yticklabels(heatmap_data.index, fontsize=8)

# 子图6：异常事件时间分布
ax6 = fig.add_subplot(gs[2, :2])
anomaly_by_date = daily_anomaly.groupby('日期')['异常'].sum().reset_index()
ax6.bar(anomaly_by_date['日期'], anomaly_by_date['异常'],
        color='#E84855', alpha=0.8, width=0.8, edgecolor='white')
ax6.set_title('每日异常事件数量', fontsize=12, pad=10)
ax6.set_xlabel('日期')
ax6.set_ylabel('异常事件数')
ax6.grid(True, axis='y', alpha=0.3)
ax6.spines['top'].set_visible(False)
ax6.spines['right'].set_visible(False)
plt.setp(ax6.xaxis.get_majorticklabels(), rotation=30, ha='right')

# 子图7：关键指标汇总
ax7 = fig.add_subplot(gs[2, 2])
ax7.axis('off')
summary_text = [
    ('📊 数据集规模', f'{df_clean.shape[0]:,} 条记录'),
    ('📡 基站总数',   f'{df_clean["基站ID"].nunique()} 个'),
    ('🏙️ 覆盖城市',   f'{df_clean["城市"].nunique()} 个'),
    ('📅 分析周期',   f'{n_days} 天'),
    ('', ''),
    ('⚡ 峰值小时',   f'{peak_hour}:00'),
    ('😴 低谷小时',   f'{valley_hour}:00'),
    ('📈 日均总流量', f'{daily_traffic["总流量"].mean()/1000:.1f} Gbps'),
    ('', ''),
    ('🚨 异常事件',   f'{n_abnormal_events} 次'),
    ('⚠️ 问题基站',   f'{len(abnormal_stations)} 个'),
]
y_pos = 0.95
for label, value in summary_text:
    if not label:
        y_pos -= 0.04
        continue
    ax7.text(0.05, y_pos, label, transform=ax7.transAxes,
             fontsize=10, color='#555', va='top')
    ax7.text(0.6, y_pos, value, transform=ax7.transAxes,
             fontsize=10, color='#2C3E50', va='top', fontweight='bold')
    y_pos -= 0.08

ax7.set_title('关键指标汇总', fontsize=12, pad=10)
ax7.add_patch(plt.Rectangle((0, 0), 1, 1, fill=False,
                              edgecolor='#E0E0E0', linewidth=1,
                              transform=ax7.transAxes))

plt.savefig('11_综合分析报告.png', bbox_inches='tight', dpi=120,
            facecolor='#F8F9FA')
plt.close()
print("保存：11_综合分析报告.png")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Step 6：导出分析结果
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
print("\n💾 Step 6: 导出分析结果")

# 导出各类统计报表
with pd.ExcelWriter('基站流量分析报告.xlsx', engine='openpyxl') as writer:
    daily_traffic.to_excel(writer, sheet_name='每日流量趋势', index=False)
    city_stats.to_excel(writer, sheet_name='城市对比')
    station_load.to_excel(writer, sheet_name='基站负载排名')
    daily_anomaly[daily_anomaly['异常']].to_excel(
        writer, sheet_name='异常事件清单', index=False)

print("分析报告已导出：基站流量分析报告.xlsx")

# 导出清洗后的数据
df_clean.to_csv('cleaned_station_data.csv', index=False, encoding='utf-8-sig')
print("清洗后数据已导出：cleaned_station_data.csv")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Step 7：简单预测 — 用历史数据预测下周流量
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
print("\n🔮 Step 7: 流量预测（简单移动平均）")

# 用最近7天的移动平均预测未来7天
daily_total = (df_clean.groupby('日期')['流量(Mbps)']
               .sum().reset_index())
daily_total.columns = ['日期', '总流量']

window = 7
last_7_avg = daily_total['总流量'].tail(window).mean()
future_dates = pd.date_range(
    daily_total['日期'].max() + pd.Timedelta(days=1),
    periods=7, freq='D')

# 加入周末效应
weekend_factor = 0.8
future_traffic = []
for d in future_dates:
    factor = weekend_factor if d.weekday() >= 5 else 1.0
    pred = last_7_avg * factor
    future_traffic.append(pred)

future_df = pd.DataFrame({'日期': future_dates, '预测流量': future_traffic})

print("未来7天流量预测（Mbps）:")
for _, row in future_df.iterrows():
    weekday = ['周一','周二','周三','周四','周五','周六','周日'][row['日期'].weekday()]
    print(f"  {row['日期'].date()} ({weekday}): {row['预测流量']:.0f} Mbps")

# 画预测图
fig, ax = plt.subplots(figsize=(14, 5))
ax.plot(daily_total['日期'], daily_total['总流量']/1000,
        color='#2E86AB', linewidth=2, label='历史数据')
ax.plot(future_df['日期'], np.array(future_traffic)/1000,
        color='#E84855', linewidth=2, linestyle='--',
        marker='D', markersize=7, label='7日均值预测')

# 预测区间（简单±10%）
upper = np.array(future_traffic) * 1.1 / 1000
lower = np.array(future_traffic) * 0.9 / 1000
ax.fill_between(future_df['日期'], lower, upper,
                alpha=0.2, color='#E84855', label='预测区间（±10%）')

ax.axvline(daily_total['日期'].max(), color='gray',
           linestyle=':', linewidth=1.5, label='预测起点')
ax.set_title('基站总流量趋势 + 未来7天预测', fontsize=14)
ax.set_xlabel('日期')
ax.set_ylabel('总流量（Gbps）')
ax.legend()
ax.grid(True, alpha=0.3)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.setp(ax.xaxis.get_majorticklabels(), rotation=30, ha='right')
plt.tight_layout()
plt.savefig('12_流量预测.png', bbox_inches='tight')
plt.close()
print("\n保存：12_流量预测.png")


print("\n" + "=" * 70)
print("✅ 项目完成！生成文件清单：")
print("=" * 70)
print("""
数据文件：
  ├── cleaned_station_data.csv    清洗后的完整数据集
  └── 基站流量分析报告.xlsx        多表结构的分析结果

可视化：
  ├── 11_综合分析报告.png          7子图综合仪表板
  └── 12_流量预测.png              趋势预测图
""")

print("=" * 70)
print("💼 这个项目可以这样写进简历：")
print("=" * 70)
print("""
「通信基站流量数据分析」
- 使用 Python（NumPy/Pandas/Matplotlib）对 20个基站×30天×24小时
  的流量数据进行全流程分析
- 实现了基于 Z-score 的异常值检测，识别出异常事件并定位问题基站
- 通过分组聚合、透视表分析揭示工作日/周末、高峰/低谷等流量规律
- 输出专业分析报告（多维度可视化仪表板）并使用移动平均模型进行流量预测
- 技术栈：NumPy · Pandas · Matplotlib · SciPy
""")

print("=" * 70)
print("🚀 学完本套教程后，你的下一步：")
print("=" * 70)
print("""
  1. Kaggle 入门：用真实数据集做类似分析（推荐 Titanic、House Prices）
  2. 进入第二阶段：学习 scikit-learn，把「描述统计」升级为「机器学习预测」
  3. 进入第三阶段：学习 PyTorch，做深度学习项目
  
  推荐资源：
  - kaggle.com — 真实数据集 + 免费 GPU
  - github.com/jakevdp/PythonDataScienceHandbook — 进阶必读
  - pandas.pydata.org/docs — 官方文档（最权威）
""")
