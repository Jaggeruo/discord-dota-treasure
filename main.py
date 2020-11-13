import json
import discord
from discord.ext import commands
import os


with open("data/data.json", "r") as data_file:
    data_dict = json.load(data_file)
    prefix = data_dict['prefix']
    token = data_dict['token']
    data_file.close()

client = commands.Bot(command_prefix=prefix, case_insensitive=True)
client.remove_command("help")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online,
                                 activity=discord.Game("Dota2 market"))
    print("Bot ready")


@client.command(aliases=["quit"])
@commands.is_owner()
async def shutdown(ctx):
    await client.logout()
    print("Bot closed")


@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! Latency: {round(client.latency, 2) * 1000 } ms")


@client.command()
@commands.has_permissions(administrator=True)
async def setprefix(ctx, prefix):

    if(len(prefix) >= 2):
        await ctx.send("Only one character prefix.")
    else:
        with open("data/data.json", "w") as data_file:
            data_dict["prefix"] = prefix
            json.dump(data_dict, data_file, ensure_ascii=True, indent=4)

        client.command_prefix = prefix

        await ctx.send(f"New prefix: {prefix}")


client.run(token)
