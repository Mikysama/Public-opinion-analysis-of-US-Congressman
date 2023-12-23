import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import MultiLabelBinarizer
from textblob import TextBlob
import matplotlib.pyplot as plt
import seaborn as sns

# 加载数据
data = pd.read_excel('数据.xlsx')
boundary = 40

# 分割训练集和测试集
train_data = data.iloc[:boundary]
test_data = data.iloc[boundary:]

# 处理数据的函数
def process_data(data, mlb):
    # 合并文本列
    text_columns = data.iloc[:, 2:27]
    text_columns_filled = text_columns.fillna('')
    combined_texts = text_columns_filled.apply(lambda x: ' '.join(x), axis=1)

    # 情感分析
    sentiments = combined_texts.apply(lambda text: TextBlob(text).sentiment.polarity)
    sentiments_reshaped = sentiments.values.reshape(-1, 1)

    # Facebook关注数据处理
    facebook_follows = data['关注'].fillna('')
    facebook_follows_split = facebook_follows.apply(lambda x: x.split(',') if x else [])
    follows_matrix = mlb.transform(facebook_follows_split)

    # 结合情感和关注数据
    combined_data = np.hstack((follows_matrix, sentiments_reshaped))

    return combined_data, sentiments, data['姓名']

# 在整个数据集上拟合MultiLabelBinarizer
mlb = MultiLabelBinarizer() #label
all_follows = data['关注'].fillna('').apply(lambda x: x.split(',') if x else [])
mlb.fit(all_follows)

# 使用函数处理训练集和测试集
train_combined_data, train_sentiments, train_names = process_data(train_data, mlb)
test_combined_data, test_sentiments, test_names = process_data(test_data, mlb)

# 训练KMeans模型
kmeans = KMeans(n_clusters=10, random_state=42)
kmeans.fit(train_combined_data)
train_clusters = kmeans.predict(train_combined_data)

kmeans = KMeans(n_clusters=10, random_state=42)
kmeans.fit(test_combined_data)
test_clusters = kmeans.predict(test_combined_data)

# 创建绘图数据
train_plot_data = pd.DataFrame({'Name': train_names, 'Sentiment': train_sentiments, 'Cluster': train_clusters})
test_plot_data = pd.DataFrame({'Name': test_names, 'Sentiment': test_sentiments, 'Cluster': test_clusters})

# 绘制训练集的聚类结果
plt.figure(figsize=(20, 30))
sns.scatterplot(x='Sentiment', y='Name', hue='Cluster', data=train_plot_data, palette='viridis', s=100)
for line in range(train_plot_data.shape[0]):
    plt.text(train_plot_data['Sentiment'][line] + 0.01, line, train_plot_data['Name'][line], 
             horizontalalignment='left', size='medium', color='black', weight='semibold')
plt.title('Training Set Clustering Based on Facebook Follows and Sentiment')
plt.xlabel('Sentiment Polarity')
plt.ylabel('Individual')

# 绘制测试集的聚类结果
# 对于测试集，确保 y 值是连续的数字序列，并在绘图时使用它们作为 y 轴的值
plt.figure(figsize=(20, 30))
sns.scatterplot(x='Sentiment', y=np.arange(test_plot_data.shape[0]), hue='Cluster', data=test_plot_data, palette='viridis', s=100)
for idx, row in test_plot_data.iterrows():
    plt.text(row['Sentiment'] + 0.01, idx-boundary, row['Name'], horizontalalignment='left', size='small', color='black', weight='semibold')
plt.yticks(np.arange(test_plot_data.shape[0]), test_plot_data['Name'])
plt.title('Test Set Clustering Based on Facebook Follows and Sentiment')
plt.xlabel('Sentiment Polarity')
plt.ylabel('Individual')
plt.show()

print(test_names)
print(train_names)