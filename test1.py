#  Script to scrape Australian postalcodes, locality and state from DATA.gov.au
#                          (Australian Government)GNAF-2023
#                 GNAF stands for Geoscape Geocoded National Access File.
#                           by Pabitra Jana
########################################################################################

import psycopg2
import json

conn = psycopg2.connect(
    dbname="******",       #For privacy concerns, removed it.
    user="******",         #Put your own db,username and password.
    password="*******",
    host="localhost"
)

cur = conn.cursor()

query = """
SELECT DISTINCT address_detail.postcode, locality.locality_name, state.state_name
FROM address_detail
JOIN locality ON address_detail.locality_pid = locality.locality_pid
JOIN state ON locality.state_pid = state.state_pid;
"""

cur.execute(query)



table_dict = {}

rows = cur.fetchall()
table_list = []  # Empty list to store dictionaries

for row in rows:    
    keys = ['Postcode', 'Locality', 'State']
    values = row
    table_dict = dict(zip(keys, values))
    table_list.append(table_dict)
    # print(table_dict)

# print(table_list)
json_string = json.dumps(table_list, indent=4)
print(json_string)



cur.close()
conn.close()
