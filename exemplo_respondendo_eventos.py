import os
import random

from discord import Client
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

client = Client()


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    fire_keeper_dialogue = [
        """
Welcome to the bonfire, Unkindled One. \n
I am a Fire Keeper. \n
I tend to the flame, and tend to thee. \n
The Lords have left their thrones, and must be deliver'd to them. \n
To this end, I am at thy side.
""",
    """
Produce the coiled sword at the bonfire. \n
The mark of ash will guide thee to the land of the Lords.\n
To Lothric, where the homes of the Lords converge.
    """,
    """
The First Flame quickly fades. \n
Darkness will shortly settle. \n
But one day, tiny flames will dance across the darkness. \n
Like embers, linked by lords past." \n
Ashen one, hearest thou my voice, still? 
    """
    ]

    if message.content == 'fire keeper':
        response = random.choice(fire_keeper_dialogue)
        await message.channel.send(response)

client.run(TOKEN)
