import json

with open("test.json", "r") as f:
    initial_data = json.load(f)

main_dict = {}
name_dict = {}
main_list = []
for x in initial_data["Actions"]:
    temp_list =[]
    id_list = []
    name = x["TargetBotName"]
    action_id = x["ActionId"]
    name_dict[action_id] = name
    for y in initial_data["Actions"]:
        if y["ParentActionId"] == action_id:
            temp_list.append(y["TargetBotName"])
            id_list.append(y["ActionId"])
            # print(temp_list)
            # print(id_list)

    main_list.append(id_list)
    main_dict[action_id]=id_list

# print(main_list)
js_dict = {}
final_list = []



for x in initial_data["Actions"]:
    if x["ParentActionId"] == 0:
        start_nodes_id = x["ActionId"]
        start_nodes_name = x["TargetBotName"]
        js_dict["key"]=start_nodes_id
        js_dict["name"]=start_nodes_name
        final_list.append(js_dict.copy())



final_dict = {}
linkDataArray = []
temp_linked_data = {}
for keys in main_dict:
    # print(keys)

    if type(main_dict[keys]) == list:
        for item in main_dict[keys]:
            js_dict["key"]=item
            # js_dict["parent"]=keys
            # print(js_dict)
            temp_linked_data["from"]=keys
            temp_linked_data["to"]=item
            temp_linked_data["fromPort"]='B'
            temp_linked_data["toPort"]='T'
            # print(temp_linked_data)
            linkDataArray.append(temp_linked_data.copy())
            for x in name_dict:
                if x == item:
                    text= name_dict[x]
                    js_dict["name"]=text
                    js_dict["text"]=text


            final_list.append(js_dict.copy())

# print(final_list)

print(linkDataArray)




final_dict["class"] = "go.GraphLinksModel"
final_dict["linkFromPortIdProperty"] = "fromPort"
final_dict["linkToPortIdProperty"] = "toPort"
final_dict["nodeDataArray"]=final_list

final_dict["linkDataArray"]=linkDataArray
with open("merge.json","w") as f:
    json.dump(final_dict,f,indent=2)


# print(name_dict)