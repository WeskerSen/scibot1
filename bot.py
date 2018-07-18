import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random

bot = commands.Bot(command_prefix='&')

@bot.event
async def on_ready():
    print ("Ready! Steady! and Go!")
    print ("Started " + bot.user.name)
    print ("ID: " + bot.user.id)

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color=0x00ff00)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def ownerinfo(ctx):
    embed = discord.Embed(title="Information about owner", description="Bot Name- SciBot", color=0x00ff00)
    embed.set_footer(text="Copyright@UK Soft")
    embed.set_author(name=" Bot Owner Name- DarkLegend")
    embed.add_field(name="Site- https://sciencetechnews.000webhostapp.com", value="Thanks for adding our bot", inline=True)
    await bot.say(embed=embed)

@bot.command()
async def add(left : int, right : int):
    """Adds two numbers together."""
    await bot.say(left + right)

@bot.command()
async def substract(left : int, right : int):
    """Adds two numbers together."""
    await bot.say(left - right)

@bot.command()
async def divide(left : int, right : int):
    """Adds two numbers together."""
    await bot.say(left / right)

@bot.command()
async def multiply(left : int, right : int):
    """Adds two numbers together."""
    await bot.say(left * right)
   
bot.run(os.env('Token'))
