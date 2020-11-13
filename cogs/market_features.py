from discord.ext import commands
import discord
from steam_community_market import Market, AppID
from datetime import datetime


class market_features(commands.Cog, name="Market_features"):
    def __init__(self, client):
        self.client = client
        self.currency = "PLN"
        self.market = Market(self.currency)

    @commands.command()
    async def treasure(self, ctx, year):
        chest = ["Immortal Treasure I ",
                 "Immortal Treasure II ", "Immortal Treasure III "]

        for item in chest:
            self.price = self.market.get_prices(item + year, AppID.DOTA2)

            embed = discord.Embed(
                title=f"{item} {year}", description=f"Lowest price: {self.price['lowest_price']} {self.currency}\nAverage price: {self.price['median_price']} {self.currency}", color=0x00ff00)
            embed.set_footer(
                text=datetime.now().strftime("%d.%m.%Y %H:%M:%S"))
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(market_features(client))
