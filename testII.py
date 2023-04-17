import json

with open('example_2.json', 'r') as f:
    data = json.load(f)

print(data['quiz']['sport']['q1']['question'])