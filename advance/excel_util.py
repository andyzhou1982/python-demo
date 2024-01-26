import xlrd
import xlwt

class NumberObject:
    def __init__(self,num,seq):
        self.num = num
        self.seq = seq

#读取excel文件
def read_excel(file_name):
    workbook = xlrd.open_workbook(file_name)
    return workbook

#获取sheet的名称
def get_sheet_name(file_name):
    workbook = read_excel(file_name)
    return workbook.sheet_names()


workbook = read_excel('./resources/difference.xlsx')
sheetA = workbook.sheet_by_index(1)

wb = xlwt.Workbook()
results = wb.add_sheet('results')


sheetB = workbook.sheet_by_index(2)
numListB = sheetB.col_values(colx=0,start_rowx=1)
seqListB = sheetB.col_values(colx=6,start_rowx=1)
if(len(numListB)!=len(seqListB)):
    raise SystemError('数量不一致')
numberList:list[NumberObject]=[]
for i in range(len(numListB)):
    numberList.append(NumberObject(numListB[i],str(seqListB[i])))


#获取第二列的数据
seqListA = sheetA.col_values(colx=1,start_rowx=2)
for i in range(len(seqListA)):
    #print(f"seqListA[i]={seqListA[i]}")
    tmpstr = ""
    y = list(filter(lambda x: x.seq==str(seqListA[i]),numberList))
    for j in range(len(y)):
        tmpstr += (y[j].num+",")
    tmpstr = tmpstr[:-1]
    #print(f"tmpstr={tmpstr}")
    results.write(i, 0, tmpstr)
    
wb.save('./resources/results.xlsx')

'''
workbook = read_excel('./resources/FP.xlsx')
sheet = workbook.sheet_by_index(0)
incomes = sheet.col_values(colx=1,start_rowx=1)
print(f"包含表单数量 {workbook.nsheets}")
print(f"表单的名分别为: {workbook.sheet_names()}")
print(f"2018年总收入为： {sum(incomes)}")
'''