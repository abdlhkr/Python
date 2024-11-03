import asyncio

async def main(msg):
    print("start")
    await asyncio.sleep(2) # ssame thing with the time module
    print(msg)
    
# main("merhaba")    
# RuntimeWarning: Enable tracemalloc to get the object allocation traceback
# print(main("merhaba"))
# async metodlar biaze bi obje döner async io ile onun çalıştırılması gerekşr aksi halde yukarıdaki hatayı alırsın
c_obj = main("merhaba")
asyncio.run(c_obj)
print("that should print after hi")