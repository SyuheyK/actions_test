import json
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("echo", help="echo the string you use here", type=str)
args = parser.parse_args()

test = open(args.echo, 'r').read().splitlines()

print("::set-output name=test::" + str(test))