
# 读取txt文件
import json
import random

def read_file(path):
    with open(path, 'r') as f:
        content = f.read()
        #根据换行符切分
        contents = content.split('\n')
        #过滤数组中的空字符串
        contents = list(filter(lambda x: x!='', contents))
        #print(f"contents={contents}")

        #将text1:text2转换为json格式
        def make_qa(question,answer):
            output_dict = {
                "question": question,
                "answer": answer,
                "history": []
            }
            for content in random.sample(contents, 5):
                #构建一个元组
                element = (content.split(':')[0],content.split(':')[1])
                output_dict.get("history").append(element)
            print(f"output_dict={output_dict}")
            return output_dict
        
        json_list = []
        for text in contents:
            split_str = text.split(':')
            json_list.append(make_qa(split_str[0],split_str[1]))
        print(f"json_list={json_list}")
    return json_list


def save_as_json(json_list, path):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(json_list, f, ensure_ascii=False, indent=4)

json_list = read_file('resources/omioji.txt')
save_as_json(json_list, 'resources/omioji.json')
