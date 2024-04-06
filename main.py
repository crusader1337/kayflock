import disnake
from disnake.ext import commands
import psutil

intents = disnake.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='*', intents=intents)

@bot.slash_command()
async def test(interaction: disnake.AppCmdInter):
    await interaction.response.send_message("Test successful")

@bot.slash_command(name='textsong')
async def songtext(ctx: disnake.ApplicationCommandInteraction):
    await ctx.response.send_message("Don't run, don't trip")

@bot.slash_command(name='random')
async def random_number(ctx: disnake.ApplicationCommandInteraction):
    try:
        random_num = random.randint(1, 100)
        await ctx.response.send_message(f'Random number: {random_num}')
    except Exception as e:
        await ctx.response.send_message(f"An error occurred: {e}")

@bot.slash_command(name='developer')
async def developer_info(ctx: disnake.ApplicationCommandInteraction):
    await ctx.response.send_message("DEV Telegram @WVTTZ666")

@bot.slash_command(name='hello')
async def say_hello(ctx: disnake.ApplicationCommandInteraction):
    await ctx.response.send_message("YO CUZ")

@bot.slash_command(name='load')
async def bot_load(ctx: disnake.ApplicationCommandInteraction):
    cpu_percent = psutil.cpu_percent()
    memory_percent = psutil.virtual_memory().percent
    await ctx.response.send_message(f"CPU Usage: {cpu_percent}%\nMemory Usage: {memory_percent}%")

@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')

bot.run("MTIyNTg0MjkxNTgwNTM2NDI2NQ.GR6tBs.TSHHwkmWgiY9XX12xr3jEGE-I99Pn2ShjKPYOM")
