
def read_file(path):
    with open(path, 'r',encoding='utf-8', errors='ignore') as f:
        content = f.read()
        #print(f"content={content}")
        contents = content.split("\n")
        contents = list(filter(lambda x: x!='', contents))
        contents = list(map(lambda x: x[1:], contents))
        #print(f"contents={contents}")
        return contents
    
if __name__ == '__main__':
    path = 'resources/prompts.txt'
    read_file(path)