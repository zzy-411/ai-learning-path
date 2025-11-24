import pandas as pd
import requests
url="https://jsonplaceholder.typicode.com/users"
data = requests.get(url).json()

clean_data = [{'name':item['name'],'email':item['email'],'city':item['address']['city']} for item in data ]
df = pd.DataFrame(clean_data)
df.to_csv('newcsv',index=False,encoding='utf-8-sig')
print("已成功")

# url = "https://jsonplaceholder.typicode.com/users" 
# data = requests.get(url).json() 
# # 数据清洗，注意 city 的取法
# clean_users = [{ '姓名': item['name'], '邮箱': item['email'], '城市': item['address']['city'] # 这里的 address 是个字典，所以要继续 ['city']
#                  } for item in data ]
# df = pd.DataFrame(clean_users) 
# # 存为 CSV，通常防止乱码可以用 encoding='utf-8-sig' 
# df.to_csv("users.csv", index=False, encoding='utf-8-sig') 
# print("用户数据已保存为 users.csv")