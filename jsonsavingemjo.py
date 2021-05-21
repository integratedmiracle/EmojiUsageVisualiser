import json
import requests

def write_json(data, filename="emoji.json"):
    with open(filename,"w") as f:
        json.dump(data, f, indent=4)

r = requests.get('https://stream.emojitracker.com/subscribe/eps', stream=True)

for id in r.iter_lines(chunk_size=512, decode_unicode=True):
    if id:
        with open("emoji.json") as json_file:
            data = json.load(json_file)
            temp = data["emojidata"]
            y = eval(id.removeprefix("data:"))
            temp.append(y)
        write_json(data)