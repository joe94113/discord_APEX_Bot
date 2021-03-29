import discord
import json
import asyncio
import datetime

from discord.ext import commands

from core.classes import Cog_Extension


class Task(Cog_Extension):
    def __init___(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # 父類別，初始化屬性

        async def interval():
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(824520694590210082)
            while not self.bot.is_closed():
                await self.channel.send("起來嗨")
                await asyncio.sleep(2)

    @commands.command()
    async def set_channel(self, ctx, ch: int):
        self.channel = self.bot.get_channel(ch)
        await ctx.send(f"Set Channel：{self.channel.mention}")


def setup(bot):
    bot.add_cog(Task(bot))
