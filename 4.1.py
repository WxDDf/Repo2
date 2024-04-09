
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文显示
plt.rcParams['axes.unicode_minus'] = False
# 读取数据
filename =r'C:\Users\123\Desktop\大三下\数据可视化\crimeRatesByState2005.csv'
crime = pd.read_csv(filename)
crime2 = crime[crime.state != "United States"]#过滤掉离散数据点
crime2 = crime2[crime2.state != "District of Columbia"]
# 绘制散点图
plt.figure(figsize=(8, 6))#设置了图形的大小
sns.scatterplot(x='murder', y='burglary', data=crime, color='green', marker='^')
#x 参数指定了横轴的数据列名为 'murder'，y 参数指定了纵轴的数据列名为 'burglary'，data 参数指定了使用的数据集为 crime。color 参数指定了散点的颜色为绿色，marker 参数指定了散点的形状为三角形('^')。
# 添加拟合曲线
sns.regplot(x='murder', y='burglary', data=crime, scatter=False, color='green', line_kws={'color': 'green'},lowess=True)
#color='green' 参数指定了拟合线的颜色为绿色，lowess=True 参数表示使用 loess 方法进行拟合。
plt.title('Murder vs Burglary')
plt.xlabel('谋杀案')
plt.ylabel('入室盗窃案')
plt.xlim(0, 10)
plt.ylim(0, 1200)
plt.show()
