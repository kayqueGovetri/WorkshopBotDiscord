import os
import random

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='?')


@bot.event
async def on_reaction_add(reaction, user):
    channel = reaction.message.channel
    await channel.send(f'{user.name} adicionou {reaction.emoji} na mensagem: {reaction.message.content}')


@bot.event
async def on_reaction_remove(reaction, user):
    channel = reaction.message.channel
    await channel.send(f'{user.name} removeu {reaction.emoji} na mensagem: {reaction.message.content}')


bot.run(TOKEN)
