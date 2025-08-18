import json

# data = {"name": "Ali", "age": 22}
# json_str = json.dumps(data)  # Python dict → JSON string
# print(json_str)

# x={"name":"ahmad","city":"Lahore,Talwandi","age":21}
# x_jason=json.dumps(x)
# print(x_jason)

info='{"name":"ahmad","city":"Lahore,Talwandi","age":21}'
data=json.loads(info)
print(data["name"],data["city"])