import json
with open('test_json.json', 'r') as f:
    data = json.load(f)
    print(data)