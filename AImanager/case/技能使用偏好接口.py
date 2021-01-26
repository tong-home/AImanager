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

    #客控技能总数
    a=cursor.execute("select sum(b.he) from (select count(distinct(a.control_id)) as 'he',a.ctrl_name from (SELECT control_id,ctrl_type,behavior, IF(ctrl_name like '%灯%','灯',IF(ctrl_name like '%窗帘%','窗帘',IF(ctrl_name like '%空调%','空调',ctrl_name)))  ctrl_name FROM guest_control where hotel_id=101661 and room_night_date between  DATE_SUB(date(now()),interval 1 year) and date(now()) and date(now()))a group by a.ctrl_name )b")
    date0= cursor.fetchall()
    he0 = date0[0][0]
    print('一年中客控总数为：', he0)

    shu=[]
    #获取客控技能按名称统计显示
    c=cursor.execute("select count(distinct(a.control_id)) as num,a.ctrl_name from (SELECT control_id,ctrl_type,behavior, IF(ctrl_name like '%灯%','灯',IF(ctrl_name like '%窗帘%','窗帘',IF(ctrl_name like '%空调%','空调',ctrl_name)))  ctrl_name FROM guest_control where hotel_id=101661 and room_night_date between  DATE_SUB(date(now()),interval 1 year) and date(now()) and date(now()))a group by a.ctrl_name order by num")
    date1= cursor.fetchall()
    i = 1
    num = []
    m = []
    while (i<len(date1)):
        h=date1[i]
        h=list(h)
        s=int(round(h[0]/he0*100,0))
        h.append(s)
        del h[0]
        shu.append(h)
        num.append(s)
        i+=1
    ##第一个数为100-其他总和
    value = 100 - sum(num)
    m.append(list(date1[0])[1])
    m.append(value)
    shu[0:0] = [m]
    print('数据库中一年中全部客需数量',shu)




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
            ##调用客控技能使用偏好接口
            url = "http://10.204.4.7:19101/behavior/ctrlBehavior/getConInfo"
            querystring = {"fromDate":start,"toDate":end}
            payload = ""
            headers = { 'token': token}
            response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
            #print('\n客需服务完成率接口结果为：',response.text)

            try:
                list=[]
                date2=json.loads(response.text)
                date3=date2['data']
                #print('ggg',date3)
                i=0
                while (i<len(date3)):
                    a=[]
                    name=date3[i]['name']
                    a.append(name)
                    value=date3[i]['value']
                    a.append(int(value))
                    list.append(a)
                    i+=1
                print('接口返回数据进行处理后最终结果是：',list)

            except:
                print('\n客需服务分布接口不通，报错信息为：',date2)

            else:
                if operator.eq(shu,list)==True:
                    print('测试通过')
                else:
                    print('客需服务完成率接口测试失败')



if __name__ == '__main__':
    unittest.main()
