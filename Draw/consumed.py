import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt

# 读取CSV文件


# 读取CSV文件
data = pd.read_csv('../DATA/1.csv')

# 清理时间戳列，只保留日期和时间部分
data['Timestamp'] = data['Timestamp'].str.split(' ').str[0]

# 转换为日期时间格式，指定格式以确保正确解析
data['Timestamp'] = pd.to_datetime(data['Timestamp'], format='%Y-%m-%dT%H:%M:%S%z', utc=True)

# 设置时间戳为索引
data.set_index('Timestamp', inplace=True)

# 输出数据查看是否正确
print(data.head())



# 绘制数据
plt.figure(figsize=(10, 5))
plt.plot(data.index, data['Kirsch Center Net Meter Net Energy Consumed'])
plt.title('Energy Consumption Over Time')
plt.xlabel('Time')
plt.ylabel('Energy (kWh)')
plt.grid(True)
plt.gca().invert_yaxis()
plt.show()
