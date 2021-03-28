# -*- coding: cp936 -*-

import pandas as pd
import json
with open("./package_data.json") as package_data_source:
	package_data = json.load(package_data_source)

# print(package_data[list(package_data.keys())[0]].keys())
# ###AD的所有package dict_keys(['PackageID_9d7fdd03-f2cf-4c6f-9128-028258fc09ea', 'PackageID_5541e679-b7bd-4992-b288-e862f6c84ae7', 'PackageID_84d0295b-1adb-4a33-a65e-f7d6247c7a07'])
# print(package_data[list(package_data.keys())[0]]["AD"].keys())
# p1 = list(package_data[list(package_data.keys())[0]]["AD"].keys())[0]
# data = pd.json_normalize(package_data[list(package_data.keys())[0]]["AD"][p1])
# print(list(data.iloc[0]))
###scan_status  planned_service_time_seconds  time_window.start_time_utc  time_window.end_time_utc  dimensions.depth_cm  dimensions.height_cm  dimensions.width_cm
# 0   DELIVERED                          59.3                         NaN                       NaN                 25.4                   7.6                 17.8


with open("./route_data.json") as route_data_source:
 	route_data = json.load(route_data_source)

# print(route_data[list(route_data.keys())[0]]["stops"].keys())
# print(route_data[list(route_data.keys())[0]]["stops"]["AD"])
# data = pd.json_normalize(route_data[list(route_data.keys())[0]]["stops"]["AD"])
# dict_keys(['AD', 'AF', 'AG', 'BA', 'BE', 'BG', 'BP', 'BT', 'BY', 'BZ', 'CA', 'CG', 'CK', 'CM', 'CO', 'CP', 'CW', 'DJ', 'DL', 'DN', 'DQ', 'EC', 'EH', 'EO', 'EX', 'EY', 'FF', 'FH', 'FY', 'GB', 'GN', 'GP', 'GS', 'GU', 'GW', 'HB', 'HG', 'HN', 'HO', 'HR', 'HT', 'HW', 'IA', 'IJ', 'IM', 'IP', 'IW', 'JH', 'JM', 'KA', 'KG', 'KJ', 'KM', 'KN', 'KP', 'KU', 'LB', 'LD', 'LG', 'LK', 'LY', 'MA', 'MO', 'MQ', 'MR', 'MW', 'NE', 'NL', 'NM', 'NR', 'NU', 'PB', 'PJ', 'PS', 'PT', 'PX', 'QE', 'QM', 'QO', 'QX', 'RA', 'RG', 'RY', 'SC', 'SD', 'SF', 'SI', 'SQ', 'TC', 'TG', 'TH', 'TK', 'TQ', 'TY', 'UI', 'UJ', 'UN', 'UR', 'US', 'UU', 'UW', 'VA', 'VC', 'VE', 'VW', 'WJ', 'WS', 'XB', 'XD', 'YE', 'YH', 'YJ', 'YN', 'YR', 'YY', 'ZB', 'ZE', 'ZP', 'ZU'])
# {'lat': 34.099611, 'lng': -118.283062, 'type': 'Dropoff', 'zone_id': 'P-12.3C'}
# [34.099611, -118.283062, 'Dropoff', 'P-12.3C']

# print(list(data.iloc[0]))
with open("./actual_sequences.json") as sequence_source:
	sequence_data = json.load(sequence_source)

