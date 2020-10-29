import requests

BASE = "http://127.0.0.1:5000/"


data = [
    {"likes": 78, "name": "Video 1", "views": 10000},
    {"likes": 88, "name": "Video 2", "views": 20000},
    {"likes": 98, "name": "Video 3", "views": 30000}
]

print('PUTS')


for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())


# response = requests.delete(BASE + "video/0")
# print(response)

# input()
print()
print('GETS:')
print()

for i in range(len(data)):
    response = requests.get(BASE + "video/" + str(i))
    print(response.json())


print()
print('DELETES:')
print()

for i in range(len(data)):
    response = requests.delete(BASE + "video/" + str(i))
    print(response)

print()
print('GETS:')
print()

for i in range(len(data)):
    response = requests.get(BASE + "video/" + str(i))
    print(response.json())
