import argparse
import json
parser = argparse.ArgumentParser()
parser.add_argument("json_schema", help="JSON file which specify the table schema for the output SQL")
args = parser.parse_args()

with open(args.json_schema) as f:
    jsn = json.load(f)

print("::set-output name=test::おわり")