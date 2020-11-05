import xlrd
import xlwt
import time
import os

def read_excel():
    file_name=input('请输入要读取的文件名:')
    try:
        workbook=xlrd.open_workbook(filename=os.path.join('./file/',file_name))
    except:
        print('文件找不到,5s后自动退出')
        time.sleep(5)
        exit(0)

    result = xlwt.Workbook() #创建xlsx文件
    sheet = result.add_sheet('result', cell_overwrite_ok=True)  # 表名为result

    # 获取工作表
    table = workbook.sheets()[0]

    content=[]
    for i in range(0,table.nrows):
        content.append(table.row_values(i))

    print(content)
    time.sleep(1)
    return content

if __name__=='__main__':
    content=read_excel()
    for item in content:
        print(item[4])