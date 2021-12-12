import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()


@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == "kayqueGovetri":
            print(
                f'{client.user} está conectado na guilda:\n'
                f'{guild.name}(id: {guild.id})'
            )
            break

client.run(TOKEN)
