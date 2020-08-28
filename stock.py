from telethon import TelegramClient, events 
import asyncio
from common_vars import *
from data import load_resources_data

# recibe una conversación de telethon y una lista de excepciones
# los recursos que no sean excepciones se depositan en el guild 
# los otros se venden a 1000g
async def save_stock(conv, client, exceptions):
    await conv.send_message('/stock')
    response  = await conv.get_response()
    await response.forward_to('Geckos_Bot')
    await asyncio.sleep(2)
    embeded_links = await client.get_messages('Geckos_Bot')
    links = embeded_links[0].text
    lines = links.split('\n')

    for line in lines:
        if not 'g_deposit' in line:
            continue

        s = line.split('%20')
        i_code = s[-2]
        i_amount = s[-1].split(')')[0]
        await client.send_message(chatwars, '/g_deposit ' + i_code + ' ' + i_amount)
        await asyncio.sleep(4)
    return True