import asyncio
import time
import aiohttp


async def download_file(url, filename):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.read()
            with open(filename, "wb") as f:
                f.write(data)
                
async def main():
    obj1 = download_file("https://reqres.in/api/users?page1", "Page1.txt")
    obj2 = download_file("https://reqres.in/api/users?page2", "Page2.txt")
    obj3 = download_file("https://reqres.in/api/users?page3", "Page3.txt")

    
    start = time.time()

    await asyncio.gather(obj1, obj2, obj3)

    time_taken = time.time() - start
    print('Time Taken {0}'.format(time_taken))

asyncio.run(main())
