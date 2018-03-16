# -*-encoding:utf-8 -*-

# from xlrd import open_workbook
# x_data1 = []
# y_data1 = []
# # 打开 excel 文件
# wb = open_workbook('../phase_detector.xlsx')
# # 打开一个excel文件后，首先对文件内的sheet进行循环，一个excel文件可能含有多个sheet
# for s in wb.sheets():
#     print('Sheet:', s.name)
#     # 行遍历
#     for row in range(s.nrows):
#         print('the row is:', row)
#         values = []
#         # 列遍历
#         for col in range(s.ncols):
#             values.append(s.cell(row, col).value)
#         print(values)
#         x_data1.append(values[0])
#         y_data1.append(values[1])

# ---------------------------------
import xlrd
from xlrd import open_workbook
import matplotlib.pyplot as plt

x_data = []
y_data = []
temp = []
wb = open_workbook('../my_data.xlsx')

for s in wb.sheets():
    print('Sheet:', s.name)
    for row in range(s.nrows):
        print('the row is:', row)
        values = []
        for col in range(s.ncols):
            values.append(s.cell(row, col).value)
        print(values)
        x_data.append(values[0])
        y_data.append(values[1])
# Phase curve 相位曲线
plt.plot(x_data, y_data, 'bo-', label='Phase curve', linewidth=1)

plt.annotate('zero point', xy=(180, 0), xytext=(80, 3),
             arrowprops=dict(facecolor='red', shrink=0.1),)  # 箭头指向
# xy表示的是坐标点，xytext是显示'zero point'的坐标位置

# 显示图内标签
plt.title('TR14 phase detector')
plt.legend()  # 控制图内标签显示label='Phase curve'


# ----优化图像在坐标中的显示----
from pylab import *
ax = gca()
ax.spines['right'].set_color('none')  # 拆右边界
ax.spines['top'].set_color('none')  # 拆上边界
ax.xaxis.set_ticks_position('bottom')  # 移动 x 轴
ax.spines['bottom'].set_position(('data', 0))  # 设置0点
ax.yaxis.set_ticks_position('left')  # 移动 y 轴
ax.spines['left'].set_position(('data', 0))  # 设置0点
# ------------坐标轴美化结束------------------

plt.xlabel('input-deg')
plt.ylabel('output-V')
plt.show()




