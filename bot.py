import os
import random
import discord
from discord.ext import commands

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# ----------------------
# Events
# ----------------------

@bot.event
async def on_ready():
    print(f"🐰 Logged in as {bot.user}")

# ----------------------
# Help Command
# ----------------------

@bot.command()
async def helpbun(ctx):
    embed = discord.Embed(
        title="🐰🍓 Bunny Bakery Commands",
        description="Cute little commands for every bunny!",
        color=0xFFC0CB
    )

    embed.add_field(
        name="💖 Affection",
        value="`!hug`\n`!kiss`\n`!cuddle`\n`!pat`\n`!boop`",
        inline=True
    )

    embed.add_field(
        name="🍰 Treats",
        value="`!cookie`\n`!cake`\n`!strawberry`\n`!tea`",
        inline=True
    )

    embed.add_field(
        name="🌸 Wholesome",
        value="`!compliment`\n`!comfort`\n`!cheer`",
        inline=True
    )

    embed.add_field(
        name="🐇 Bunny Specials",
        value="`!bunhug`\n`!feedbun`\n`!adoptbun`\n`!bunname`",
        inline=False
    )

    embed.add_field(
        name="🎀 Fun",
        value="`!bake`\n`!sprinkle`\n`!blush`\n`!sleep`",
        inline=False
    )

    embed.set_footer(text="Stay cozy in the Bunny Bakery 🧁✨")

    await ctx.send(embed=embed)

# ----------------------
# Affection Commands
# ----------------------

@bot.command()
async def hug(ctx, member: discord.Member = None):
    if member:
        await ctx.send(f"🤗 {ctx.author.mention} gives {member.mention} a warm bunny hug! 🐰💕")
    else:
        await ctx.send("🤗 *A fluffy bunny hug appears!*")

@bot.command()
async def kiss(ctx, member: discord.Member = None):
    if member:
        await ctx.send(f"💋 {ctx.author.mention} gives {member.mention} a sweet kiss! 💖")
    else:
        await ctx.send("💋 *A tiny bunny blows a kiss!*")

@bot.command()
async def cuddle(ctx, member: discord.Member = None):
    if member:
        await ctx.send(f"🧸 {ctx.author.mention} cuddles {member.mention}! 💕")
    else:
        await ctx.send("🧸 *The bunny curls up in a blanket.*")

@bot.command()
async def pat(ctx, member: discord.Member = None):
    if member:
        await ctx.send(f"🐾 {ctx.author.mention} gently pats {member.mention}!")
    else:
        await ctx.send("🐾 *Pat pat!*")

@bot.command()
async def boop(ctx, member: discord.Member = None):
    if member:
        await ctx.send(f"👉🐰 {ctx.author.mention} boops {member.mention}!")
    else:
        await ctx.send("👉🐰 *Boop!*")

# ----------------------
# Treat Commands
# ----------------------

@bot.command()
async def cookie(ctx, member: discord.Member = None):
    target = member.mention if member else "everyone"
    await ctx.send(f"🍪 {ctx.author.mention} gives a cookie to {target}!")

@bot.command()
async def cake(ctx, member: discord.Member = None):
    target = member.mention if member else "everyone"
    await ctx.send(f"🎂 {ctx.author.mention} shares cake with {target}!")

@bot.command()
async def strawberry(ctx, member: discord.Member = None):
    target = member.mention if member else "everyone"
    await ctx.send(f"🍓 {ctx.author.mention} gives a fresh strawberry to {target}!")

@bot.command()
async def tea(ctx, member: discord.Member = None):
    target = member.mention if member else "everyone"
    await ctx.send(f"🫖 {ctx.author.mention} serves tea to {target}!")

# ----------------------
# Wholesome Commands
# ----------------------

compliments = [
    "You're wonderful just the way you are! 💖",
    "You make the bakery brighter! ✨",
    "You're appreciated more than you know! 🌸",
    "You deserve all the cookies! 🍪",
    "Your vibe is immaculate! 🎀"
]

@bot.command()
async def compliment(ctx):
    await ctx.send(f"💖 {random.choice(compliments)}")

@bot.command()
async def comfort(ctx):
    await ctx.send("🧸 Everything will be okay. Have a warm blanket and a cookie. 🍪")

@bot.command()
async def cheer(ctx):
    await ctx.send("🎉 You're doing great! Keep going, bunny! 🐰✨")

# ----------------------
# Bunny Specials
# ----------------------

bunny_names = [
    "Strawberry Bun",
    "Mochi Bun",
    "Cupcake Hopper",
    "Marshmallow Bun",
    "Carrot Puff",
    "Sugar Bun"
]

@bot.command()
async def bunname(ctx):
    await ctx.send(f"🐰 Your bunny name is **{random.choice(bunny_names)}**!")

@bot.command()
async def bunhug(ctx):
    await ctx.send("🐰💕 A giant fluffy bunny hugs everyone!")

@bot.command()
async def feedbun(ctx):
    await ctx.send("🥕 You feed the bunny a carrot. The bunny is very happy!")

@bot.command()
async def adoptbun(ctx):
    await ctx.send("🐇 Congratulations! You adopted a tiny virtual bunny! 💖")

# ----------------------
# Fun Commands
# ----------------------

@bot.command()
async def bake(ctx):
    baked = random.choice([
        "🍪 Cookies",
        "🧁 Cupcakes",
        "🎂 Cake",
        "🥐 Pastries",
        "🍓 Strawberry Tart"
    ])

    await ctx.send(f"🍰 You baked: **{baked}**!")

@bot.command()
async def sprinkle(ctx, member: discord.Member = None):
    target = member.mention if member else ctx.author.mention
    await ctx.send(f"✨ Sprinkles rain down upon {target}! ✨")

@bot.command()
async def blush(ctx):
    await ctx.send("🌸 *blushes intensely* 🌸")

@bot.command()
async def sleep(ctx):
    await ctx.send("💤 The bunny curls up and falls asleep... 🐰")

# ----------------------
# Run Bot
# ----------------------

if not TOKEN:
    raise ValueError("No TOKEN variable found.")

bot.run(TOKEN)
