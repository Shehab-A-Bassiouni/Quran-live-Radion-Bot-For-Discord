import os
import logging
import settings
import discord
from discord.ext import commands
from discord import FFmpegPCMAudio

logger = settings.logging.getLogger("bot")

def run():
    intents = discord.Intents.all()
    intents.message_content=True
    bot = commands.Bot(command_prefix=settings.DISCORD_PREFIX , intents=intents)



    @bot.event
    async def on_ready():
        logger.info(f"User: {bot.user} (ID: {bot.user.id})")
        print("The Muslim Bot is Ready")


    @bot.command(
        aliases=['p'],
        help="write '!play' to play the quran radio station from cairo",
        description = "write '!play' to play the quran radio station from cairo",
        brief="quran radio station from cairo"
    )
    async def play(ctx):
        channel = ctx.message.author.voice.channel
        global player
        try:
            player = await channel.connect()
        except:
            pass
        player.play(FFmpegPCMAudio(settings.API_QURAN_RADIO_STATION_EGYPT))

    @bot.command(name="stop")
    async def stop(ctx):
        voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
        voice.stop()
        await voice.disconnect()


    
        

    bot.run(settings.DISCORD_API_SECRET_TOKEN , root_logger=True)

if __name__ == "__main__":
    run()