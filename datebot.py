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
TOKEN = 'MTA0OTY0NTY0MTQwMTM3Mjc0NA.GxdSnr.KGFMgZuN6XlVvkpvYVta-96niVcZhjUuBvhfa0'
a = ["Я - бот, ты - бот)", "Easy peasy", "Apelsin4ik - мой создатель", "Apelsin4ik? bIades!", "<@748495964964388906> Струптер когда ВВ?", "WrendliWibe?", "WW3???", "Легенда в деле", "Vivarko - ✨ чел ты крутой ✨ ", "http://qrcoder.ru/code/?https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DdQw4w9WgXcQ%26ab_channel%3DRickAstley&3&0"]
d0 = date(2022, 6, 15)
today = date.today()
delta = today - d0
b_commands = '  | $    |data, |sex, |phrase, \n  | $    |call, |author, |donate, \n  | $    |help, |gif, |search, \n  | $    |watch, |git, |clear \n  | $    |web'
url = "https://github.com/dodik337"
url_donate = "не я ещё не настолько наглый \nчтобы у вас деньги просить, \nлучше дайти эти деньги страйдеру"
url_srch = "https://yandex.ru/search/?text="

#команды бота
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(embed = discord.Embed(description = f'** {ctx.author.name}, данной команды не существует.**', color=0x0c0c0c))
    elif isinstance(error, commands.CommandError):
        await ctx.send(embed = discord.Embed(description = f'** {ctx.author.name}, вы неправильно ввели команду.**', color=0x0c0c0c))

@bot.command()
async def clear(ctx, amount=9999):
    embed=discord.Embed(title="Удалено сообщений", description=amount, color=0xc83434)
    embed.set_author(name="Бот Евгений", icon_url="https://mobimg.b-cdn.net/v3/fetch/11/11a048e1dc27122485346049cd6d7c4f.jpeg")
    await ctx.channel.purge(limit=amount)
    if amount <=10:
        return
    else:
        await ctx.send(embed=embed)

@bot.command()
async def sex(ctx, arg):
    await ctx.send(f"{arg} был(а) выебан(а) смачно в попочку")
    await ctx.send('https://media.tenor.com/pF3s48bhdIsAAAAM/marin-kitagawa-anime-shy.gif')

@bot.command()
async def data(message):
    await message.channel.send(f"{delta.days} дней без WW3")

@bot.command()
async def phrase(message):
    b = random.choice(a)
    await message.channel.send(b)
    if b == a[9]:
        await message.channel.send(f"↑↑↑ Сканируй чтобы получить бесплатные робуксы ↑↑↑")

@bot.command()
async def call(message):
    await message.channel.send(f"<@748495964964388906> когда WW3?")

@bot.command()
async def search(ctx, *arg):
    arg = "-".join(arg)
    await ctx.send("https://media2.giphy.com/media/HdkzWcDvoRmLmkrWOt/giphy.gif?cid=ecf05e47ce1eo6kglj7hyvbjjmdpc3a5z5b939wlqzxwh97a&rid=giphy.gif&ct=g")
    time.sleep(2)
    await ctx.send(url_srch + arg)

@bot.command()
async def watch(ctx, *arg):
    arg = '-'.join(arg)
    await ctx.send(f"https://www.youtube.com/results?search_query={arg}")

@bot.command()
async def author(message):
    await message.channel.send(f"<@477170248479408141> - {url}")

@bot.command()
async def donate(message):
    await message.channel.send(url_donate)

@bot.command()
async def gif(ctx, *arg):
    arg = "-".join(arg)
    giffy = "https://giphy.com/"
    await ctx.send(giffy + arg)

@bot.command()
async def git(ctx):
    await ctx.send("https://github.com/dodik337/datebot-for-WW")

#@bot.command()
#async def web(ctx):
#    embed=discord.Embed(title="Вот наш прекрасный сайт!", url='http://wrendliwibe.pythonanywhere.com', color=0xc83434)
#    embed.set_author(name="WrendliWibe", icon_url="https://sun9-84.userapi.com/impg/FG8w3TVMuy11K5JeTkWVJsIQ3DO2eKfOuUk_lg/FNN1NNyxPak.jpg?size=1170x1163&quality=95&sign=d0f85dd39ae99575b464c43c1c255aeb&type=album")
#    await ctx.send(embed=embed)

@bot.command()      
async def help(ctx):
    embed=discord.Embed(title="Вот все мои команды", description=" ".join(b_commands), color=0xc83434)
    embed.set_author(name="bIades(Apelsin4ik_)", icon_url="https://mobimg.b-cdn.net/v3/fetch/11/11a048e1dc27122485346049cd6d7c4f.jpeg")
    await ctx.send(embed=embed)

#запуск

bot.run(token=TOKEN)
