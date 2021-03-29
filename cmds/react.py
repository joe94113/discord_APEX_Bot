import random
import time

import discord

from discord.ext import commands

from core.classes import Cog_Extension
from read_file import read_setting, read_url
from get_beauty_url import get_beauty_data

data = read_setting()


class React(Cog_Extension):

    @commands.command()
    async def porn(self, ctx):
        url = random.choice(data["porn_url"])
        await ctx.send(url)

    @commands.command()
    async def pump(self, ctx):
        date = time.strftime("%m/%d").lstrip('0')
        urls = read_url()
        if urls[date]:
            url = random.choice(urls[date])
            await ctx.send(url)
        else:
            urls = get_beauty_data()
            url = random.choice(urls[date])
            await ctx.send(url)


def setup(bot):
    bot.add_cog(React(bot))
