# -*- coding: utf-8 -*-
import xlrd
import os
import xlwt
#import pandas as pd
#import numpy as np
from xlrd import open_workbook
from xlutils.copy import copy

execl_file = "test.xlsx"

if __name__ == "__main__":
    print(">>>>>>>Python操作execl<<<<<<<<<")
    try:
        data = xlrd.open_workbook(execl_file)
        print("[OK]Open %s success（%s）" % (execl_file,type(data)))
        #属性遍历
        #for i in dir('data'):
        #   print(i)

        #获取一个工作表,默认有三张表
        table = data.sheets()[0]
        #for i in dir(table):   #遍历对象
        #   print(i)

        #遍历整个表
        nrows = table.nrows
        ncols = table.ncols
        for i in range(nrows):
            for j in range(ncols):
                print("|",table.row_values(i)[j],end="\t"), #输出不换行
            print("|")

        #增加一行保存
        save_xsl = copy(data)
        save_xsl.get_sheet(0).write(4,0,4)
        save_xsl.get_sheet(0).write(4,1,"user4")
        save_xsl.get_sheet(0).write(4,2,"pwd4")
        save_xsl.get_sheet(0).write(4,3,"100")
        save_xsl.get_sheet(0).write(4, 4, "四")
        save_xsl.save("test_copy.xlsx")

    except Exception as e:
        print("%s" % (str(e)))
    finally:
        print(">>>End") #一定会执行到



