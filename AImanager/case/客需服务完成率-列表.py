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

    #获取客需服务完成按楼层统计数量
    c=cursor.execute("SELECT g.building_no,g.floor_no,COUNT(1),SUM(IF(g.`status`=2,1,0)),SUM(IF(g.`status`=3,1,0)) FROM (SELECT DISTINCT(requirement_id),`status`,hotel_id,room_night_date,building_no,floor_no FROM guest_requirement) g WHERE g.room_night_date between DATE_SUB(date(now()),interval 1 year) and date(now()) AND g.hotel_id='101661'GROUP BY g.building_no,g.floor_no ORDER BY abs(g.building_no),abs(g.floor_no)")
    date1= cursor.fetchall()
    he1=list(date1[0])
    #print('sql语句中取出一年中全部楼层客需',type(date1),date1)
    value = list(date1[0])
    #print('大点东西出来看卡\n', round((value[3] + value[4])/ value[2] * 100,2))
    i=0
    shu = []
    while (i<len(date1)):
        value=list(date1[i])
        per=round((value[3] + value[4])/ value[2] * 100,2)
        value[3] = int(value[3])
        value[4] = int(value[4])
        if per==0.00:
            per=0
            value.append(str(per))
        else:
            value.append(str(per))
        i+=1
        shu.append(value)
    print('\n数据库中sql语句执行并处理后：\n',type(shu),shu)



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
            ##调用客需服务完成率--列表接口
            url = "http://10.204.4.7:19101/behavior/demandBehavior/getCompleteList"
            querystring = {"fromDate":start,"toDate":end,"page":1,"pageSize":1000}
            payload = ""
            headers = { 'token': token}
            response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
            #print('客需服务完成率接口结果为：',response.text)


            try:
                list=[]
                date2=json.loads(response.text)
                #print('\n接口返回的结果为\n', date2)
                ha=date2['data']['list']
                #print('客需服务-列表接口返回的值结果\n',type(ha),ha)
                i=0
                while (i<len(ha)):
                    list1=[]
                    del ha[i]['id']
                    del ha[i]['buildloor']
                    a=ha[i]['buildingNo']
                    b=ha[i]['floorNo']
                    c= ha[i]['allCount']
                    d=ha[i]['completeCount']
                    e=ha[i]['cancelCount']
                    f=ha[i]['completeRate']
                    i+=1
                    list1.append(a)
                    list1.append(b)
                    list1.append(c)
                    list1.append(d)
                    list1.append(e)
                    list1.append(f)
                    list.append(list1)
                print('\n取出接口中楼号-楼层-总数-完成数-取消数-占比：\n',list)


            except:
                print('\n客需服务分布接口不通，报错信息为：',date2)

            else:
                if operator.eq(shu,list)==True:
                    print('测试通过')
                else:
                    print('客需服务完成率接口测试失败\n',type(list),list)

if __name__ == '__main__':
    unittest.main()
