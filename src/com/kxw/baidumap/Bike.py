# -*- coding: utf-8 -*-

import xlrd


# excelFile = xlrd.open_workbook(r'bike.xlsx')


def read03Excel(path):
    workbook = xlrd.open_workbook(path)
    sheets = workbook.sheet_names()
    worksheet = workbook.sheet_by_name(sheets[1])
    for i in range(0, worksheet.nrows):
        row = worksheet.row(i)
        for j in range(0, len(row)):
            print(str(worksheet.cell_value(i, j)) + "|", end=' ')

        print()


read03Excel("bike.xlsx")
