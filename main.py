import json
import discord
from discord.ext import commands

with open("data.json", "r") as data_file:
    data_file = json.load(data_file)
    prefix = data_file['prefix']
    token = data_file['token']

client = commands.Bot(command_prefix=prefix)
client.load_extension("market_features")


@client.event
async def on_ready():
    print("Bot ready")


@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! Latency: {round(client.latency, 2) * 1000 } ms")

client.run(token)
