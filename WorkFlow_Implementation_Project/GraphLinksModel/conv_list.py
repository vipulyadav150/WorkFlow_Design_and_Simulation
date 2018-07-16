import json


with open("test2.json","r") as f:
    data = json.load(f)


for x in data["Actions"]:
    temp_list = []
    if type(x["ParentActionId"]) == int:
        parent = x["ParentActionId"]
        temp_list.append(parent)
        x["ParentActionId"] = temp_list
    # print(type(x["ParentActionId"]))
    # parent = x["ParentActionId"]

f.close()

with open("test2.json","w") as f:
    json.dump(data,f,indent=2)

print(data)