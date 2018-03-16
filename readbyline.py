# -*-encoding:utf-8-*-

from xlrd import open_workbook
import matplotlib.pyplot as plt
date = []
time = []
trading_volumes = []
success_rate = []
response_time = []
wb = open_workbook('D:/pycode/mathematical_modeling/appendix/January.xls')
for s in wb.sheets():
    print('Sheet:', s.name)
    for row in range(s.nrows):
        print('the row is:', row)
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

        else:
            date.append(values[0])

            # values[1] = int(values[1][:2]) * 60 + int(values[1][2:])  # 将时间统一转换成分钟
            values[1] = int(values[1][:2]) + int(values[1][2:]) / 60.0  # 将时间统一转换成小时
            time.append(values[1])

            trading_volumes.append(values[2])

            print(type(values[3]))
            print(values[3][:-1])
            values[3] = float(values[3][:-1]) / 100.0  # string to float  '%'的问题
            success_rate.append(values[3])

            response_time.append(values[4])


            # plt.plot(time[1: ], trading_volumes[1: ], 'g--', label="January", linewidth=2)
            # plt.xlabel('time(minutes)')
            # plt.ylabel('trading_volumes')
            # plt.show()
            # row_number = 0
            # if values == '0123':
            #     row_number += 1
            #     date.append(values[0])
            #
            # if values == '0124':
            #     date.append(values[0])
            # else:




        # if row == 0:
        #     time.append(values[1])
        # else:
        #     values[1] = int(values[1][:2]) * 60 + int(values[1][2:])  # 将时间统一转换成分钟
        #     time.append(values[1])
        # print(values[1])
        # print(type(values[1][1]))  # str






# plt.plot(time[1:], trading_volumes[1:], 'g--', label="January", linewidth=2)
# plt.legend()
# plt.xlabel('time(hours)')
# plt.ylabel('trading_volumes')
# plt.show()

plt.plot(trading_volumes[1:], success_rate[1:], 'g.', label="January", linewidth=2)
plt.legend()
plt.xlabel('trading_volumes')
plt.ylabel('success_rate')
plt.show()

# 统计每天的交易量，区分工作日和非工作日
# 
# 无监督
