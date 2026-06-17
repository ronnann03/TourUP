import json

with open('graphify-out/graph.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Identificar duplicados - quedarse con el nodo simple (id mas corto)
labels = {}
to_remove = set()

for n in data['nodes']:
    label = n.get('label', '')
    if label not in labels:
        labels[label] = n['id']
    else:
        existing = labels[label]
        if len(n['id']) > len(existing):
            to_remove.add(n['id'])
        else:
            to_remove.add(existing)
            labels[label] = n['id']

# Filtrar nodos
original = len(data['nodes'])
data['nodes'] = [n for n in data['nodes'] if n['id'] not in to_remove]

# Filtrar edges que apunten a nodos removidos
data['edges'] = [e for e in data['edges']
                 if e.get('source') not in to_remove
                 and e.get('target') not in to_remove]

with open('graphify-out/graph.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f'Removidos {len(to_remove)} duplicados')
print(f'Nodos: {original} -> {len(data["nodes"])}')
print(f'Edges: {len(data["edges"])}')
