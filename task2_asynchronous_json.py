import asyncio
import time
import aiohttp

urls = []
filenames = []
for id in range(1,201):
    urls.append(f"https://xkcd.com/{id}/info.0.json")
    filenames.append(f"ComicID{id}.json")

def get_tasks(session, urls):
    tasks = []
    for url in urls:
        tasks.append(session.get(url))
    return tasks

async def main():
    async with aiohttp.ClientSession() as session:
        start = time.time()
        tasks = await asyncio.gather(*get_tasks(session, urls))
        for task in tasks:
            data = await task.read()
            url_index = urls.index(str(task.url))
            with open(filenames[url_index], "wb") as f:
                f.write(data)
        time_taken = time.time() - start
        print('Time Taken {0}'.format(time_taken))

asyncio.run(main())


