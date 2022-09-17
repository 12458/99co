import json

urls = []

with open('urls.jl', 'r') as f:
    for line in f:
        data = json.loads(line)
        urls.extend(data['urls'])
urls = list(set(urls))
with open('urls.txt', 'w') as f:
    f.write('\n'.join(urls))