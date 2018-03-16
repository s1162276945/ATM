import os


def downloadData():
    data_url = 'http://labfile.oss.aliyuncs.com/courses/791'
    for filename in ('finally.py', 'my_data.xlsx', 'phase_detector.xlsx', 'phase_detector2.xlsx'):
        if not os.path.exists(filename):
            os.system("wget %s/%s" % (data_url, filename))

if __name__ == '__main__':
    downloadData()