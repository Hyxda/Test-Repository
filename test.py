import json

data = {
        'employees' : [
        {
            'name': 'John Doe',
            'department' : 'Marketing',
            'place' : 'remote'
        },
        {
            'name' : 'Jane Doe',
            'department' : 'Software Engineering',
            'place' : 'remote'
        },
        {
            'name' : 'Don Joe',
            'department' : 'Software Engineering',
            'place' : 'office'
        }
    ]
}

# dumps() as string
json_string = json.dumps(data)
print(json_string)