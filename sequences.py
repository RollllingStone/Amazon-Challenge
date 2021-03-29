import pandas as pd
import json
#with open("./data/model_build_inputs/package_data.json") as package_data_source:
#	package_data = json.load(package_data_source)

with open("./data/model_build_inputs/route_data.json") as route_data_source:
 	route_data = json.load(route_data_source)

with open("./data/model_build_inputs/actual_sequences.json") as sequence_source:
	sequence_data = json.load(sequence_source)
col_names = ['index0','stop_name','lat','lng','route_id','type','zone_id','actual']

print('file loaded')

index0 = 0
rows = []
rt_num = 0
for route_id in list(sequence_data.keys()):
	print('route:',rt_num)
	rt_num+=1
	route_actual = sequence_data[route_id]["actual"]
	for stop_name in list(route_actual.keys()):
		stop_properties = route_data[route_id]["stops"][stop_name]
		rows.append([index0, stop_name, stop_properties['lat'], stop_properties['lng'],
					 route_id,stop_properties['type'],stop_properties['zone_id'], route_actual[stop_name]])
		index0 += 1
	# it's better to append to list, we should avoiding changing the length of pd.dataframe, otherwise it's slow
df = pd.DataFrame(rows, columns = col_names)
import sqlite3 as sql
con = sql.connect('amazon_last_mile_route.db')
df.to_sql('route_path',con,if_exists='append',index=False)
df2 = pd.read_sql('select count(*) from route_path',con)
con.close()






























