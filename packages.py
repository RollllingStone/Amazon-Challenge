import pandas as pd
import json

with open("./data/model_build_inputs/package_data.json") as package_data_source:
    package_data = json.load(package_data_source)

col_names = ['index0', 'route_id', 'stop_name', 'package_id', 'scan_status', 'time_window_start', 'time_window_end',
             'planned_service_time_seconds', 'depth_cm', 'height_cm', 'width_cm']
"""
index0 INTEGER PRIMARY KEY,
  route_id TEXT DEFAULT NULL,
  stop_name TEXT DEFAULT NULL,
  package_id TEXT DEFAULT NULL,
  scan_status TEXT DEFAULT NULL,
  time_window_start TEXT DEFAULT NULL,
  time_window_end TEXT DEFAULT NULL,
  planned_service_time_seconds INTEGER DEFAULT NULL,
  depth_cm REAL DEFAULT NULL,
  height_cm REAL DEFAULT NULL,
  width_cm REAL DEFAULT NULL,
"""
rows = []
rt_num = 0
index0 = 0
for route_id in list(package_data.keys()):
    route = package_data[route_id]
    print('route:', rt_num)
    rt_num += 1
    for stop_name, stop_packages in route.items():
        for package_id, package_property in stop_packages.items():
            this_row = [index0, route_id, stop_name, package_id, package_property['scan_status'],
             package_property['time_window']['start_time_utc'], package_property['time_window']['end_time_utc'],
             package_property['planned_service_time_seconds'],
             package_property['dimensions']['depth_cm'],
             package_property['dimensions']['height_cm'],
             package_property['dimensions']['width_cm']
             ]
            rows.append(this_row)
            index0 += 1
df = pd.DataFrame(rows, columns = col_names)
import sqlite3 as sql
con = sql.connect('amazon_last_mile_route.db')
df.to_sql('package',con,if_exists='append',index=False)
df2 = pd.read_sql('select * from route_path',con)
con.close()
