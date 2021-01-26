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
    #获取已完成状态日耗品的数量,按照首字母和数量倒叙
    a=cursor.execute("SELECT sum(quantity),service_item FROM  guest_requirement WHERE  hotel_id = '101661' AND room_night_date between date_sub(date(now()),INTERVAL 1 year) and date(now())and service_type='日耗品' and status='2' group by service_item order by sum(quantity) desc,CONVERT(service_item USING gbk) limit 5")
    date1 = cursor.fetchall()
    ##取出元祖中的值
    i=0
    haoname=[]
    haonum=[]
    while(i<len(date1)):
        j=date1[i][0]
        haonum.append(int(j))
        k=date1[i][1]
        haoname.append(k)
        i=i+1
    print('日耗品前五名名称',haoname)
    print('日耗品前五名数量',haonum)



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
        haoname=self.haoname
        haonum=self.haonum

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
            url = "http://10.204.4.7:19101/behavior/demandBehavior/getGoodsStatistical"
            querystring = {"fromDate":start,"toDate":end}
            payload = ""
            headers = { 'token': token}
            response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
            #print(response.text)
            try:
                date2=json.loads(response.text)
                goodsName=date2['data']['goodsName']
                usedQuantity = date2['data']['usedQuantity']
                print(type(goodsName),goodsName)
                print(type(usedQuantity), usedQuantity)

            except:
                print('客需使用时段分布接口不通',date2)
            else:
                if operator.eq(haoname,goodsName)==True:
                    if operator.eq(haonum,usedQuantity)==True:
                        print ('日耗品统计接口测试通过')
                    else:
                        print('日耗品数量错误')
                else:
                    print('日耗品统计接口测试失败')


if __name__ == '__main__':
    unittest.main()
