# Asynchronous I/O, or async for short, is a programming pattern that allows for high-performance I/O operations in a concurrent and non-blocking manner. In Python, async programming is achieved through the use of the asyncio module and asynchronous functions.


import asyncio
import requests

async def my_async_function():
  # asynchronous code here
  #await asyncio.sleep(1)
  print("Func 1!")
  URL = "https://wallpaperaccess.in/public/uploads/preview/1920x1200-desktop-background-ultra-hd-wallpaper-wiki-desktop-wallpaper-4k-.jpg"
  response = requests.get(URL)
  open("instagram.ico", "wb").write(response.content)

  return "Minal"

async def my_async_function1():
  # asynchronous code here
  #await asyncio.sleep(1)
  print("Func 2!")
  URL = "https://p4.wallpaperbetter.com/wallpaper/490/433/199/nature-2560x1440-tree-snow-wallpaper-preview.jpg"
  response = requests.get(URL)
  open("instagram2.jpg", "wb").write(response.content)


async def my_async_function2():
  # asynchronous code here
  #await asyncio.sleep(4)
   print("Func 3!")
   URL = "https://c4.wallpaperflare.com/wallpaper/622/676/943/3d-hd-wikipedia-3d-wallpaper-preview.jpg"
   response = requests.get(URL)
   open("instagram3.ico", "wb").write(response.content)


async def main():
  # task = asyncio.create_task(my_async_function())
  # await my_async_function()
  # await my_async_function2()
  L = await asyncio.gather(
        my_async_function(),
        my_async_function1(),
        my_async_function2(),
    )
  print(L)

asyncio.run(main())