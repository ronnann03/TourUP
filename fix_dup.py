import json

with open('graphify-out/graph.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

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

original = len(data['nodes'])
data['nodes'] = [n for n in data['nodes'] if n['id'] not in to_remove]

data['links'] = [e for e in data['links']
                 if e.get('source') not in to_remove
                 and e.get('target') not in to_remove]

with open('graphify-out/graph.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print('Removidos:', len(to_remove))
print('Nodos:', original, '->', len(data['nodes']))
print('Links:', len(data['links']))
