import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Загружаем переменные из файла .env
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    # Синхронизируем слэш-команды, чтобы они появились в меню Discord
    await bot.tree.sync()
    print(f"Бот {bot.user} успешно запущен и команды синхронизированы!")

# Создаем настоящую слэш-команду
@bot.tree.command(name="привет", description="Поздороваться с ботом")
async def hello_command(interaction: discord.Interaction):
    await interaction.response.send_message("Привет! Я работаю.")

bot.run(TOKEN)