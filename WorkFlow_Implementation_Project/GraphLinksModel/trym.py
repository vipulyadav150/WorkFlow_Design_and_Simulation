import json

with open("try.json","r") as f:
    initial_data = json.load(f)
print(initial_data)

main_list = []
name_dict ={}
main_dict = {}
for x in initial_data["Actions"]:
    temp_list =[]
    id_list = []
    name = x["TargetBotName"]
    action_id = x["ActionId"]
    name_dict[action_id] = name
    for y in initial_data["Actions"]:
        if type(y["ParentActionId"]) == list:
            new_id = y["ActionId"]
            fetch_list = y["ParentActionId"]
            # print(fetch_list)
            if action_id in fetch_list:
                print('{} has a parent {}'.format(new_id,action_id))
                temp_list.append(y["TargetBotName"])
                id_list.append(y["ActionId"])

    main_list.append(id_list)
    main_dict[action_id]=id_list

print(main_dict)






    # for y in initial_data["Actions"]:
    #     if y["ParentActionId"] == action_id:
    #         temp_list.append(y["TargetBotName"])
    #         id_list.append(y["ActionId"])