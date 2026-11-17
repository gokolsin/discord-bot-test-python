import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(f"Бот {bot.user} успешно запущен!")

@bot.command()
async def привет(ctx):
    await ctx.send("Привет! Я работаю.")

bot.run("")