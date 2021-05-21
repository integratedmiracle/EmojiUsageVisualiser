import requests
import time

r = requests.get('https://stream.emojitracker.com/subscribe/eps', timeout=(0.5), stream=True,)

for id in r.iter_lines(chunk_size=512, decode_unicode=True):
    print(id)
    time.sleep(5)