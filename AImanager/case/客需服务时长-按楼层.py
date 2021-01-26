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

    #服务时长--按楼层分布
    a=cursor.execute("SELECT g.building_no,g.floor_no,max(TIMESTAMPDIFF(SECOND,g.req_cmd_time,g.service_finished_time)),round(avg(TIMESTAMPDIFF(SECOND,g.req_cmd_time,g.service_finished_time)),0)FROM(SELECT DISTINCT(requirement_id),`status`,hotel_id,room_night_date,building_no,floor_no,req_cmd_time,service_finished_time FROM guest_requirement WHERE hotel_id = '101661'AND `status` in (2,3) AND room_night_date BETWEEN DATE_sub(date(now()),INTERVAL 1 year)AND date(now())) g GROUP BY g.building_no,g.floor_no ORDER BY abs(g.building_no),abs(g.floor_no)")
    date1= cursor.fetchall()
    print("服务时长-按楼层分布类型%S内容%S\n" ,type(date1),date1)

    ##取出元祖中的值
    i=0
    long=len(date1)
    num=[]
    #将楼号和楼层用-进行连接，并放到num列表中
    while(i<long):
        time = []
        lis=list(date1[i])
        m="%s-%s"%(lis[0],lis[1])
        time.append(m)
        ##将服务最长时长换算成分钟并保存到num列表中
        j=int(lis[2])
        value1=round(j/60,1)
        #print('\n',type(value1),value1)
        if value1>int(value1):
            value1=int(value1)+1
            lis[2] = value1
            time.append(value1)
        else:
            value1 = int(value1)
            lis[2] = value1
            time.append(value1)
        ##将服务平均时长换算成分钟并保存为num列表中
        k=int(lis[3])
        value2=round(k/60,1)
        if value2>int(value2):
            value2=int(value2)+1
            lis[3] = value2
            time.append(value2)
        else:
            value2 = int(value2)
            lis[3] = value2
            time.append(value2)
        i=i+1
        num.append(time)
    print('数据库中一年中客需按楼层服务时长',type(num),num)
    #将楼层，最长服务时长，平均服务时长分别放到不同的列表中
    lou=[]
    max=[]
    ave=[]
    i=0
    while (i<len(num)):
        a=num[i][0]
        lou.append(a)
        b=num[i][1]
        max.append(b)
        c=num[i][2]
        ave.append(c)
        i+=1
    print('数据库中楼层列表为：',lou)
    print('最长服务时长为：',max)
    print('平均服务时长为：',ave)

    # 关闭数据库连接
    db.close()


    def test_server(self):
        start=self.start
        end=self.end
        lou=self.lou
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
            querystring = {"fromDate":start,"toDate":end,"type":"1"}
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
                if operator.eq(lou,category)==True:
                    if operator.eq(averageServiceTime,ave)==True:
                        if operator.eq(maxServiceTime,max)==True:
                            print('\n客需服务时长-按楼层统计的接口测试通过\n')
                        else:
                            print('\n客需服务时长-最长服务时长计算有问题\n', maxServiceTime)
                    else:
                        print('\n客需服务时长-平均服务时长返回结果有问题\n', averageServiceTime)

                else:
                    print('\n客需服务时长-楼层返回结果有问题\n', category)

if __name__ == '__main__':
    unittest.main()


