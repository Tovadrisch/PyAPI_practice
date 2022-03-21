import aiohttp
import asyncio

async def main(): # [2]
    async with aiohttp.ClientSession() as session: # [3]
        async with session.get("http://httpbin.org/get",
                               headers={"Test-Request":"Id12345"}) as resp: # [4]
            print("Отправка GET-запроса...")
            if (resp.status == 200):
                print("Успех! Код ответа:", resp.status)
                response = await resp.json()  # [5]
                print(response, "\n")
            else:
                print("Произошла ошибка! Код ошибки:", resp.status)

        async with session.post('http://httpbin.org/post',
            headers={"Test-Request":"Id12345"},
            json={"test": "TEST DATA POST"}) as resp: # [1]
            print("Отправка POST-запроса...")
            if (resp.status == 200):
                print("Успех! Код ответа:", resp.status)
                response = await resp.json()  # [5]
                print(response, "\n")
            else:
                print("Произошла ошибка! Код ошибки:", resp.status)

        async with session.put('http://httpbin.org/put',
            headers={"Test-Request":"Id12345"},
            json={"test": "TEST DATA PUT"}) as resp: # [1]
            print("Отправка PUT-запроса...")
            if (resp.status == 200):
                print("Успех! Код ответа:", resp.status)
                response = await resp.json()  # [5]
                print(response, "\n")
            else:
                print("Произошла ошибка! Код ошибки:", resp.status)

        async with session.patch('http://httpbin.org/patch',
            headers={"Test-Request":"Id12345"},
            json={"test": "TEST DATA PATCH"}) as resp: # [1]
            print("Отправка PATCH-запроса...")
            if (resp.status == 200):
                print("Успех! Код ответа:", resp.status)
                response = await resp.json()  # [5]
                print(response, "\n")
            else:
                print("Произошла ошибка! Код ошибки:", resp.status)

        async with session.delete('http://httpbin.org/delete',
            headers={"Test-Request":"Id12345"},
            json={"test": "TEST DATA DELETE"}) as resp: # [1]
            print("Отправка DELETE-запроса...")
            if (resp.status == 200):
                print("Успех! Код ответа:", resp.status)
                response = await resp.json()  # [5]
                print(response, "\n")
            else:
                print("Произошла ошибка! Код ошибки:", resp.status)

asyncio.run(main()) # [6]