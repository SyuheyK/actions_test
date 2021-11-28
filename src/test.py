import json
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("echo", help="echo the string you use here", type=str)
args = parser.parse_args()

print("::set-output name=test::" + args.echo)