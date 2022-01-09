import json 
with open('/path/to/josn_file.json', 'r') as file:
     json_data = json.load(file)
     for item in json_data:
		if item['validity'] not in [""]:
		      item['validity'] = ""
		if item['read only'] not in [""]:
		      item['read only'] = ""
		if item['hidden'] not in [false]:
		      item['hidden'] = false
		if item['code'] not in [""]:
			item['code'] = ""

with open('/path/to/josn_file.json', 'w') as file:
    json.dump(json_data, file, indent=2)
