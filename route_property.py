import pandas as pd
import json
with open("./data/model_build_inputs/route_data.json") as route_data_source:
	route_data = json.load(route_data_source)

# print(list(route_data.keys()))

###dict_keys(['station_code', 'date_YYYY_MM_DD', 'departure_time_utc', 'executor_capacity_cm3', 'route_score', 'stops'])

# print(route_data[list(route_data.keys())[0]].keys())
# a = pd.json_normalize(route_data[list(route_data.keys())[0]],max_level = 0)
# print(list(a.iloc[0])[:-1])
# # data = pd.json_normalize(travel_times[list(travel_times.keys())[0]]["AH"],max_level = 0, )

# 对每个route
# data = pd.json_normalize...., 
# list(data.iloc(0))[:-1]
df = pd.DataFrame(columns = ["route id", "station_code", "data_YYYY_MM_DD", "departure_time_utc", "executor_capacity_cm3", "route_score"])

# 默认是按route ID的既有顺序
for i in route_data.keys():
	route_id = []
	route_id.append(i)
	data = pd.json_normalize(route_data[i],max_level = 0)
	route_id += list(data.iloc[0])[:-1]
	route_id = [route_id]
	print("嘻嘻")
	print(route_id)
	to_dataframe = pd.DataFrame(route_id, columns = ["route id", "station_code", "data_YYYY_MM_DD", "departure_time_utc", "executor_capacity_cm3", "route_score"])     #######(route id, list 里面每个元素的值)
	df = df.append(to_dataframe, ignore_index = True)
	print(df)

print(df)