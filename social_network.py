import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

# 加载数据
file_path = '众议院数据.xlsx'
data = pd.read_excel(file_path)

# 获取议员列表
senators = data['姓名'].tolist()

# 创建存储关注关系的字典
following_dict = {}
for index, row in data.iterrows():
    follows = str(row['关注']).split(',')
    following_dict[row['姓名']] = follows

# 创建无向图
G_shared = nx.Graph()

# 添加节点（议员）
for senator in senators:
    G_shared.add_node(senator)

# 添加边，基于共同关注关系
for i in range(len(senators)):
    for j in range(i + 1, len(senators)):
        # 检查是否有共同关注的账户
        common_following = set(following_dict[senators[i]]) & set(following_dict[senators[j]])
        if common_following:
            # 如果有共同关注的账户，则添加边
            G_shared.add_edge(senators[i], senators[j])

# 绘制网络图
plt.figure(figsize=(15, 30))
plt.title("U.S. Representative Shared Following Network")
nx.draw(G_shared, with_labels=True, node_color='skyblue', edge_color='gray', font_size=10, node_size=1000)
plt.show()
