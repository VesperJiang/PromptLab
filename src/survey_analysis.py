# This script was generated with the assistance of DeepSeek AI.
# All data used in this script comes from our own survey (30 responses).
# Charts are based on real data collected by the author.

import pandas as pd
import matplotlib.pyplot as plt
import os

# 设置中文字体（Windows）
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

# 创建输出目录
os.makedirs('docs/images', exist_ok=True)

# 从 CSV 读取数据
df = pd.read_csv('data/survey_results.csv', encoding='utf-8')

# 提取各题数据（根据你的问卷结果手动整理）
ai_usage = {'经常使用': 26, '偶尔使用': 4}
difficulty = {'非常困难': 2, '有一定困难': 10, '一般': 12, '比较轻松': 4, '很轻松': 2}
pain_points = {'任务描述太模糊': 17, '没有指定输出格式': 16, 'AI回答太泛泛': 15, '没有设定角色': 11, '缺少约束条件': 11}
features = {'自动优化': 22, '自动诊断': 19, '模板库': 16, '保存历史版本': 11, '给Prompt打分': 9}
willingness = {'非常愿意': 15, '比较愿意': 11, '一般': 4}

# ===== 图1：AI使用频率（饼图）=====
fig1, ax1 = plt.subplots(figsize=(7, 5))
ax1.pie(ai_usage.values(), labels=ai_usage.keys(), autopct='%1.1f%%', 
        colors=['#4CAF50', '#FFC107'])
ax1.set_title('AI工具使用频率')
plt.savefig('docs/images/ai_usage.png', dpi=150, bbox_inches='tight')
plt.close()

# ===== 图2：Prompt写作困难程度（柱状图）=====
fig2, ax2 = plt.subplots(figsize=(8, 5))
colors = ['#F44336', '#FF9800', '#FFC107', '#8BC34A', '#4CAF50']
bars = ax2.bar(difficulty.keys(), difficulty.values(), color=colors)
ax2.set_title('写Prompt困难程度')
ax2.set_ylabel('人数')
for bar, val in zip(bars, difficulty.values()):
    ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.2, 
             str(val), ha='center')
plt.savefig('docs/images/difficulty.png', dpi=150, bbox_inches='tight')
plt.close()

# ===== 图3：用户痛点分布（柱状图）=====
fig3, ax3 = plt.subplots(figsize=(9, 5))
colors = ['#F44336', '#FF9800', '#FFC107', '#8BC34A', '#4CAF50']
bars = ax3.bar(pain_points.keys(), pain_points.values(), color=colors)
ax3.set_title('用户遇到的Prompt写作问题（可多选）')
ax3.set_ylabel('人数')
ax3.set_xticklabels(pain_points.keys(), rotation=15, ha='right')
for bar, val in zip(bars, pain_points.values()):
    ax3.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.2, 
             str(val), ha='center')
plt.tight_layout()
plt.savefig('docs/images/pain_points.png', dpi=150, bbox_inches='tight')
plt.close()

# ===== 图4：最想要的功能（柱状图）=====
fig4, ax4 = plt.subplots(figsize=(9, 5))
colors = ['#2196F3', '#3F51B5', '#009688', '#FF9800', '#F44336']
bars = ax4.bar(features.keys(), features.values(), color=colors)
ax4.set_title('用户最想要的Prompt工具功能（可多选）')
ax4.set_ylabel('人数')
ax4.set_xticklabels(features.keys(), rotation=15, ha='right')
for bar, val in zip(bars, features.values()):
    ax4.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.2, 
             str(val), ha='center')
plt.tight_layout()
plt.savefig('docs/images/features.png', dpi=150, bbox_inches='tight')
plt.close()

# ===== 图5：使用意愿（饼图）=====
fig5, ax5 = plt.subplots(figsize=(7, 5))
ax5.pie(willingness.values(), labels=willingness.keys(), autopct='%1.1f%%',
        colors=['#4CAF50', '#8BC34A', '#FFC107'])
ax5.set_title('是否愿意使用PromptLab')
plt.savefig('docs/images/willingness.png', dpi=150, bbox_inches='tight')
plt.close()

print("✅ 所有图表已生成，保存在 docs/images/ 目录下：")
print("  - ai_usage.png")
print("  - difficulty.png")
print("  - pain_points.png")
print("  - features.png")
print("  - willingness.png")