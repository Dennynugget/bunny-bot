TOKEN = "MTQ5MDA5MTE3NjM1ODA1NjA2OA.GPBWmF.cRwYT1nPGwkGWSmkgG5rT0DOnOWDTIRLSoPzw0"
import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# 🌸 Cute responses
compliments = [
    "You're as sweet as strawberry cake 🍓",
    "You light up the bakery 💖",
    "Certified cutie detected ✨",
    "You're doing amazing, keep going 🌸",
    "You're softer than a fresh bun 🐰"
]

comforts = [
    "It's okay, you're safe here 🫶",
    "Take a deep breath, you got this 🌸",
    "The bakery is always here for you 🐰",
    "Sending you warm hugs and soft vibes 💖"
]

desserts = [
    "You baked a strawberry shortcake 🍰",
    "You made cute bunny cookies 🍪",
    "You created a magical pastel cupcake 🧁",
    "You baked a heart-shaped cake 💕"
]

bun_names = [
    "Mochi", "Peaches", "Bunbun", "Cotton", "Snowdrop", "Honey", "Pudding"
]

# 🐰 Events
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

# 💖 Affection Commands
@bot.command()
async def hug(ctx, member: discord.Member):
    await ctx.send(f"{ctx.author.mention} gives {member.mention} a warm hug 🤗")

@bot.command()
async def kiss(ctx, member: discord.Member):
    await ctx.send(f"{ctx.author.mention} gives {member.mention} a soft kiss 💋")

@bot.command()
async def cuddle(ctx, member: discord.Member):
    await ctx.send(f"{ctx.author.mention} cuddles {member.mention} 🧸")

@bot.command()
async def pat(ctx, member: discord.Member):
    await ctx.send(f"{ctx.author.mention} gives {member.mention} gentle headpats 🐾")

@bot.command()
async def boop(ctx, member: discord.Member):
    await ctx.send(f"{ctx.author.mention} boops {member.mention}'s nose 👉🐰")

# 🍪 Treat Commands
@bot.command()
async def cookie(ctx, member: discord.Member):
    await ctx.send(f"{ctx.author.mention} gives {member.mention} a fresh cookie 🍪")

@bot.command()
async def cake(ctx, member: discord.Member):
    await ctx.send(f"{ctx.author.mention} shares cake with {member.mention} 🍰")

@bot.command()
async def strawberry(ctx, member: discord.Member):
    await ctx.send(f"{ctx.author.mention} gives {member.mention} a sweet strawberry 🍓")

@bot.command()
async def tea(ctx, member: discord.Member):
    await ctx.send(f"{ctx.author.mention} pours tea for {member.mention} 🫖")

# 🌸 Wholesome
@bot.command()
async def compliment(ctx, member: discord.Member):
    await ctx.send(f"{member.mention}, {random.choice(compliments)}")

@bot.command()
async def comfort(ctx, member: discord.Member):
    await ctx.send(f"{member.mention}, {random.choice(comforts)}")

@bot.command()
async def cheer(ctx, member: discord.Member):
    await ctx.send(f"{ctx.author.mention} cheers for {member.mention}! 🎉")

# 🐰 Bunny Specials
@bot.command()
async def bunhug(ctx, member: discord.Member):
    await ctx.send(f"A tiny bunny hops over and hugs {member.mention} 🐰💖")

@bot.command()
async def feedbun(ctx, member: discord.Member):
    await ctx.send(f"{ctx.author.mention} gives {member.mention} a crunchy carrot 🥕")

@bot.command()
async def adoptbun(ctx):
    name = random.choice(bun_names)
    await ctx.send(f"You adopted a tiny bunny named **{name}** 🐰💖")

@bot.command()
async def bunname(ctx):
    await ctx.send(f"Your bunny name is **{random.choice(bun_names)}** 🐰")

# 🎀 Fun
@bot.command()
async def bake(ctx):
    await ctx.send(random.choice(desserts))

@bot.command()
async def sprinkle(ctx, member: discord.Member):
    await ctx.send(f"{member.mention} is covered in sparkles ✨")

@bot.command()
async def blush(ctx, member: discord.Member):
    await ctx.send(f"{member.mention} is blushing! 😊")

@bot.command()
async def sleep(ctx):
    await ctx.send("You fell asleep in the bakery… sweet dreams 😴")

# 🚀 Run bot
TOKEN = "MTQ5MDA5MTE3NjM1ODA1NjA2OA.GPBWmF.cRwYT1nPGwkGWSmkgG5rT0DOnOWDTIRLSoPzw0"
bot.run(TOKEN)
