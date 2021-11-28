import argparse
import json
parser = argparse.ArgumentParser()
parser.add_argument("json_schema", help="JSON file which specify the table schema for the output SQL.", type=str)
args = parser.parse_args()

with open(args.json_schema) as f:
    jsn = json.load(f)

condition_string2_list = []
column_name_list = []

for i in range(1,len(jsn)-1):
    condition_string2_list.append('"'+jsn['condition'+str(i)]['condition_string2']+'"')
    column_name_list.extend(jsn['condition'+str(i)]['column_names'])

condition_string2_list = list(dict.fromkeys(condition_string2_list))
column_name_list = list(dict.fromkeys(column_name_list))

query = """
DECLARE condition STRING DEFAULT '{condition_string1}';

SELECT
  {column_names}
FROM `table_{table_name}`
WHERE condition_column1 = condition
  AND condition_column2 in ({condition_string2})
""".format(table_name=jsn['table_name'], 
      condition_string1=jsn['condition_string1'], 
      column_names = ", ".join(column_name_list), 
      event_names = ", ".join(condition_string2_list)
)

print("::set-output name=test::" + query)