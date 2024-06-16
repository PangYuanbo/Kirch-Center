import pandas as pd
import glob
import matplotlib.pyplot as plt
import os
gas_fee=1.9
electricity_fee=0.3
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
sum = 0
for(i, data) in enumerate(data_list):
    if len(data.columns) < 5:
        data.insert(4, 'New Column', 0)  # 在第四列位置创建新列，默认值为0

    for j in range(1,len(data)):
        sum += data.iloc[j, 3]

        data.at[j, 'New Column'] = sum
    Kir_sum_pd.at[i , 'Time'] = i
    Kir_sum_pd.at[i , 'Cost'] = sum*electricity_fee

for(i, data) in enumerate(data_list):
    if len(data.columns) < 5:
        data.insert(4, 'New Column', 0)  # 在第四列位置创建新列，默认值为0


    S_build_pd.at[i , 'Time'] = i
    print(data.iloc[98, 2])
    S_build_pd.at[i , 'Cost'] = (data.iloc[98, 2] - intial)*gas_fee

# print(data_list[20].shape)
# 创建图形
plt.figure(figsize=(10, 5))

# 绘制 GAS 曲线
plt.plot(S_build_pd['Time'], S_build_pd['Cost'], label='S buildings_GAS', color='red')

# 绘制 Electricity 曲线
plt.plot(Kir_sum_pd['Time'], Kir_sum_pd['Cost'], label='Kirch Center Electricity', color='blue')

# 标记 GAS 曲线的最后一个点
plt.annotate(f'({S_build_pd["Time"].iloc[-1]}, ${S_build_pd["Cost"].iloc[-1]})',
             xy=(S_build_pd['Time'].iloc[-1], S_build_pd['Cost'].iloc[-1]),
             xytext=(S_build_pd['Time'].iloc[-1], S_build_pd['Cost'].iloc[-1] + 2),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=9)

# 标记 Electricity 曲线的最后一个点
plt.annotate(f'({Kir_sum_pd["Time"].iloc[-1]}, ${Kir_sum_pd["Cost"].iloc[-1]})',
             xy=(Kir_sum_pd['Time'].iloc[-1], Kir_sum_pd['Cost'].iloc[-1]),
             xytext=(Kir_sum_pd['Time'].iloc[-1], Kir_sum_pd['Cost'].iloc[-1] + 2),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=9)

# 添加标题和标签
plt.title('April Energy Consumption fee (GAS and Electricity)')
plt.xlabel('Date')
plt.ylabel('Energy Cost ($)')

# 显示图例
plt.legend()

# 显示网格
plt.grid(True)

# 显示图形
plt.show()