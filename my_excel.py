import  xlrd

workbook= xlrd.open_workbook(r'E:\zl\auto\test.xlsx')
worksheet = workbook.sheet_by_name("Sheet1")
rows = worksheet.nrows
cols = worksheet.ncols
for i in range(rows):
    for j in range(cols):
        print(worksheet.cell_value(i,j)+" ",end='')
    print()