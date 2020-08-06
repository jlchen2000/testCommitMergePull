import asyncio
import websockets

async def message():
    async with websockets.connect("ws://localhost:1234") as websocket:
        msg = input("what do you want to send: ")
        await websocket.send(msg)
        print(await websocket.recv())

asyncio.get_event_loop().run_until_complete(message())