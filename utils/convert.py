import json

with open('sunless.dat', 'w') as f:
    for name in ['areas', 'events', 'exchanges', 'personas', 'qualities']:
        with open(f'{name}_import.json') as g:
                data = json.loads(g.read())
                for line in data:
                    entry = {'key': f'{name}:{line["Id"]}', 'value': line}
                    f.write(f"{json.dumps(entry)}\n")
    with open('Tiles.txt') as g:
        tiles = json.loads(g.read())
        ports = {}
        for tile in tiles:
            for subtile in tile['Tiles']:
                for port in subtile['PortData']:
                    id = port['Setting']['Id']
                    try:
                        ports[id].append(port['Name'])
                    except KeyError:
                        ports[id] = [port['Name']]
        for id in ports:
            entry = {'key': f'settings:{id}', 'value': {'Id': id, 'Name': ports[id][0] if len(ports[id]) == 1 else ports[id]}}
            f.write(f'{json.dumps(entry)}\n')
