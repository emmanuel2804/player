from telethon import TelegramClient, events 
import time
import random
import asyncio
import stock
from utils import get_quest
from common_vars import *
from socket import gethostname, gethostbyname
from json import loads

loop = asyncio.get_event_loop()

# name = 'minion-click by text fixed'

name = 'tentaculo'

file = open('sessions.json', 'r')
sessions = loads(file.read())
file.close()
quest = sessions[name]['quest']

client=TelegramClient(name,sessions[name]['api_id'],sessions[name]['api_hash'])

client.start()

async def notify():
    await client.send_message(puesto_de_mando, 'alive ' + name)

@client.on(events.NewMessage(chats=(chatwars), incoming = True))
async def my_event_handler(event):
    if 'trying to pillage a local' in event.raw_text:
        time.sleep(random.randint(30, 120))
        buttons = await event.get_buttons() 
        for b_line in buttons: 
            for button in b_line: 
                if 'Intervene' in button.button.text: 
                    await button.click() 
        time.sleep(3)
    elif 'To accept their offer, you shall' in event.raw_text:
        time.sleep(random.randint(30, 50))
        await client.send_message(chatwars, '/pledge')
    elif 'You received:' in event.raw_text:
        await asyncio.sleep(random.randint(45,70))
        async with client.conversation(chatwars) as cnv:
            await cnv.send_message('🗺Quests')
            await asyncio.sleep(10)
            response = await cnv.get_response()
            await asyncio.sleep(10)
            await response.click(get_quest(quest))
            time.sleep(4)
    elif '/promo to' in event.raw_text:
        async with client.conversation(chatwars) as cnv:
            await stock.save_stock(cnv, client, None)
            await client.send_message(chatwars, '/g_def')

        await client.send_message(puesto_de_mando, 'estamina agotada')
    elif 'Stamina restored. You are ready for more adventures!' in event.raw_text:
        await asyncio.sleep(random.randint(45,65))
        async with client.conversation(chatwars) as cnv:
            await cnv.send_message('🗺Quests')
            await asyncio.sleep(10)
            response = await cnv.get_response()
            await asyncio.sleep(10)
            await response.click(get_quest(quest))
            time.sleep(4)
    # else:
    #     await deposit_stock(client)
    #     await client.send_message(chatwars, '/g_def')

@client.on(events.NewMessage(chats=(puesto_de_mando), incoming=True))
async def orders(event):
    if 'swamp' == event.raw_text:
        async with client.conversation(chatwars) as cnv:
            await cnv.send_message('🗺Quests')
            await asyncio.sleep(10)
            response = await cnv.get_response()
            await asyncio.sleep(10)
            await response.click(get_quest(quest))
            time.sleep(4)
            m = await cnv.get_response()
            await m.forward_to(puesto_de_mando)
    elif 'g_def' == event.raw_text:
        async with client.conversation(chatwars) as cnv:
            await stock.save_stock(cnv, client, None)
            await client.send_message(chatwars, '/g_def')
            time.sleep(4)
            m = await cnv.get_response()
            await m.forward_to(puesto_de_mando)

# para verificar que esta running
@client.on(events.NewMessage(from_users='kncio'))
async def commands(event):
    if 'ping_alive' in event.raw_text:
        hostname = gethostname() 
        host_ip = gethostbyname(hostname)
        response = 'im_alive running on ' + hostname + ': ' + host_ip + phone + name
        await client.send_message('kncio', response)
    if 'save_stock' in event.raw_text:
        async with client.conversation(chatwars) as cnv:
            await stock.save_stock(cnv, client, None)

loop.run_forever()