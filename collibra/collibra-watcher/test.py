import json
from argparse import ArgumentParser
from datetime import datetime, timedelta

# Set up argument parsing
parser = ArgumentParser(description='Process a JSON file.')
parser.add_argument('-c', '--config', type=str, help='Path to the JSON file.')

# Parse the arguments
args = parser.parse_args()

# Read and parse the JSON file
with open(args.config, 'r') as file:
    data = json.load(file)

clbraDomain = data['collibraDomain']
usr = data['username']
psswrd = data['password']
startDate = str()
endDate = str()

if ('startDate' in data and 'endDate' in data) and (data['startDate'] != '' and data['endDate'] != ''):
    startDate = data['startDate']
    endDate = data['endDate']
else:
    dayMinus1 = datetime.now() - timedelta(days=1)
    dayMinus2 = datetime.now() - timedelta(days=2)
    # now = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S%z')

    endDate = dayMinus1.strftime('%Y-%m-%dT00:00:00+00:00')
    startDate = dayMinus2.strftime('%Y-%m-%dT00:00:00+00:00')

# now = now[:-2] + ':' + now[-2:]
# print(now)

print(type(endDate))
print(type("hello"))

print(endDate)
print(startDate)
