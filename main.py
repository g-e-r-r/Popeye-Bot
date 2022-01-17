import os
import discord
from discord.ext import commands
import datetime
from urllib import parse, request
import re
import keep_alive

token = os.environ['token']
bot = commands.Bot(command_prefix="<", description="This is a multifunction bot")
@bot.command()
async def ping(ctx):
    await ctx.send("Pong")

@bot.command()
async def sum(ctx, numOne: int, numTwo: int):
    await ctx.send(numOne + numTwo)

@bot.command()
async def stats(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="This is HARAM PLACE", timestamp=datetime.datetime.utcnow(), color=discord.Color.green())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    await ctx.send(embed=embed)

@bot.command()
async def rules(ctx):
    embed2 = discord.Embed(title=f"{ctx.guild.name}", description="Help", timestamp=datetime.datetime.utcnow(), color=discord.Color.green())
    embed2.add_field(name="Rule 1", value="No griefing")
    embed2.add_field(name="Rule 2", value="Usa cada canal correctamente")
    await ctx.send(embed=embed2)

@bot.command()
async def youtube(ctx, *, search):
    query_string = parse.urlencode({"search_query": search})
    html_content = request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall('watch\?v=(.{11})',html_content.read().decode('utf-8'))
    await ctx.send("https://youtube.com/watch?v=" + search_results[0])

#Events
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="<help", url="https://www.twitch.tv/itsgerliz"))
    print("bot is alive")

keep_alive.keep_alive()

bot.run(token)
