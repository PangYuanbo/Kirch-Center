import pandas as pd
import glob
import matplotlib.pyplot as plt
# 设置文件路径模式
path = 'DATA/'  # 注意路径最后的斜杠
file_pattern = path + '*.csv'  # 匹配所有.csv文件

# 使用 glob.glob() 找到所有匹配的文件路径
file_paths = glob.glob(file_pattern)

# 打印找到的文件路径，检查是否正确
print(file_paths)
pd.set_option('display.max_columns', None)  # None意味着无限制
# 读取每个文件并将其存储在列表中
data_list = [pd.read_csv(file) for file in file_paths]
# 如果文件列表不为空，打印第一个 DataFrame 的头部
for(i, data) in enumerate(data_list):
    data['Kirsch Center Net Meter Net Energy Consumed']=data['Kirsch Center Net Meter Net Energy Consumed'].str.replace('kWh','').astype(float)
sum = 0
S_build_pd=pd.DataFrame()
Kir_sum_pd=pd.DataFrame()
Kir_sum_pd.insert(0, 'Time', 0)
Kir_sum_pd.insert(1, 'Cost', 0)
S_build_pd.insert(0, 'Time', 0)
S_build_pd.insert(1, 'Cost', 0)
for(i, data) in enumerate(data_list):
    if len(data.columns) < 5:
        data.insert(4, 'New Column', 0)  # 在第四列位置创建新列，默认值为0

    for j in range(1,len(data)):
        sum += data.iloc[j, 3]

        data.at[j, 'New Column'] = sum
    Kir_sum_pd.at[i , 'Time'] = i
    Kir_sum_pd.at[i , 'Cost'] = sum
print(Kir_sum_pd.head())
# print(data_list[20].shape)
plt.figure(figsize=(10, 5))
plt.plot(Kir_sum_pd['Time'], Kir_sum_pd['Cost'])
plt.title('Energy Consumption Over Time')
plt.xlabel('Time')
plt.ylabel('Energy (kWh)')
plt.grid(True)
plt.gca().invert_yaxis()
plt.show()