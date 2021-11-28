import argparse
import json
parser = argparse.ArgumentParser()
parser.add_argument("template_sql", nargs = 1, help="template SQL for modification.", type=str)
parser.add_argument("json_schema", nargs = 2, help="JSON file which specify the table schema for the output SQL.", type=str)
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

query = args.template_sql.format(table_name=jsn['table_name'], condition_string1=jsn['condition_string1'], column_names = ", ".join(column_name_list), event_names = ", ".join(condition_string2_list))

print("::set-output name=test::" + query)