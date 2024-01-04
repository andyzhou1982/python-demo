import xlrd
import xlwt

#读取excel文件
def read_excel(file_name):
    workbook = xlrd.open_workbook(file_name)
    return workbook

#获取sheet的名称
def get_sheet_name(file_name):
    workbook = read_excel(file_name)
    return workbook.sheet_names()


workbook = read_excel('./resources/FP.xlsx')
sheetA = workbook.sheet_by_index(0)

wb = xlwt.Workbook()
results = wb.add_sheet('results')

#获取第二列的数据
modListA = sheetA.col_values(colx=2,start_rowx=1)
funListA = sheetA.col_values(colx=3,start_rowx=1)
if(len(modListA)!=len(funListA)):
    raise SystemError('模块和方法数量不一致')
for i in range(len(modListA)):
    wholeWordsA = modListA[i] + ' ' + funListA[i]
    results.write(i, 0, wholeWordsA)

    #print(f'wholeWordsA={wholeWordsA}')

wb.save('./resources/results.xlsx')

'''
sheetB = workbook.sheet_by_index(1)
modListB = sheetB.col_values(colx=1,start_rowx=1)
funListB = sheetB.col_values(colx=2,start_rowx=1)
if(len(modListB)!=len(funListB)):
    raise SystemError('模块和方法数量不一致')
for i in range(len(modListB)):
    wholeWordsB = modListB[i] + ' ' + funListB[i]
    print(f'wholeWordsB={wholeWordsB}')
'''
'''
workbook = read_excel('./resources/FP.xlsx')
sheet = workbook.sheet_by_index(0)
incomes = sheet.col_values(colx=1,start_rowx=1)
print(f"包含表单数量 {workbook.nsheets}")
print(f"表单的名分别为: {workbook.sheet_names()}")
print(f"2018年总收入为： {sum(incomes)}")
'''