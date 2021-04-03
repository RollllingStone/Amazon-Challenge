import sqlite3 as sql
import pandas as pd
con = sql.connect('amazon_last_mile_route.db')
# test 1. number of stations
sql_string1='''
SELECT COUNT(*), MAX(rp.lat), MIN(rp.lat), MAX(rp.lng), MIN(rp.lng), station_code
FROM route_path rp
INNER JOIN route rt
ON rp.route_id = rt.route_id
WHERE rp.actual=0
GROUP BY station_code
'''
df1 = pd.read_sql(sql_string1,con)
# test2. problem setting how many pickups?
sql_string2='''
SELECT COUNT(*)
FROM route_path
WHERE type != "Dropoff"
GROUP BY route_id
'''
df2 = pd.read_sql(sql_string2,con)
print(df2['COUNT(*)'].max())
sql_string3='''
SELECT *
FROM route_path
WHERE type != "Dropoff"
'''
df3 = pd.read_sql(sql_string3,con)
# we found that only one pickup station stop in each route

# test3. capacity constraint?
print('start test 3')
sql_string4='''
SELECT rt.route_id, rt.route_score AS route_score, SUM(depth_cm*height_cm*width_cm) AS total_vol, SUM(depth_cm*height_cm*width_cm)/executor_capacity_cm3 AS ratio
FROM package pkg
INNER JOIN route rt
ON pkg.route_id = rt.route_id
GROUP BY pkg.route_id
'''
df4 = pd.read_sql(sql_string4,con)
df4_abnormal = df4.loc[df4['ratio']>1]
route_id_interested = 'RouteID_2fa2f181-0c19-444d-a36c-938b0462270a' # this route has an ratio > 1

print('relation: score and ratio')
df4[['ratio','route_score']].hist(by='route_score',alpha=0.5)
from matplotlib import pyplot as plt
plt.figure()
df4_high = df4.loc[df4['route_score']=='High','ratio'].values
df4_med = df4.loc[df4['route_score']=='Medium','ratio'].values
df4_low = df4.loc[df4['route_score']=='Low','ratio'].values
plt.hist(df4_low,label='low',alpha=0.3, density=True)
plt.hist(df4_med,label='med',alpha=0.3, density=True)
plt.hist(df4_high,label='high',alpha=0.3, density=True)
plt.legend()
# we found that high score ususally has a higher ratio

# test4. do they need to return to the station?
# Here we alter the table so that we have the info of stations for each route
sql_string0='''
ALTER TABLE route
ADD COLUMN 
  lat REAL DEFAULT NULL;
'''
#con.execute(sql_string0)
sql_string0='''
ALTER TABLE route
ADD COLUMN 
  lng REAL DEFAULT NULL;
'''
#con.execute(sql_string0)

sql_string0 = '''
UPDATE route
SET lat = rp_first.lat,
    lng = rp_first.lng
FROM (
    SELECT MAX(lat) AS lat, MAX(lng) AS lng, route_id
    FROM route_path
    WHERE actual = 0
    GROUP BY route_id
) AS rp_first
WHERE route.route_id = rp_first.route_id
'''
#con.execute(sql_string0)
sql_string_first = '''
SELECT 
FROM route rt
INNER JOIN route_path rp
ON rt.route_id = rp.route_id
'''

