import pandas as pd
import glob
import matplotlib.pyplot as plt
import os
# 设置文件路径模式
directory = 'DATA/'  # 注意路径最后的斜杠
file_paths = [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith('.csv')]

# 对文件名进行排序
file_paths = sorted(file_paths, key=lambda x: int(os.path.basename(x).split('_')[0]))

# 读取每个文件并将其存储在列表中
data_list = [pd.read_csv(file) for file in file_paths]

# 打印找到的文件路径，检查是否正确
print(file_paths)
pd.set_option('display.max_columns', None)  # None意味着无限制
# 读取每个文件并将其存储在列表中
data_list = [pd.read_csv(file) for file in file_paths]
# 如果文件列表不为空，打印第一个 DataFrame 的头部
for(i, data) in enumerate(data_list):
    data['Kirsch Center Net Meter Net Energy Consumed']=data['Kirsch Center Net Meter Net Energy Consumed'].str.replace('kWh','').astype(float)
    data['S6 Central Plant Gas Meter Gas Consumption'] = data[
        'S6 Central Plant Gas Meter Gas Consumption'].str.replace('hundred_cubic_feet_natural_gas', '').astype(float)
intial = data_list[0].iloc[1, 2]
print(intial)
S_build_pd=pd.DataFrame()
Kir_sum_pd=pd.DataFrame()
Kir_sum_pd.insert(0, 'Time', 0)
Kir_sum_pd.insert(1, 'Cost', 0)
S_build_pd.insert(0, 'Time', 0)
S_build_pd.insert(1, 'Cost', 0)
for(i, data) in enumerate(data_list):
    if len(data.columns) < 5:
        data.insert(4, 'New Column', 0)  # 在第四列位置创建新列，默认值为0


    Kir_sum_pd.at[i , 'Time'] = i
    print(data.iloc[98, 2])
    Kir_sum_pd.at[i , 'Cost'] = data.iloc[98, 2] - intial
print(Kir_sum_pd.head())
# print(data_list[20].shape)
plt.figure(figsize=(10, 5))
plt.plot(Kir_sum_pd['Time'], Kir_sum_pd['Cost'])
plt.title('S Buildings April Energy Consumption (Gas)')
plt.xlabel('Date')
plt.ylabel('Energy (hundred_cubic_feet_natural_gas)')
plt.grid(True)
plt.show()