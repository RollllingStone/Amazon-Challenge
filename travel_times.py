import pandas as pd
import json

with open("./data/model_build_inputs/travel_times.json") as travel_time_source:
	travel_times = json.load(travel_time_source)
# data = pd.json_normalize(travel_times[list(travel_times.keys())[0]]["AH"],max_level = 0, )
# print(list(data.columns))
# print(list(data.iloc[0]))


####MacBook-Air:last_mile_delivery apple$ python3 j_to_c.py
#     AH     AK     AN     AU     AV     AY    BA     BC     BK  ...     YX     ZB     ZH     ZI     ZL     ZO     ZQ     ZS     ZX
# 0  0.0  287.4  249.4  476.9  421.2  320.7  87.4  481.5  398.4  ...  233.4  494.9  456.9  186.6  418.1  343.0  124.6  475.9  397.2

# [1 rows x 193 columns]


####route id
total = []
# 默认是按route ID的既有顺序
for i in travel_times.keys():
	route_id = []
	#####from [AA, AB ,AC]  pick one 'from' city
	for j in list(travel_times[i].keys()):
		from_node_j_times= []
		data = pd.json_normalize(travel_times[i][j],max_level = 0)
		from_node_j_times = (i,j, list(data.columns), list(data.iloc[0])) ####第三个entry就是第一行
		route_id.append(from_node_j_times) 
	total.append(route_id)

df = pd.DataFrame(columns = ["route id", "from", "to", "time"])

# print(total[0][0][2])
# total = [list1, list1].   total [[route 1], [route 2]].  route 1 = [(route id, AA, AA to all, AA to all times)]
# route 1 = [(AA),(AB),(AC)]

for route in total:
	for from_node in range(len(route)):
		each_node = []
		for to_node_index in range(len(route[from_node][2])):
			each_node.append([route[from_node][0], route[from_node][1], route[from_node][2][to_node_index], route[from_node][3][to_node_index]])
		to_dataframe = pd.DataFrame(each_node, columns = ["route id", "from", "to", "time"])
		df = df.append(to_dataframe,ignore_index=True)
		if from_node ==4:
			print(df)

print(df)


#                                             route id from  to   time
# 0       RouteID_15baae2d-bf07-4967-956a-173d4036613f   AH  AH    0.0
# 1       RouteID_15baae2d-bf07-4967-956a-173d4036613f   AH  AK  287.4
# 2       RouteID_15baae2d-bf07-4967-956a-173d4036613f   AH  AN  249.4
# 3       RouteID_15baae2d-bf07-4967-956a-173d4036613f   AH  AU  476.9
# 4       RouteID_15baae2d-bf07-4967-956a-173d4036613f   AH  AV  421.2
# ...                                              ...  ...  ..    ...
# 330788  RouteID_fffd257c-3041-4736-be7a-5efea8af1173   ZX  YU  641.0
# 330789  RouteID_fffd257c-3041-4736-be7a-5efea8af1173   ZX  YW   23.8
# 330790  RouteID_fffd257c-3041-4736-be7a-5efea8af1173   ZX  ZK  281.1
# 330791  RouteID_fffd257c-3041-4736-be7a-5efea8af1173   ZX  ZS  528.2
# 330792  RouteID_fffd257c-3041-4736-be7a-5efea8af1173   ZX  ZX    0.0

# [330793 rows x 4 columns]
# MacBook-Air:last_mile_deliv



######批量读取，写一个循环把每个node的存到一个list 1 里面存成  [(AA,[AA到所有],[AA到所有数字])，(AB,[AB到所有])...
####然后这个循坏在route的循环里面 然后每个loop一个route id 的时候，就把
# for i in len(list1):
#        for j in len(list1[i][1])   list 1[i]是route id的(AA,[AA到所有]):
#           row.append([route id, list1[i][0],list1[i][1][j], list1[i][2][j]])    加入[route id, from, to , time]