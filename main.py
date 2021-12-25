import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

bot = commands.Bot(command_prefix='..')

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

print('Bot is running...')
bot.run(TOKEN)
print('Terminating...')