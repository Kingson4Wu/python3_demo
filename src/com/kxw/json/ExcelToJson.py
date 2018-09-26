# -*- coding: utf-8 -*-

import xlrd

excelFile = xlrd.open_workbook(r'西安-公交站.xlsx')


def read03Excel(path):
    workbook = xlrd.open_workbook(path)
    sheets = workbook.sheet_names()
    worksheet = workbook.sheet_by_name(sheets[0])
    for i in range(1, worksheet.nrows):
        row = worksheet.row(i)
        strr = "";
        #for j in range(2, len(row)):
            # print(worksheet.cell_value(i, j), "\t", end="")
            # print("var marker" + str(i) + " = new BMap.Marker(new BMap.Point(" + worksheet.cell_value(i, j) + "), { icon: tagMarkerIcon });", "\t",end="")
            # print("var label" + str(i) + " = new BMap.Label(\""+  worksheet.cell_value(i, j) + "\", { offset: new BMap.Size(-15, 2) });", "\t", end="")
            # print("map.addOverlay(marker" + str(i) + ");", "\t", end="")
            #strr = strr + worksheet.cell_value(i, j);
            #print("function renderItem"+ str((i+1))+"(params, api) {return renderItemAll(coordss[" +str(i)+"],params, api);}")
        #print("function renderItem"+ str((i+1))+"(params, api) {return renderItemAll(coordss[" +str(i)+"],params, api);}")
        #print(str(i)+"["+strr.replace("(", "[").replace(")", "]")+"],")
        #print("\""+worksheet.cell_value(i, 0)+ "\":["+ worksheet.cell_value(i, 1)+"],")
        #print("\""+worksheet.cell_value(i, 1)+"\":["+worksheet.cell_value(i, 2)+","+worksheet.cell_value(i, 3)+"],")
        print("{name: '" + worksheet.cell_value(i, 1)+"',value: Math.round(Math.random()*1000)},")


read03Excel("西安-公交站.xlsx")
