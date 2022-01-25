import json

def json_dumper(data):
	with ('main.json', 'w') as file:
		json.dump(data, file, indent=3)

def json_loader():
	with ('main.json', 'r') as file:
		return json.load(file)