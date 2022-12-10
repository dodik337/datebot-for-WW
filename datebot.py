#импорт
import time
import discord
from discord.ext import commands
from datetime import date
import random
#переменные

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='|', intents=intents)
bot.remove_command('help')
client = discord.Client(intents=intents)
TOKEN = "BOT'S TOKEN"
a = ["Я - бот, ты - бот)", "Easy peasy", "Apelsin4ik - мой создатель", "Apelsin4ik? bIades!", "<@748495964964388906> Струптер когда ВВ?", "WrendliWibe?", "WW3???", "Легенда в деле", "Vivarko - ✨ чел ты крутой ✨ ", "http://qrcoder.ru/code/?https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DdQw4w9WgXcQ%26ab_channel%3DRickAstley&3&0"]
d0 = date(2022, 6, 15)
today = date.today()
delta = today - d0
b_commands = ["|d̶a̶t̶a̶", "|sex", "|phrase", "|call", "|author", "|donate", "|help", "|gif", "|search", "|watch"]
url = "https://github.com/dodik337"
url_donate = "не я ещё не настолько наглый \nчтобы у вас деньги просить, \nлучше дайти эти деньги страйдеру"
url_srch = "https://yandex.ru/search/?text="
nothing = " "

#команды бота

#@client.event
#async def on_ready():
#    print(f'We have logged in as {client.user}')

@bot.command()
async def sex(ctx, arg):
    await ctx.send(f"{arg} был(а) выебан(а) смачно в попочку")
    await ctx.send('https://media.tenor.com/pF3s48bhdIsAAAAM/marin-kitagawa-anime-shy.gif')

@bot.command()
async def data(message):
    await message.channel.send(f"{delta.days} дней без ВВ, \n PS: Скоро это изменится <3")

@bot.command()
async def phrase(message):
    b = random.choice(a)
    await message.channel.send(b)
    if b == a[9]:
        await message.channel.send(f"↑↑↑ Сканируй чтобы получить бесплатные робуксы ↑↑↑")

@bot.command()
async def call(message):
    await message.channel.send(f"<@748495964964388906> когда ВВ3?")

@bot.command()
async def search(ctx, arg):
    await ctx.send("https://media2.giphy.com/media/HdkzWcDvoRmLmkrWOt/giphy.gif?cid=ecf05e47ce1eo6kglj7hyvbjjmdpc3a5z5b939wlqzxwh97a&rid=giphy.gif&ct=g")
    time.sleep(2)
    await ctx.send(url_srch + arg)

@bot.command()
async def watch(ctx, arg):
    await ctx.send(f"https://www.youtube.com/results?search_query={arg}")

@bot.command()
async def author(message):
    await message.channel.send(url)

@bot.command()
async def donate(message):
    await message.channel.send(url_donate)

@bot.command()
async def gif(ctx, arg):
    giffy = "https://giphy.com/"
    await ctx.send(giffy + arg)

#@bot.command()
#async def translate(ctx, arg, arg2):
#    await ctx.send(f"")

@bot.command()
async def help(message):
    await message.channel.send(f"Вот все мои команды: \n {b_commands}")

#запуск

bot.run(token=TOKEN)