# print(sequence_data[list(sequence_data.keys())[0]]["actual"])
# {'AD': 105, 'AF': 47, 'AG': 4, 'BA': 33, 'BE': 109, 'BG': 53, 'BP': 67, 'BT': 49, 'BY': 7, 'BZ': 61, 'CA': 43, 'CG': 26, 'CK': 86, 'CM': 96, 'CO': 54, 'CP': 36, 'CW': 8, 'DJ': 28, 'DL': 15, 'DN': 37, 'DQ': 35, 'EC': 106, 'EH': 101, 'EO': 56, 'EX': 104, 'EY': 69, 'FF': 88, 'FH': 12, 'FY': 76, 'GB': 81, 'GN': 42, 'GP': 2, 'GS': 64, 'GU': 16, 'GW': 74, 'HB': 97, 'HG': 87, 'HN': 40, 'HO': 80, 'HR': 111, 'HT': 3, 'HW': 93, 'IA': 57, 'IJ': 20, 'IM': 68, 'IP': 94, 'IW': 23, 'JH': 10, 'JM': 92, 'KA': 48, 'KG': 55, 'KJ': 41, 'KM': 51, 'KN': 17, 'KP': 22, 'KU': 63, 'LB': 11, 'LD': 46, 'LG': 27, 'LK': 84, 'LY': 83, 'MA': 66, 'MO': 89, 'MQ': 70, 'MR': 25, 'MW': 50, 'NE': 45, 'NL': 29, 'NM': 79, 'NR': 18, 'NU': 65, 'PB': 110, 'PJ': 73, 'PS': 82, 'PT': 14, 'PX': 117, 'QE': 85, 'QM': 5, 'QO': 107, 'QX': 118, 'RA': 71, 'RG': 59, 'RY': 75, 'SC': 19, 'SD': 115, 'SF': 6, 'SI': 95, 'SQ': 99, 'TC': 44, 'TG': 1, 'TH': 24, 'TK': 13, 'TQ': 91, 'TY': 103, 'UI': 52, 'UJ': 38, 'UN': 108, 'UR': 30, 'US': 72, 'UU': 114, 'UW': 39, 'VA': 32, 'VC': 60, 'VE': 0, 'VW': 9, 'WJ': 113, 'WS': 78, 'XB': 21, 'XD': 98, 'YE': 58, 'YH': 34, 'YJ': 102, 'YN': 90, 'YR': 77, 'YY': 116, 'ZB': 112, 'ZE': 31, 'ZP': 100, 'ZU': 62}
# for route in list(sequence_data.keys()):
col_names1 = ["route id", "stop id", "sequence", "lat","lng","type","zone_id"]
col_names2 = ["route id", "stop id", "package id", "scan_status", "service seconds","time_window.start", "time_window.end", "depth_cm","height_cm","width_cm"]

df1 = pd.DataFrame(columns = col_names1)
df2 = pd.DataFrame(columns = col_names2)

# (route id, stop point, sequence_data[route_id]["actual"][stop_point], package_id, )
# row = []
# 	row.append(route_id)
# 	row.append(stop_point)
# 	row.append()


for route_id in list(sequence_data.keys()):
	route = sequence_data[route_id]["actual"]
	for stop_point in list(route.keys()):
		route_properties = pd.json_normalize(route_data[route_id]["stops"][stop_point])
		route_properties = list(route_properties.iloc[0])
		row1 = [route_id, stop_point, sequence_data[route_id]["actual"][stop_point]]
		row1 += route_properties
		row1 = [row1]
		to_dataframe1 = pd.DataFrame(row1, columns = col_names1)
		df1 = df1.append(to_dataframe1, ignore_index = True)
		print(df1)
		if package_data[route_id].get(stop_point, "NA") != "NA":
			for package_id in list(package_data[route_id][stop_point]):
				package_info = pd.json_normalize(package_data[route_id][stop_point][package_id])
				package_info = list(package_info.iloc[0])
				row2 = [route_id, stop_point, package_id]
				row2 += package_info
				route_properties = pd.json_normalize(route_data[route_id]["stops"][stop_point])
				route_properties = list(route_properties.iloc[0])
				row2 = [row2]
				to_dataframe2 = pd.DataFrame(row2, columns = col_names2)
				df2 = df2.append(to_dataframe2, ignore_index = True)

				print(df2)

		else:
			row2 = [route_id, stop_point, package_id,"", "", "","", "","",""]
			row2 = [row2]
			to_dataframe2 = pd.DataFrame(row2, columns = col_names2)
			df2 = df2.append(to_dataframe2, ignore_index = True)
			print(df2)


df1.to_csv("stop_point_info.csv")
df2.to_csv("package_info.csv")




























