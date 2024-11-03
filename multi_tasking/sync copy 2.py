import asyncio

async def fetch_data(delay, id):
    print(f"veri alınıyor : {id}")
    await asyncio.sleep(delay)
    print(f"veri alındı : {id}")
    return {"data" : "bişeyler bişeyler","id" : id}

# task de oluşturdum ama await te çalıştırdım
async def main():
    task1 = asyncio.create_task(fetch_data(1,1))
    task2 = asyncio.create_task(fetch_data(1,2))
    task3 = asyncio.create_task(fetch_data(1,3))
    
    result = await task1
    print(f"alınan veri : {result}")
    """     task1 = fetch_data(1,1)
    task2 = fetch_data(1,2)
    task3 = fetch_data(1,3) """
    # böyle yaarsan senkron programlamadan farkı kalmıyor farklı olduğu kısım ..........
    result2 = await task2
    print(f"alınan veri : {result2}")
    
    result3 = await task3
    print(f"alınan veri : {result3}")
    
    


asyncio.run(main())    
