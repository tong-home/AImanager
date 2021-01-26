#coding:utf-8
#************************
#author：wmm
#date：2019-7-5
#如果有内容为空的内容，手动添加为标准格式的内容
#因为服务类和送物类的测试用例接口返回的结果不同，因此需要按照类型进行分类
#*************************
import xlrd,json
#workbook=xlrd.open_workbook(r'C:\Users\admin\Documents\WeChat Files\wangmingming3147\FileStorage\File\2019-07\众荟测试-asr&nlu_v2.xlsx')
workbook=xlrd.open_workbook(r'C:\Users\admin\Desktop\众荟测试-结果分析.xls')


##service服务
'''
sheetname=workbook.sheet_by_name('Sheet2')
#a=sheetname.cell(2,1).value.encode('utf-8')
i=1
while(i<57):
    a = sheetname.cell(i,9).value.encode('utf-8')
    #print(a)
    #print(type(a),a)
    b=str(a, encoding="utf-8")
    #print(type(b))
    re = json.loads(b)
    print(re['semantic']['intent']['tag'])
    i = i + 1

    #print(a['semantic']['intent'])
print('jieshu')
'''

##goods服务
sheetname=workbook.sheet_by_name('Sheet3')
i=1
while(i<112):
    a = sheetname.cell(i,9).value.encode('utf-8')
    #print(a)
    #print(type(a),a)
    b=str(a, encoding="utf-8")
    #print(type(b))
    re = json.loads(b)
    print(re['semantic']['intent']['name'])
    i = i + 1

    #print(a['semantic']['intent'])
print('jieshu')