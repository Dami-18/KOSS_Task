# KOSS_Task
The given below task highlights how python tackles the problem of locked threading with its concurrency paradigm to provide added performance using multiple threads. It also compares the concurrency paradigms with C++ and Golang.
Some example code snippets have been inserted in the presentation which implements multithreading and asynchronous programming and compares their execution times with synchronous programs.
## Asyncio and Aiohttp packages
In the code file uploaded, json responses have been downloaded from 200 URLs in both ways: Asynchronously and Synchronously.
In synchronous manner, time taken for execution was about 312.91 seconds.
Using async/await and aiohttp, the json responses were downloaded asynchronously. This resulted in execution time of about 4.085 seconds.

