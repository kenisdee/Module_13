import asyncio

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for i in range(1, 6):
        await asyncio.sleep(5 / power)  # Задержка обратно пропорциональна силе
        print(f'Силач {name} поднял шар {i}')
    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    tasks = [
        asyncio.create_task(start_strongman("Паша", 3)),
        asyncio.create_task(start_strongman("Денис", 4)),
        asyncio.create_task(start_strongman("Аполлон", 5))
    ]
    await asyncio.gather(*tasks)

# Запуск асинхронной функции start_tournament
asyncio.run(start_tournament())