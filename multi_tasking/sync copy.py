import asyncio

async def fetch_data(delay):
    print("veri alınıyor")
    await asyncio.sleep(delay)
    print("veri alındı")
    return {"data" : "bişeyler bişeyler"}


async def main():
    print("start")
    task = fetch_data(2) # burda böle bir işlem yapılacak diyoruz
    result = await task # burda fetch data nın çalışmasının bitmesini bekliyoruz ki aşağıda result key error vermesin mesela yani burda yapıyoruz
    print(f"alınan veri : {result}") 
    #  result = await fetch_data(2) # bie asenkron fonk çağrılırken farklı bi yerden bu şekilde kullanılıyor
# main("merhaba")    
# RuntimeWarning: Enable tracemalloc to get the object allocation traceback
# print(main("merhaba"))
# async metodlar biaze bi obje döner async io ile onun çalıştırılması gerekşr aksi halde yukarıdaki hatayı alırsın
c_obj = main()
asyncio.run(c_obj)
print("that should print after hi")

# await olmadan, asenkron fonksiyon sadece bir coroutine nesnesi döndürür, ancak bu fonksiyonun tamamlanmasını beklemez. Bu nedenle, fonksiyonun geri kalanının çalışabilmesi için await kullanılması gerekir.