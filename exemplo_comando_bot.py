import os
import random

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='?')


@bot.command(name="speak")
async def speak(ctx):
    fire_keeper_dialogue = [
        """
Welcome to the bonfire, Unkindled One.
I am a Fire Keeper.
I tend to the flame, and tend to thee.
The Lords have left their thrones, and must be deliver'd to them.
To this end, I am at thy side.
""",
    """
Produce the coiled sword at the bonfire.
The mark of ash will guide thee to the land of the Lords.
To Lothric, where the homes of the Lords converge.
    """,
    """
The First Flame quickly fades.
Darkness will shortly settle.
But one day, tiny flames will dance across the darkness.
Like embers, linked by lords past."
Ashen one, hearest thou my voice, still? 
    """
    ]

    response = random.choice(fire_keeper_dialogue)
    await ctx.send(response)

bot.run(TOKEN)
