import pandas as pd
import json
with open("./data/model_build_inputs/route_data.json") as route_data_source:
	route_data = json.load(route_data_source)
df = pd.DataFrame(columns = ["route id", "station_code", "data_YYYY_MM_DD", "departure_time_utc", "executor_capacity_cm3", "route_score"])
for i in route_data.keys():
	route_id = []
	route_id.append(i)
	data = pd.json_normalize(route_data[i],max_level = 0)
	route_id += list(data.iloc[0])[:-1]
	route_id = [route_id]
	#print("嘻嘻")
	print(route_id)
	to_dataframe = pd.DataFrame(route_id, columns = ["route id", "station_code", "data_YYYY_MM_DD", "departure_time_utc", "executor_capacity_cm3", "route_score"])     #######(route id, list 里面每个元素的值)
	df = df.append(to_dataframe, ignore_index = True)
	#import pdb;pdb.set_trace()
	print(df)
df.rename(columns={'route id':'route_id','data_YYYY_MM_DD':'date_YYYY_MM_DD'},inplace=True)

import sqlite3 as sql
con = sql.connect('amazon_last_mile_route.db')
df.to_sql('route',con,if_exists='append',index=False)
con.close()