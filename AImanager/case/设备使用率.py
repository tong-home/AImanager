#!coding=utf-8
#!/usr/bin/python3

import pymysql,time,unittest,requests,json,operator
from datetime import datetime

class TestserverInitiate(unittest.TestCase):
    # 打开数据库连接
    db = pymysql.connect(host="192.168.13.235", user="root", password="joFem31$kf", database="bw_reven_tool",charset="utf8")
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

    #设备使用率
    a=cursor.execute("select count(distinct(room_no)),room_night_date from (select room_no,room_night_date from guest_requirement where hotel_id=101661 and room_night_date between date_sub(date(now()),INTERVAL 1 year) and date(now())union all select room_no,room_night_date from guest_control where hotel_id=101661 and room_night_date between date_sub(date(now()),INTERVAL 1 year) and date(now())) a group by a.room_night_date")
    Molecular = cursor.fetchall()
    #print("设备使用次数类型%S内容%S\n" ,type(Molecular),Molecular)


    b=cursor.execute("select room_count,room_night_date from hotel_room_night_count where hotel_id=101661 order by room_night_date")
    Denominator = cursor.fetchall()
    #print("当天的设备数量S内容%S\n" ,type(Denominator),Denominator)

    # 计算一年的天数差值
    b = cursor.execute('select datediff(date(now()),date_sub(date(now()),interval 1 year))')
    date3 = cursor.fetchall()
    days = date3[0][0]+1
    #print('相差天数为：', days)


    ##取出元祖中的值
    i=0
    list=[]
    time=[]
    #while(i<len(Denominator)):
    while(i<len(Denominator)):
        j=Denominator[i][0]
        k=Molecular[i][0]
        value=round((k/j)*100,2)
        if value>100:
            value=100
        elif value<0:
            value=0
        else:
            value=value
        list.append(value)
        time.append(Denominator[i][1])
        i=i+1
    ave=round(sum(list)/366,0)
    #print('一年中有使用设备的使用率',list)
    #print('设备使用率对应的时间为：',time)
    #print('活跃率求和：',sum(list))
    print('一年中设备平均活跃率',type(ave),ave)

    # 关闭数据库连接
    db.close()


    def test_server(self):
        start=self.start
        end=self.end
        list=self.list
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
            print('token值为：', token)
        except:
            print('获取token接口失败：', re)
        else:
            ##调用设备活跃率
            url = "http://192.168.13.235:19101/behavior/ctrlBehavior/loudspeakerUsage"
            querystring = {"fromDate":start,"toDate":end,"format":"M-d"}
            payload = ""
            headers = { 'token': token}
            response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
            #print(response.text)


            try:
                date2=json.loads(response.text)
                active=date2['data']['charts']['counts']
                averageUsage=date2['data']['averageUsage']
                averageUsage=float(averageUsage)
                #print(type(active),active,len(active))
                #print('接口中返回的一年平均设备活跃率',type(averageUsage), averageUsage)

                i=0
                #删除列表中所有为0的值
                #坑点：删除后相应的下标变化了~~~

                length = len(active)
                x = 0
                while x < length:
                    if active[x] == '0':
                        del active[x]
                        x -= 1
                        length -= 1
                    x = x+1
                #print ('取出非0的值之后剩余打印出来active',active)


            except:
                print('设备活跃率接口不通',date2)

            else:
                long= len(active)
                print(type(active[0]))
                print(type(list[0]))
                i = 0
                act=[]
                #接口中取出的值为str字符串，需要先转换为float浮点型数组
                while i< long:
                    j=active[i]
                    j=float(j)
                    #print(type(j))
                    act.append(j)
                    i = i+1


                if operator.eq(act,list)==True:
                    if operator.eq(averageUsage,ave)==True:
                        print('设备使用率接口测试通过~，每天的设备使用率和平均设备使用率均正确')
                    else:
                        print('设备使用接口中平均设备使用率计算错误')

                else:
                    print('设备使用率接口测试失败，每天的设备使用率和平均设备使用率均错误')
                    print('list为：',list)
                    #print('active为：',active)
                    print('接口中返回的设备活跃率act为：',act)


if __name__ == '__main__':
    unittest.main()


