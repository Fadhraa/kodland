import discord
from discord.ext import commands
from password_generator import gen_pass
# Variabel intents menyimpan hak istimewa bot
intents = discord.Intents.default()
# Mengaktifkan hak istimewa message-reading
intents.message_content = True
# Membuat bot di variabel klien dan mentransfernya hak istimewa
bot = commands.Bot(command_prefix='$', intents=intents)

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
async def repeat(ctx, times = 3, content=(discord.Member.message)):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)
bot.run("MTE5NDI2NTE0MTM4NzIxNDkzMQ.G6MUZg.D7qeMt-52EDKcVnEcQw6lk2OQ91X1VkEVwhSBU")
