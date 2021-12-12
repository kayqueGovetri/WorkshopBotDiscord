import os

from discord import Client, utils
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = Client()


@client.event
async def on_ready():
    guild = utils.find(lambda g: g.name == "kayqueGovetri", client.guilds)
    print(
        f'{client.user} está conectado na guilda:\n'
        f'{guild.name}(id: {guild.id})'
    )
