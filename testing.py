import asyncio
from datetime import datetime
from telethon import TelegramClient, events 

# async def hello(delay):
#     await asyncio.sleep(delay)
#     print("hello")

# async def world(delay):
#     await asyncio.sleep(delay)
#     print("world")

# loop = asyncio.get_event_loop()
# loop.create_task(world(2))
# loop.create_task(hello(1))
# loop.run_forever()

async def clock():
    while(True):
        print("Time: ", datetime.now())
        await asyncio.sleep(1)

api_id = 
api_hash = ''
phone = ''
chatwars = 'chtwrsbot'

loop = asyncio.get_event_loop()

client=TelegramClient(phone,api_id,api_hash)

client.start()

async def alert():
    while(True):
        await client.send_message('me', 'alert bitch')
        await asyncio.sleep(5)

# para verificar que esta running
@client.on(events.NewMessage(from_users='kncio'))
async def alive_echo(event):
    if 'ping_alive' in event.raw_text:
        response = 'im_alive running with alert bitch'
        await client.send_message('me', response)

loop = asyncio.get_event_loop()
loop.create_task(clock())
loop.create_task(alert())
loop.run_forever()
