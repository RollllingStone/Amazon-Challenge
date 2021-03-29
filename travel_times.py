import pandas as pd
import json

with open("./data/model_build_inputs/travel_times.json") as travel_time_source:
    travel_times = json.load(travel_time_source)
print('travel time file loaded')
col_names = ['index0', 'route_id', 'stop1', 'stop2', 'travel_time']
"""
index0 INTEGER PRIMARY KEY,
  route_id TEXT DEFAULT NULL,
  stop1 TEXT DEFAULT NULL,
  stop2 TEXT DEFAULT NULL,
  travel_time REAL DEFAULT NULL,
"""
rows = []
rt_num = 0
index0 = 0
for route_id in list(travel_times.keys()):
    dist_matrix = travel_times[route_id]
    print('route:', rt_num)
    rt_num += 1
    for stop1, stop2s_of_stop1 in dist_matrix.items():
        for stop2, dist in stop2s_of_stop1.items():
            this_row = [index0, route_id, stop1, stop2, dist]
            rows.append(this_row)
            index0 += 1
df = pd.DataFrame(rows, columns=col_names)

del travel_times

import sqlite3 as sql
con = sql.connect('amazon_last_mile_route.db')
df.to_sql('travel_times', con, if_exists='append', index=False)
df2 = pd.read_sql('select * from route_path limit 100', con)
con.close()
