import json

with open('sunless.dat', 'w') as f:
    for name in ['areas', 'events', 'exchanges', 'personas', 'qualities']:
        with open(f'{name}_import.json') as g:
                data = json.loads(g.read())
                for line in data:
                    entry = {'key': f'{name}:{line["Id"]}', 'value': line}
                    f.write(f"{json.dumps(entry)}\n")
    with open('settings.json') as g:
        f.write(g.read())
