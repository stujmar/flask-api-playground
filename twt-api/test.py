import requests

BASE = "http://127.0.0.1:5000/"

data = [{"likes": 10, "name": "Tim", "views": 10000},
        {"likes": 100, "name": "Bill", "views": 100000},
        {"likes": 1000, "name": "John", "views": 1000000}]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())

response = requests.put(BASE + "video/99", {"likes": 10, "name": "Put from test.py", "views": 10000})
print(response.json())
input()
response = requests.get(BASE + "video/99")
print(response.json())
