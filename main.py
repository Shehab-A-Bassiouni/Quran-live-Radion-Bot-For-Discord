import os
import discord
from discord.ext import commands
from discord import FFmpegPCMAudio


def run():
  intents = discord.Intents.all()
  intents.message_content = True
  bot = commands.Bot(command_prefix="$", intents=intents)

  @bot.event
  async def on_ready():
    print("Radio Bot is Ready")

  @bot.command(name="play")
  async def play(ctx):
    channel = ctx.message.author.voice.channel
    player = await channel.connect()
    player.play(FFmpegPCMAudio("<API>"))

 # playing custome local file
  @bot.command(name="playc")
  async def play(ctx):
    channel = ctx.message.author.voice.channel
    player = await channel.connect()
    player.play(FFmpegPCMAudio("<cutome path>"))

  @bot.command(name="stop")
  async def stop(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    voice.stop()
    await voice.disconnect()

  bot.run(
      "<your bot token>"
  )


if __name__ == "__main__":
  run()


