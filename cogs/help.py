import discord
from discord.ext import commands


class Help(commands.Cog, name="Help"):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(
            title="Command list", description="prefix `.`\n\n**`.help`**\nShows this message\n\n**`.ping`**\nShows latency\n\n**`.setprefix <prefix>`**\nSets new prefix\n\n**`.treasure <rok>`**\nShows prices of Immortal Treasure I, II and III", color=0xbc61d7)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Help(client))
