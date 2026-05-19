import json, sys

today = sys.argv[1]

with open('/tmp/uv_response.json') as f:
    data = json.load(f)

max_uv = 0.0
for i, t in enumerate(data['hourly']['time']):
    if t.startswith(today):
        hour = int(t[11:13])
        uv = data['hourly']['uv_index'][i] or 0
        if 8 <= hour <= 19 and uv > max_uv:
            max_uv = uv

print(round(max_uv, 1))
