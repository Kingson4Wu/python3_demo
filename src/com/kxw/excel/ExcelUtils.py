# -*- coding: utf-8 -*-

import xlrd

a = set()
b = set()


def read03Excel(path):
    workbook = xlrd.open_workbook(path)
    sheets = workbook.sheet_names()
    worksheet = workbook.sheet_by_name(sheets[0])
    for i in range(1, worksheet.nrows):
        a.add(worksheet.cell_value(i, 1))


def read04Excel(path):
    workbook = xlrd.open_workbook(path)
    sheets = workbook.sheet_names()
    worksheet = workbook.sheet_by_name(sheets[0])
    for i in range(1, worksheet.nrows):
        b.add(worksheet.cell_value(i, 0))
        # if worksheet.cell_value(i, 0) not in a:
        # print(str(worksheet.cell_value(i, 0) + "|", end=' '))


read03Excel("/Users/kingsonwu/Downloads/part1.xlsx")
read03Excel("/Users/kingsonwu/Downloads/part2.xlsx")
read03Excel("/Users/kingsonwu/Downloads/part3.xlsx")
read03Excel("/Users/kingsonwu/Downloads/part4.xlsx")
read03Excel("/Users/kingsonwu/Downloads/part5.xlsx")

read04Excel(
    "/Users/kingsonwu/Downloads/xxx.xlsx")

print()

for item in a:
    if item not in b:
        print(item)
