import requests
import pandas as pd

url="https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
data = response.json() 

clean_data=[{'id':item['id'],'title':item['title']} for item in data]


# clean_data=[{'id':item['id'],'title':item['title'] }for item in data]

print(f"一共获取了{len(clean_data)}条数据")
print("-"*30)

print(f"清洗前的数据第一条: {data[0]}")


for item in clean_data[:5]:
    print(f"ID: {item['id']},标题: {item['title']}")
  # print(f"ID: {item['id']} 标题：{item['title']}")
    
    