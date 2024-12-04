import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 假设您已经有一个DataFrame df，包含从collect_results.py生成的数据
data = {
    'path': ['./datadir/429.mcf_underattack/base', './datadir/429.mcf_underattack/mech'],
    'mechanism': ['base', 'mech'],
    'workload': ['429.mcf_underattack', '429.mcf_underattack'],
    'cpu_cycles': [12780938.0, 4592826.0],
    'norm_cpu_cycles': [1.00000, 0.35935]
}

df = pd.DataFrame(data)

# 设置图形风格
sns.set(style="whitegrid")

# 创建一个柱状图
plt.figure(figsize=(10, 6))
sns.barplot(x='mechanism', y='cpu_cycles', data=df, palette='viridis')

# 添加标题和标签
plt.title('CPU Cycles Comparison')
plt.xlabel('Mechanism')
plt.ylabel('CPU Cycles')

# 显示图表
plt.tight_layout()
plt.show()