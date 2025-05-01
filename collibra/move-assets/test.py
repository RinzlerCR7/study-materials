import requests
import json
import logging
# import api.Id_validation as Id_validation
from argparse import ArgumentParser

# Set up argument parsing
parser = ArgumentParser(description='Process a JSON file.')
# parser.add_argument('-u', '--user')
# parser.add_argument('-p', '--password')
parser.add_argument('-c', '--config', type=str, help='Path to the JSON file.')

# Parse the arguments
args = parser.parse_args()

# Read and parse the JSON file
with open(args.config, 'r') as file:
    data = json.load(file)

# Process the JSON data (example: print it)
print('user: ' + data['username'])
print('password: ' + data['password'])

# Id validation
# usr = args.user
# psswrd = args.password

# print (usr + ' --> ' + psswrd)
# response = Id_validation.POST_auth_sessions(usr, psswrd)
# print("***RESPONSE***")
# print(response.status_code)
# print(response)

# python process_json.py path/to/your/file.json
