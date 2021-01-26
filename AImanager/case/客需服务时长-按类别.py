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

    ###获取今天时间并转化为时间戳
    p = cursor.execute("select date(now())")
    data5 = cursor.fetchall()
    time1 = data5[0][0]
    time2 = time1.strftime('%Y%m%d')
    time1Array = time.strptime(time2, "%Y%m%d")
    end = int(time.mktime(time1Array)) * 1000
    print('今天时间戳',end)

    ###获取上一年的今天并转化为时间戳
    p = cursor.execute("select date_sub(date(now()),interval 1 year)")
    data5 = cursor.fetchall()
    time1 = data5[0][0]
    time2 = time1.strftime('%Y%m%d')
    time1Array = time.strptime(time2, "%Y%m%d")
    start = int(time.mktime(time1Array)) * 1000
    print('上一年的今天时间戳',start)

    #服务时长--按类别统计
    a=cursor.execute("SELECT g.service_type,max(TIMESTAMPDIFF(SECOND,g.req_cmd_time,g.service_finished_time)),round(avg(TIMESTAMPDIFF(SECOND,g.req_cmd_time,g.service_finished_time)),0)FROM (SELECT DISTINCT(requirement_id),`status`,hotel_id,room_night_date,IF(service_type like '%打扫%','打扫服务',IF(service_type like '%洗衣%','洗衣服务',service_type)) service_type,req_cmd_time,service_finished_time FROM guest_requirement WHERE hotel_id='101661' AND `status`in(2,3) AND room_night_date BETWEEN DATE_sub(date(now()),INTERVAL 1 year)AND date(now())) g GROUP BY g.service_type ORDER BY CASE WHEN g.service_type='日耗品' THEN 1 WHEN g.service_type='借用物品' THEN 2 WHEN g.service_type='打扫服务' THEN 3 WHEN g.service_type='洗衣服务' THEN 4 ELSE 5 END")
    date1= cursor.fetchall()
    print("服务时长-按类别统计类型%S内容%S\n" ,type(date1),date1)

    ##取出元祖中的值
    i=0
    long=len(date1)
    type=[]
    max=[]
    ave=[]
    #将楼号和楼层用-进行连接，并放到num列表中
    while(i<long):
        time = []
        lis=list(date1[i])
        m="%s"%(lis[0])
        type.append(m)
        ##将服务最长时长换算成分钟并保存到num列表中
        j=int(lis[1])
        value1=round(j/60,1)
        #print('\n',type(value1),value1)
        if value1>int(value1):
            value1=int(value1)+1
            lis[1] = value1
            max.append(value1)
        else:
            value1 = int(value1)
            lis[1] = value1
            max.append(value1)
        ##将服务平均时长换算成分钟并保存为num列表中
        k=int(lis[2])
        value2=round(k/60,1)
        if value2>int(value2):
            value2=int(value2)+1
            lis[2] = value2
            ave.append(value2)
        else:
            value2 = int(value2)
            lis[2] = value2
            ave.append(value2)
        i=i+1

    #将类别，最长服务时长，平均服务时长分别放到不同的列表中
    print('数据库中一年类型列表为：',type)
    print('数据库中一年最长服务时长为：',max)
    print('数据库中一年平均服务时长为：',ave)

    # 关闭数据库连接
    db.close()

    def test_server(self):
        start=self.start
        end=self.end
        type=self.type
        max=self.max
        ave=self.ave


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
            ##客需服务时长-楼层分布
            url = "http://10.204.4.7:19101/behavior/demandBehavior/getServiceTime"
            querystring = {"fromDate":start,"toDate":end,"type":"2"}
            payload = ""
            headers = { 'token': token}
            response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
            #print(response.text)
            date2 = json.loads(response.text)

            try:
                date2=json.loads(response.text)
                #print ('接口返回结果：',date2)
                category=date2['data']['category']
                averageServiceTime=date2['data']['averageServiceTime']
                maxServiceTime=date2['data']['maxServiceTime']
                #print('\n接口楼层',category)
                #print('\n接口平均',averageServiceTime)
                #print('\n接口最长',maxServiceTime)

            except:
                print('客需服务时长接口不通',date2)

            else:
                if operator.eq(type,category)==True:
                    if operator.eq(averageServiceTime,ave)==True:
                        if operator.eq(maxServiceTime,max)==True:
                            print('\n客需服务时长-按楼层统计的接口测试通过\n')
                        else:
                            print('\n客需服务时长-最长服务时长计算有问题\n', maxServiceTime)
                    else:
                        print('\n客需服务时长-平均服务时长返回结果有问题\n', averageServiceTime)

                else:
                    print('\n客需服务时长-按类型返回结果有问题\n', category)

if __name__ == '__main__':
    unittest.main()


