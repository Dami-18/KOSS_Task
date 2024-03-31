import time
import requests

def save_json(url, filename):
    resp = requests.get(url)
    with open(filename, "wb") as f:
        f.write(resp.content)
        
def main():
    for comic_id in range(1,201):
        url = f"https://xkcd.com/{comic_id}/info.0.json"
        filename = f"Comic_ID{comic_id}.json"
        save_json(url, filename)

    
start = time.time()
main()
time_taken = time.time() - start
print('Time Taken {0}'.format(time_taken))


