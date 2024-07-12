import matplotlib.pyplot as plt
import numpy as np

# 定义步骤
steps = ["见识", "学习", "实践", "思考", "分享", "交流", "练习", "反馈", "创造"]
num_steps = len(steps)

# 生成每个节点的角度
angles = np.linspace(0, 2 * np.pi, num_steps, endpoint=False).tolist()
angles += angles[:1]  # 闭合环形

# 设置极坐标图
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
ax.set_theta_direction(-1)
ax.set_theta_offset(np.pi / 2.0)

# 绘制节点和双向箭头
for i in range(num_steps):
    angle = angles[i]
    next_angle = angles[(i + 1) % num_steps]
    
    # 添加节点位置标记
    ax.plot([angle], [1.1], marker='o', markersize=10, color='skyblue')
    
    # 添加双向箭头
    ax.annotate("",
                xy=(next_angle, 1),
                xytext=(angle, 1),
                arrowprops=dict(arrowstyle="<->", color='black', lw=2))

# 隐藏极坐标的圆圈
ax.set_frame_on(False)
ax.set_yticklabels([])
ax.set_xticks([])

# 设置标题
plt.title("认知模型环形循环图", va='bottom', fontsize=16)
plt.show()
