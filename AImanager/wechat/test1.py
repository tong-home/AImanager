import requests,json
###获取token值###
url = "https://dv-ucenter.brandwisdom.cn/api/v1/user/login"
###变量
me="tongtong.mu@jointwisdom.cn"
pw="MTT2019"
payload1 ={ "username": me,  "password":pw }
###将变量输入后变成的dic形式需要转换成str形式
payload=json.dumps(payload1)

headers = {
    'Content-Type': "application/json",
    }
response = requests.request("POST", url, data=payload, headers=headers)
print(response.request.body)
re=json.loads(response.text)
print(re)
###将dict的形式转换成json后才可以取出键值
token=re['data']['token']
print('token值为：',token)


