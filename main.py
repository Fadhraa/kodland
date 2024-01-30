import discord
from discord.ext import commands
from project import gen_pass, sampah_organic, sampah_anorganic
import random,os
# Variabel intents menyimpan hak istimewa bot
intents = discord.Intents.default()
# Mengaktifkan hak istimewa message-reading
intents.message_content = True
# Membuat bot di variabel klien dan mentransfernya hak istimewa
bot = commands.Bot(command_prefix='$', intents=intents)
sent_memes = set()
@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
@bot.command()
async def hello(ctx):
    await ctx.send(f"hi! im a bot {bot.user}")
@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
@bot.command()
async def password(ctx):
    await ctx.send("berikut password untuk anda")
    await ctx.send(gen_pass())
@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')
@bot.command()
async def repeat(ctx, times = 3, content="hello"):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def meme(ctx):
    meme_folder = "images"
    meme_files = os.listdir(meme_folder)

    if len(sent_memes) == len(meme_files):
        await ctx.send('Stok meme sudah habis.')
    else:
        while True:
            Gambar = random.choice(meme_files)
            if Gambar not in sent_memes:
                sent_memes.add(Gambar)
                with open(f'{meme_folder}/{Gambar}', 'rb') as f:
                    pic = discord.File(f)
                await ctx.send(file=pic)
                break
@bot.command()
async def say_hello(ctx):
    author = ctx.author
    await ctx.send(f"Hello {author.display_name}! I'm here to assist you.")

@bot.command()
async def organic(ctx):
    sampah = ''
    for i in sampah_organic:
        i = i +'\n'
        sampah += i
    await ctx.send('berikut daftar sampah organik')
    await ctx.send(sampah)
@bot.command()
async def anorganic(ctx):
    sampah = ''
    for i in sampah_anorganic:
        i = i +'\n'
        sampah += i
    await ctx.send('berikut daftar sampah anorganik')
    await ctx.send(sampah)

bot.run("MTE5NDI2NTE0MTM4NzIxNDkzMQ.GiOyro.CO9cCtNBu9upXFcpECBNGBWJDeARhsp1I6ZhGY")
