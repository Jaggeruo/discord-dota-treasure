import discord
from discord.ext import commands
from datetime import datetime


class ErrorCog(commands.Cog, name="Error"):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        try:
            if hasattr(ctx.command, "on_error"):
                return
            else:
                embed = discord.Embed(
                    title=f"Error in commnad: {ctx.command}", description=f"Correct syntax: '{ctx.command.qualified_name} {ctx.command.signature}'\nError: {error}", color=0xbc61d7)
                embed.set_footer(
                    text=datetime.now().strftime("%d.%m.%Y %H:%M:%S"))
                await ctx.send(embed=embed)

        except:
            embed = discord.Embed(
                title=f"Error in commnad: {ctx.command}",
                description=f"If you see this something unexpected occured.\n{error}", colour=0xbc61d7)
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(ErrorCog(client))
