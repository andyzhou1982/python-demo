import xlrd

#读取excel文件
def read_excel(file_name):
    workbook = xlrd.open_workbook(file_name)
    return workbook

#获取sheet的名称
def get_sheet_name(file_name):
    workbook = read_excel(file_name)
    return workbook.sheet_names()


workbook = read_excel('./resources/income.xlsx')
sheet = workbook.sheet_by_index(0)
incomes = sheet.col_values(colx=1,start_rowx=1)
print(f"包含表单数量 {workbook.nsheets}")
print(f"表单的名分别为: {workbook.sheet_names()}")
print(f"2018年总收入为： {sum(incomes)}")