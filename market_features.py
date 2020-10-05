from discord.ext import commands
import discord
from steam_community_market import Market, AppID


class market_features(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.market = Market("PLN")

    @commands.command()
    async def skarb(self, ctx, year):
        skrzynki = ["Immortal Treasure I ",
                    "Immortal Treasure II ", "Immortal Treasure III "]
        for item in skrzynki:
            self.price = self.market.get_prices(item + year, AppID.DOTA2)
            await ctx.send(f"{item}:\nNajniższa cena: {self.price['lowest_price']} zł\nŚrednia cena: {self.price['median_price']} zł")


def setup(client):
    client.add_cog(market_features(client))
