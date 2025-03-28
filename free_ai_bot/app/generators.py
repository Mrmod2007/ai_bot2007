from config import AI_TOKEN
# Asynchronous Example
import asyncio
from mistralai import Mistral
import os

async def generate(content):

    async with Mistral(
        api_key=AI_TOKEN,
    ) as mistral:

        res = await mistral.chat.complete_async(model="mistral-small-latest", messages=[
            {
                "content": content,
                "role": "user",
            },
        ])

        if res is not None:
            return res
