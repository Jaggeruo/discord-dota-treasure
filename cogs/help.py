import discord
from discord.ext import commands
from datetime import datetime


class Help(commands.Cog, name="Help"):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(
            title=f"Spis komend", description=f"prefix `.`\n\n**`.help`**\nPokazuje tę wiadomość\n\n**`.ping`**\nPokazuje opóźnienie bota\n\n**`.setprefix <prefix>`**\nUstawia nowy prefix\n\n**`.treasure <rok>`**\nPokazuje ceny Immortal Treasure I, II i III podanego roku", color=0xbc61d7)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Help(client))
