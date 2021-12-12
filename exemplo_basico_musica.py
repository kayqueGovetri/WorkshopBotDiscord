import os
import youtube_dl
from discord import FFmpegPCMAudio

from discord.ext import commands
from dotenv import load_dotenv
from discord.utils import get

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='?')

YDL_OPTIONS = {"format": "bestaudio", "noplaylist": "True"}
FFMPEG_OPTIONS = {
    "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5",
    "options": "-vn",
}

queues = {}
players = {}


@bot.command(name="join")
async def join(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        await channel.connect()


@bot.command(name="play", pass_context=True)
async def play(ctx, *, url: str):
    if ctx.author.voice:
        player = get(bot.voice_clients, guild=ctx.guild)
        players[ctx.message.guild.id] = player

        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        url_youtube = info["url"]

        options = FFmpegPCMAudio(url_youtube, **FFMPEG_OPTIONS)

        players[ctx.message.guild.id].play(
            options,
            after=lambda x=None: check_queues(ctx, ctx.message.guild.id),
        )
        await ctx.send(f'Bot está tocando a música: {info["title"]}')


@bot.command(name="resume")
async def resume(ctx):
    voice = get(bot.voice_clients, guild=ctx.guild)

    if not voice.is_playing():
        voice.resume()
        await ctx.send("Bot volta a tocar.")


@bot.command(name="pause")
async def pause(ctx):
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice.is_playing():
        voice.pause()
        await ctx.send("Bot está sendo pausado.")


@bot.command(name="stop")
async def stop(ctx):
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice.is_playing():
        voice.stop()
        await ctx.send("Parando o bot.")


def check_queues(ctx, id):
    if queues[id]:
        source = queues[id].pop(0)
        players[id].play(
            source,
            after=lambda x=None: check_queues(ctx, ctx.message.guild.id),
        )


bot.run(TOKEN)
