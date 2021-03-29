import discord
from discord.ext import commands

from core.classes import Cog_Extension


class Main(Cog_Extension):

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"延遲；{round(self.bot.latency * 1000)}(ms)")

    @commands.has_permissions(administrator=True)
    @commands.command()
    async def sayd(self, ctx, *, msg):
        await ctx.message.delete()
        await ctx.send(f'本訊息為聊天室廣播,故標記 @everyone \n {msg}')

    @commands.has_permissions(administrator=True)
    @commands.command()
    async def clean(self, ctx, num: int):
        await ctx.channel.purge(limit=num+1)


def setup(bot):
    bot.add_cog(Main(bot))
