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
    #获取客需服务已完成的数量
    shu=[]
    #获取客需服务取消的客需数量
    c=cursor.execute("select count(DISTINCT(requirement_id)) from guest_requirement where hotel_id=101661 and room_night_date between date_sub(date(now()),INTERVAL 1 year) and date(now())")
    date3= cursor.fetchall()
    he3=date3[0][0]
    #print('一年中全部客需数量',he3)
    shu.append(he3)

    a=cursor.execute("select count(DISTINCT(requirement_id)),status from guest_requirement where hotel_id=101661 and room_night_date between date_sub(date(now()),INTERVAL 1 year) and date(now()) and status=2")
    date1 = cursor.fetchall()
    he1 = date1[0][0]
    #print('一年中已完成状态的客需数量', he1)
    shu.append(he1)

    #获取客需服务取消的客需数量
    b=cursor.execute("select count(DISTINCT(requirement_id)),status from guest_requirement where hotel_id=101661 and room_night_date between date_sub(date(now()),INTERVAL 1 year) and date(now()) and status=3")
    date2= cursor.fetchall()
    he2=date2[0][0]
    #print('一年中取消的客需数量',he2)
    shu.append(he2)



    bi=int(round((he1+he2)/he3*100,0))
    #print('占比为：',bi)
    shu.append(bi)

    print('数据库中计算的结果',shu)


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
        bi=self.bi
        shu=self.shu


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
            ##调用客需服务完成率接口
            url = "http://10.204.4.7:19101/behavior/demandBehavior/getComplete"
            querystring = {"fromDate":start,"toDate":end}
            payload = ""
            headers = { 'token': token}
            response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
            #print('客需服务完成率接口结果为：',response.text)
            date2 = json.loads(response.text)


            try:
                list=[]
                date2=json.loads(response.text)
                allCount=date2['data']['allCount']
                list.append(allCount)
                completeCount = date2['data']['completeCount']
                list.append(completeCount)
                cancelCount = date2['data']['cancelCount']
                list.append(cancelCount)
                completeRate = date2['data']['completeRate']
                list.append(int(completeRate))
                print('\n接口返回客需服务数量及完成率：',list)


            except:
                print('\n客需服务分布接口不通，报错信息为：',date2)

            else:
                if operator.eq(shu,list)==True:
                    print('测试通过')
                else:
                    print('客需服务完成率接口测试失败')


if __name__ == '__main__':
    unittest.main()
