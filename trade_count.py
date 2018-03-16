# -*-encoding:utf-8-*-

from xlrd import open_workbook
import matplotlib.pyplot as plt

date = []
time = []
trading_volumes = []
success_rate = []
response_time = []

day_trading_volumes = []
time_trading_volumes = 0
yesterday = ''  # 初始化为空
# total_row_number = 0
# day_number = 0

row_number = 0
# wb0 = open_workbook('D:/pycode/mathematical_modeling/appendix/January.xls')
# wb0 = open_workbook('D:/pycode/mathematical_modeling/appendix/February.xls')
# wb0 = open_workbook('D:/pycode/mathematical_modeling/appendix/March.xls')
wb0 = open_workbook('D:/pycode/mathematical_modeling/appendix/April.xls')
for s in wb0.sheets():
    for row in range(s.nrows):
        row_number += 1
print(row_number)
print('++++++++++++++++++++++++++++')

# wb = open_workbook('D:/pycode/mathematical_modeling/appendix/January.xls')
# wb = open_workbook('D:/pycode/mathematical_modeling/appendix/February.xls')
# wb = open_workbook('D:/pycode/mathematical_modeling/appendix/March.xls')
wb = open_workbook('D:/pycode/mathematical_modeling/appendix/April.xls')

for s in wb.sheets():
    print('Sheet:', s.name)
    for row in range(s.nrows):
        print('the row is:', row)
        # total_row_number += 1
        values = []
        for col in range(s.ncols):
            values.append(s.cell(row, col).value)
        print(values)  # 输出某一行数据

        if row == 0:
            date.append(values[0])  # 第一列赋值给date列表
            time.append(values[1])
            trading_volumes.append(values[2])
            success_rate.append(values[3])
            response_time.append(values[4])
            print('---------------------------------------------------')
            day_trading_volumes.append(values[2])

        else:
            # 用行来控制遍历数据
            if row == 1:
                date.append(values[0])  # 第一行做特殊处理
                yesterday = values[0]
                # print(date[1])  # 0123                # day_number = 1

            # 错误原因：total_row_number - 1 是动态变化的，错当成静态的值了
            # if row == total_row_number - 1:
            #     day_trading_volumes.append(time_trading_volumes)  # 最后一行做特殊处理
            #     print(day_trading_volumes[len(date) - 1])  # 5511943.0    # day_number = len(date) - 1

            if values[0] == yesterday:
                # print('==================')
                # print(row)
                time_trading_volumes += values[2]
                if row == row_number-1:  # 12954: # total_row_number - 1:
                    print(row)
                    print('.........................')
                    day_trading_volumes.append(time_trading_volumes)

            else:
                day_trading_volumes.append(time_trading_volumes)

                time_trading_volumes = 0  # 算完一天清零
                yesterday = values[0]  # 更新日期
                date.append(values[0])  # 添加当天日期
                time_trading_volumes = values[2]  # 当天第一笔交易量
                # 进入下一行
                if row == row_number-1:  # 12954:   # total_row_number - 1:
                    day_trading_volumes.append(time_trading_volumes)

                # date.append(values[0])   重复的日期只计算一次
                # day_trading_volumes = []  # 以列表形式呈现每一天的交易量

            # values[1] = int(values[1][:2]) * 60 + int(values[1][2:])  # 将时间统一转换成分钟
            # values[1] = int(values[1][:2]) + int(values[1][2:]) / 60.0  # 将时间统一转换成小时
            # time.append(values[1])

            # trading_volumes.append(values[2])

            # print(type(values[3]))
            # print(values[3][:-1])
            # values[3] = float(values[3][:-1]) / 100.0  # string to float  '%'的问题
            # print(values[3])
            # success_rate.append(values[3])

            # response_time.append(values[4])

# print(total_row_number)  # 12955
print('------------------------------------------')
print(len(date))  # 10 正常
print(len(day_trading_volumes))  # 12963 不正常
print('------------------------------------------')

# plt.plot(date[1:], day_trading_volumes[1:], 'go', label="January", linewidth=2)
# plt.plot(date[1:], day_trading_volumes[1:], 'go', label="February", linewidth=2)
# plt.plot(date[1:], day_trading_volumes[1:], 'go', label="March", linewidth=2)
plt.plot(date[1:], day_trading_volumes[1:], 'go', label="April", linewidth=2)
plt.legend()
plt.xlabel('date')
plt.ylabel('day_trading_volumes')
plt.show()

# 统计每天的交易量，以日期-工作量的格式用 matplotlib 画图，
# 区分工作日和非工作日
# 无监督
