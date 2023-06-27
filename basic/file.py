

#读取文件
def read_file(filename):
    with open(filename,'r',encoding='utf-8') as f:
        content = f.read()
        return content
    
    
#写入文件
def write_file(filename,content): 
    with open(filename,'w',encoding='utf-8') as f:
        f.write(content)

def save_record(memberList,fee):
    member_number = len(memberList)
    average = float(fee)/member_number
    with open('resources/record.txt','a',encoding='utf-8') as f:
        recordList = [f'{member}:{average:.2f} \n' for member in memberList]
        f.writelines(recordList)

#新建一个文件
def create_file(filename):
    with open(filename,'w',encoding='utf-8') as f:
        f.write('')

content = read_file('resources/doc.txt')
print(f"文件内容:{content}")
new_content = content.replace('hello','hello1')
write_file('resources/doc.txt',new_content)

