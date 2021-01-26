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
    #获取客需服务时间分布
    a=cursor.execute("select time_quantum,count(distinct(requirement_id)) from guest_requirement where hotel_id='101661' and room_night_date between date_sub(date(now()),interval 1 year) and date(now()) group by time_quantum order by time_quantum")
    date1 = cursor.fetchall()
    #print("一年内客需服务时间分布类型%S内容%S\n" ,type(date1),date1)
    ##取出元祖中的值
    #a=date1[0][1]
    #print(type(a),len(date1),a)
    xulist=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    #print(len(xulist))
    i=0
    #while(i<len(date1)):
    while(i<len(date1)):
        j=date1[i][0]
        value=date1[i][1]
        xulist[j]=value
        i=i+1
    #print(xulist)



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
        xulist=self.xulist

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
            ##调用客需使用时段分布的接口
            url = "http://10.204.4.7:19101/behavior/demandBehavior/serverInitiate"
            querystring = {"fromDate":start,"toDate":end}
            payload = ""
            headers = { 'token': token}
            response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
            #print(response.text)
            try:
                date2=json.loads(response.text)
                time=date2['data']
                #print(type(time),time)
                #print(type(operator.eq(xulist, time)),operator.eq(xulist, time))
            except:
                print('客需使用时段分布接口不通',date2)
            else:
                if operator.eq(xulist,time)==True:
                    print ('测试通过')
                else:
                    print('测试失败')

if __name__=='__main__':
    suite=unittest.TestSuite()
    tests=[TestserverInitiate("test_server")]
    suite.addTests(tests)

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
