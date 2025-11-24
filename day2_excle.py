import pandas as pd
import requests

url = "https://jsonplaceholder.typicode.com/posts"
data = requests.get(url).json()

print(f"未清洗的数据:{data[0]}")

# 1. 清洗数据 (复习上午的知识)
# 假设我们想把 body 内容也存下来，统计字数作为 AI 的特征
clean_data = [
    {
    'id':item['id'],
    'title':item['title'],
    'long': len(item['body'])
    }
for item in data
]

# 2. 创建 DataFrame (这是 Pandas 的核心对象，你可以把它看作内存里的 Excel 表)
df = pd.DataFrame(clean_data)

# 3. 保存文件
# index=False 的意思是不要把 0,1,2... 这种索引号存进去
df.to_excel("new_data.xlsx",index=False)

print("成功！请在左侧文件栏查看 news_data.xlsx")