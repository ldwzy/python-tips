#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, re
        
'''在给定的目录即其下层目录中查找包含给定字符串的文件，返回以路径为键，文件名为值的字典
   如有必要,可以修改代码设置需要跳过的目录,
   注意os.path.join()函数在路径或文件判断中的使用必要性。        
'''
def find_file(file_str, dir_name):     
    file_path = {} 
    for x in os.listdir(dir_name): 
        if os.path.isfile(os.path.join(dir_name, x)):
            if re.search(file_str, x):
                #print(x)
                file_path[dir_name] = x
        else:
            if x.startswith('$') or x.startswith('System'):
                continue
            file_path.update(find_file(file_str, os.path.join(dir_name, x)))        
    return file_path
    
    
def test():
    with open('./gbk.txt', 'r', encoding='gbk', errors='ignore') as f:
        print(f.read())

        
import pickle

'''
close()很重要,如果是执行操作将已序列化或JSON对象写入文本，但未执行close()，又从其他模块直接读了文件，则可能文件实际并未保存而出差
'''
def pickle_test():
    d = dict(name='Bob', age=20, score=88)
    f = open('dump.txt', 'wb')
    pickle.dump(d, f)
    f.close()
    
    f2 = open('dump.txt', 'rb')
    e = pickle.load(f2)
    f2.close()
    print(e)
   
   
import json
    
def test_json():             
    d = dict(name='Bob', age=20, score=88)
    print(json.dumps(d))
    
    json_str = '{"age":20, "score":88, "name":"Bob"}'
  
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }        
    
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])
    
def main():
    
    #for path_str, name_str in find_file('space', 'd:\\').items():
    #    print(path_str, name_str)
    #pickle_test()
    #test_json()
    s = Student('Bob', 20, 88)
    print(json.dumps(s, default=student2dict))
    print(json.dumps(s, default=lambda obj: obj.__dict__))
    
    json_str = '{"age": 20, "score": 88, "name": "Bob"}'
    print(json.loads(json_str, object_hook=dict2student))
    
    obj = dict(name='小明', age=20)
    s = json.dumps(obj, ensure_ascii=True)
    print(s)
    
    
if __name__ == '__main__':
    main()   