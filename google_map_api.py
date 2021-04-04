import googlemaps
from datetime import datetime,timedelta
import sqlite3 as sql
import pandas as pd
import pytz
from tzwhere import tzwhere


def get_google_map_dist_matrix(lat_lng_dict, departure_time, dist_matrix_history,is_utc=True,MAX_SIZE = 4):
    """
    :param lat_lng_dict: a dictionary of lat lng e.g. {'AB':(40.3,-120.5),...}
    :param departure_time: datetime, depareture time in UTC with given date
    :param dist_matrix_history: part of the travel_distance table
    :param is_utc: the input is in UTC or not
    :param MAX_SIZE: we only consider the first MAX_SIZE stops on one route
    :return:
    dist_matrix_reduced: reduced-size distance matrix from google map
    dist_matrix_history_reduced: reduced-size distance matrix from travel times
    """
    lat_lng_list = list(lat_lng_dict.values())
    if is_utc:
        tzwhere1 = tzwhere.tzwhere()
        timezone_str = tzwhere1.tzNameAt(lat_lng_list[0][0], lat_lng_list[0][1])
        timezone = pytz.timezone(timezone_str)
        departure_time0 = timezone.fromutc(departure_time)
    else:
        departure_time0 = departure_time
        
    dt = datetime.now()
    departure_time0 = departure_time0.replace(year=dt.year, month=dt.month, day=dt.day) + timedelta(days=1)
    API_KEY = '******'
    gmaps = googlemaps.Client(key=API_KEY)
    dist_matrix = gmaps.distance_matrix(origins=lat_lng_list[:MAX_SIZE], destinations=lat_lng_list[:MAX_SIZE], mode='driving',
                                        departure_time=departure_time0)

    name_list = list(lat_lng_dict.keys())[:MAX_SIZE]
    dist_matrix_history_reduced = dist_matrix_history.loc[name_list, name_list]
    dist_matrix_reduced = dist_matrix_history_reduced.copy()
    for index1, row in enumerate(dist_matrix['rows']):
        row1 = row['elements']
        name1 = name_list[index1]
        for index2, row2 in enumerate(row1):
            name2 = name_list[index2]
            value = row2['duration']['value']
            dist_matrix_reduced.loc[name1, name2] = value

    return dist_matrix_reduced, dist_matrix_history_reduced



con = sql.connect('amazon_last_mile_route.db')
route_info = pd.read_sql('SELECT * FROM route limit 100;',con)
one_route_id = route_info.loc[90,'route_id']
one_route_path = pd.read_sql('SELECT * FROM route_path WHERE route_id = "{0}"'.format(one_route_id),con)
lat_lng_dict = {one_route_path.loc[index,'stop_name']:(one_route_path.loc[index,'lat'],one_route_path.loc[index,'lng'])for index in one_route_path.index}

dt_str = route_info.loc[90,'date_YYYY_MM_DD']+' '+route_info.loc[90,'departure_time_utc']
departure_time = datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')

df_dist_matrix_history = pd.read_sql('SELECT * FROM travel_times WHERE route_id = "{0}";'.format(one_route_id), con)
dist_matrix_history = df_dist_matrix_history.pivot(index='stop1',columns='stop2',values='travel_time')

dist_matrix_reduced, dist_matrix_history_reduced = get_google_map_dist_matrix(lat_lng_dict, departure_time, dist_matrix_history,is_utc=False)





# results:
# from history data
#stop2     AD     AI     AO     AT
#stop1
#AD       0.0   86.4  316.3   84.2
#AI      78.6    0.0  268.5  139.0
#AO     270.8  257.9    0.0  331.2
#AT      91.7  148.9  394.2    0.0
# from google map
#stop2     AD     AI     AO     AT
#stop1
#AD       0.0   55.0  220.0   57.0
#AI      55.0    0.0  225.0   97.0
#AO     228.0  255.0    0.0  270.0
#AT      57.0   94.0  259.0    0.0