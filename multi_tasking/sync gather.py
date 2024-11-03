import asyncio

async def fetch_data(delay, id):
    print(f"veri alınıyor : {id}")
    await asyncio.sleep(delay)
    print(f"veri alındı : {id}")
    return {"data" : "bişeyler bişeyler","id" : id}

# task de oluşturdum ama await te çalıştırdım
async def main():
    results = await  asyncio.gather(fetch_data(1,1),fetch_data(1,2),fetch_data(1,3))
    for result in results:
        print(result)
    

    


asyncio.run(main())    
 