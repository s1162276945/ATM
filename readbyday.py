# encodin:utf-8

from xlrd import open_workbook
import matplotlib.pyplot as plt
date = []
time = []
trading_volumes = []
success_rate = []
response_time = []
# yesterday = ''
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
            print('---------------------------------------------------')

        else:
            values[1] = int(values[1][:2]) + int(values[1][2:]) / 60.0  # 将时间统一转换成小时
            time.append(values[1])

        yesterday = '0123'  # 如果有 bug ，看看初始化的位置是否正确
        start_row_number = 1
        end_row_number = 0
        row_number = 0

        if values[0] != yesterday:
            row_number += 1
            end_row_number = row_number
            plt.plot(time[start_row_number: end_row_number],
                     trading_volumes[start_row_number:end_row_number],
                     'g--', label=yesterday, linewidth=2)
            plt.legend()  # 显示 label="January23"
            plt.xlabel('time(hours)')
            plt.ylabel('trading_volumes')
            plt.show()

            yesterday = values[0]
            date.append(values[0])
            start_row_number = end_row_number


        # values[0] == yesterday
        else:
            row_number += 1
            start_row_number = start_row_number
            date.append(values[0])



        trading_volumes.append(values[2])
        success_rate.append(values[3])
        response_time.append(values[4])


# plt.plot(time[1: 1441], trading_volumes[1:1441], 'g--', label="January23", linewidth=2)
# plt.legend()  # 显示 label="January23"
# plt.xlabel('time(minutes)')
# plt.ylabel('trading_volumes')
# plt.show()


