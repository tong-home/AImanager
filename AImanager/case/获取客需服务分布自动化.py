#!coding=utf-8
#!/usr/bin/python3


import pymysql,time,unittest,requests,json,operator
from datetime import datetime

class TestserverInitiate(unittest.TestCase):
    # 打开数据库连接
    db = pymysql.connect(host="10.204.6.1", user="mobilefront", password="ARaapCFmrkw199g", database="bw_reven_tool",charset="utf8")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 使用 execute()  方法执行 SQL 查询
    #获取客需服务分布名称和数量
    a=cursor.execute("SELECT service_type name,COUNT(service_type) value FROM  guest_requirement WHERE  hotel_id = '101661' AND room_night_date between date_sub(date(now()),INTERVAL 1 year) and date(now())GROUP BY service_type")
    date1 = cursor.fetchall()

    #获取客需服务全部数量
    b=cursor.execute("select sum(a.value) from (SELECT service_type name,COUNT(service_type) value FROM  guest_requirement WHERE  hotel_id = '101661' AND room_night_date between date_sub(date(now()),INTERVAL 1 year) and date(now())GROUP BY service_type)a")
    date2= cursor.fetchall()
    he=date2[0][0]
    #print('一年中客需全部数量',he)

    ##取出元祖中的值
    i=0
    name=[]
    value=[]
    percent=[]
    #while(i<len(date1)):
    while(i<(len(date1)-1)):
        j=date1[i][0]
        name.append(j)
        k=date1[i][1]
        m=int(round(k/he*100,0))
        percent.append(m)
        value.append(int(k))
        i=i+1
    n=len(date1)-1
    j = date1[n][0]
    name.append(j)
    k = date1[n][1]
    m = int(round(100-sum(percent), 0))
    percent.append(m)
    value.append(int(k))

    #print('客需服务分布名称',name)
    #print('客需服务的数量',value)
    #print('客需占比',percent)
    ##将两个列表整理为一个字典
    me=dict(zip(name,percent))
    print('\n数据库中数据加工为字典格式的客需名称和占比:',me)

    ###获取今天时间并转化为时间戳
    p=cursor.execute("select date(now())")
    data5=cursor.fetchall()
    time1=data5[0][0]
    time2=time1.strftime('%Y%m%d')
    time1Array=time.strptime(time2,"%Y%m%d")
    end=int(time.mktime(time1Array))*1000
    #print('今天时间戳',end)

    ###获取上一年的今天并转化为时间戳
    p=cursor.execute("select date_sub(date(now()),interval 1 year)")
    data5=cursor.fetchall()
    time1=data5[0][0]
    time2=time1.strftime('%Y%m%d')
    time1Array=time.strptime(time2,"%Y%m%d")
    start=int(time.mktime(time1Array))*1000
    #print('上一年的今天时间戳',start)

    # 关闭数据库连接
    db.close()


    def test_server(self):
        start=self.start
        end=self.end
        percent=self.percent
        name=self.name
        me=self.me

        ###获取token值###
        url = "http://dv-gw.jointwisdom.cn:20667/user_platform/user/login"

        payload1 ={ "loginname":"wangmm@jointwisdom.cn",  "password":"0ebd5ea1f4806bcd1328fac894fc3b5b" }
        ###将变量输入后变成的dic形式需要转换成str形式
        #dumps是将dict转化成str格式，loads是将str转化成dict格式。
        payload=json.dumps(payload1)
        headers = {
            'Content-Type': "application/json"
            }
        response = requests.request("POST", url, data=payload, headers=headers)
        ###将str的形式转换成dict后才可以取出键值
        re=json.loads(response.text)
        try:
            token = re['data']['token']
            #print('token值为：', token)
        except:
            print('获取token接口失败：', re)
        else:
            ##调用客需服务分布的接口
            url = "http://10.204.4.7:19101/behavior/demandBehavior/distribution"
            querystring = {"fromDate":start,"toDate":end}
            payload = ""
            headers = { 'token': token}
            response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
            #print('客需服务分布接口结果为：',response.text)
            try:
                date2=json.loads(response.text)
                Name=date2['data']
                #print('客需服务名称和占比分别为：',type(Name),Name)
                i=0
                a=[]
                b=[]
                long=len(Name)

                while (i<long):
                    j=Name[i]['name']
                    k=Name[i]['value']
                    a.append(j)
                    b.append(int(k))
                    i=i+1
                apidict=dict(zip(a,b))
                print('\n接口返回内容转换为字典形式：',apidict)



            except:
                print('\n客需服务分布接口不通，报错信息为：',date2)

            else:
                if operator.eq(me,apidict)==True:
                    print('测试通过')
                else:
                    print('客需服务分布接口测试失败')


if __name__ == '__main__':
    unittest.main()
