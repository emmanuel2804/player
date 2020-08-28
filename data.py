import json
import asyncio

async def load_resources_data():
    resources_codes = {}
    with open('data.json','r') as fd:
        resources_codes = json.load(fd)
    return resources_codes

