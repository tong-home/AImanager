#!coding=utf-8
#!/usr/bin/python3

import unittest,pymysql,time
from datetime import datetime

# 打开数据库连接
db = pymysql.connect(host="10.204.4.7", user="root", password="ARaapCFmrkw199g", database="bw_reven_tool",charset="utf8")
# 使用 cursor() 方法创建一个游标对象 cursor
#cursor = db.cursor()
# 使用 execute()  方法执行 SQL 查询
#查询上年今天到今天内，每天客需+客控总的PV的值,用来检查room_night_pv落库是否正确
#a=cursor.execute("select count(id) from guest_requirement where hotel_id=103501 and room_night_date between '2019-03-04'and '2020-03-03'")
#data1 = cursor.fetchall()
#print(data1)

'''
class TestusageData(unittest.TestCase):
    # 打开数据库连接
    db = pymysql.connect(host="10.204.4.6:3308", user="root", password="ARaapCFmrkw199g", database="bw_reven_tool",charset="utf8")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 使用 execute()  方法执行 SQL 查询
    #查询上年今天到今天内，每天客需+客控总的PV的值,用来检查room_night_pv落库是否正确
    a=cursor.execute("select count(id) from guest_requirement where hotel_id=103501 and room_night_date between '2019-03-04'and '2020-03-03'")
    data1 = cursor.fetchall()
    print(data1)
    
    # 查询日均PV
    b = cursor.execute('select  datediff(date(now()),date_sub(date(now()),interval 1 year))')
    date3 = cursor.fetchall()
    days = date3[0][0]
    #print('相差天数为：', days + 1)
    avePV1 = sumPV / (days + 1)
    avePV = str(round(avePV1, 2))
    #print('日均PV（avePV）为：', avePV)

    ##一年中房间最大PV
    c = cursor.execute(
        "select sum(a.he),a.room_no from (SELECT count(DISTINCT(requirement_id)) AS 'he',room_no FROM guest_requirement WHERE hotel_id = '101661'AND room_night_date BETWEEN DATE_SUB(date(now()), INTERVAL 1 YEAR)AND date(now()) GROUP BY room_no UNION ALL SELECT count(distinct(control_id)),room_no FROM guest_control WHERE hotel_id = '101661'AND room_night_date BETWEEN DATE_SUB(date(now()), INTERVAL 1 YEAR)AND date(now())GROUP BY room_no)a group by a.room_no order by sum(a.he) desc limit 1")
    date4 = cursor.fetchall()
    maxPV = int(date4[0][0])
    #print('一年中房间最大maxPV为：', maxPV)
    
    ###获取今天时间并转化为时间戳
    p = cursor.execute("select date(now())")
    data5 = cursor.fetchall()
    time1 = data5[0][0]
    time2 = time1.strftime('%Y%m%d')
    time1Array = time.strptime(time2, "%Y%m%d")
    end = int(time.mktime(time1Array)) * 1000
    #print('今天时间戳', end)

    ###获取上一年的今天并转化为时间戳
    p = cursor.execute("select date_sub(date(now()),interval 1 year)")
    data5 = cursor.fetchall()
    time1 = data5[0][0]
    time2 = time1.strftime('%Y%m%d')
    time1Array = time.strptime(time2, "%Y%m%d")
    start = int(time.mktime(time1Array)) * 1000
    #print('上一年的今天时间戳', start)

    # 关闭数据库连接
    db.close()

    def test_usageData(self):
        start=self.start
        end=self.end
        sumPV=self.sumPV
        avePV=self.avePV
        maxPV=self.maxPV

        ###调用整体使用数据接口
        import requests, json, time
        ###获取token值###
        url = " "

        payload1 = {"loginname": " ", "password": " "}
        ###将变量输入后变成的dic形式需要转换成str形式
        payload = json.dumps(payload1)
        headers = {
            'Content-Type': "application/json",
        }
        response = requests.request("POST", url, data=payload, headers=headers)
        re = json.loads(response.text)
        try:
            ###将dict的形式转换成json后才可以取出键值
            token = re['data']['token']
            print('token值为：', token)
        except:
            print('获取token接口失败：', re)
        else:

            #整体使用数据查询一年的数据，接口返回
            url = " "

            querystring = {"fromDate": start, "toDate": end}

            payload = ""
            headers = {
                        'token': token

                    }
            response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
            res = json.loads(response.text)
            try:
                totalPV = res['data']['totalPV']
                averageDaily = res['data']['averageDaily']
                nightMaxPV = res['data']['nightMaxPV']
 
                if sumPV == totalPV:
                    print('总PV计算正确')
                    if avePV == averageDaily:
                        print('日均PV计算正确')
                        if maxPV == nightMaxPV:
                            print('房间最大PV计算正确')
                        else:
                            print('房间最大PV计算错误')
                    else:
                        print('日均PV计算错误')
                else:
                    print('总PV计算错误')
            except:
                print('整体使用数据接口失败',res)




if __name__=='__main__':
    suite=unittest.TestSuite()
    tests=[TestusageData("test_usageData")]
    suite.addTests(tests)

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
'''