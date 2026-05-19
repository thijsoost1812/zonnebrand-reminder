import json, sys

today = sys.argv[1]

with open('/tmp/uv_response.json') as f:
    data = json.load(f)

max_uv = 0.0
max_rain = 0.0

for i, t in enumerate(data['hourly']['time']):
    if t.startswith(today):
        hour = int(t[11:13])
        if 8 <= hour <= 19:
            uv = data['hourly']['uv_index'][i] or 0
            rain = data['hourly']['precipitation'][i] or 0
            if uv > max_uv:
                max_uv = uv
            if rain > max_rain:
                max_rain = rain

print(round(max_uv, 1))
print(round(max_rain, 1))
