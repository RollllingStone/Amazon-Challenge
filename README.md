# Amazon-Challenge

# create database:
run create_db_python.py

run route_property.py

run sequences.py

run packages.py

run travel_times.py

Note: run one file only once, otherwise we will duplicate data

# use the database
make sure amazon_last_mile_route.db is in your folder

Example 1. read database to pd.DataFrames:
```python
import sqlite3 as sql
import pandas as pd
con = sql.connect('amazon_last_mile_route.db')
df_route = pd.read_sql('select * from route limit 100')
df_route_path= pd.read_sql('select * from route_path limit 100',con)
con.close()
```