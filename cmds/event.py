import discord

from discord.ext import commands

from core.classes import Cog_Extension
from get_apexdata import get_data, get_overview
from read_file import read_setting

data = read_setting()


class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self, member):  # 當有人加入server
        # for channel in member.guild.channels:
        #     if str(channel) == "歡迎":  # 在歡迎的頻道內顯示
        channel = self.bot.get_channel(int(data["Welcome_channel_ID"]))
        await channel.send(f"""{member.mention}Welcome to the 玩拉哪次不玩!!!""")

    @commands.Cog.listener()
    async def on_member_remove(self, member):  # 當有人離開server
        channel = self.bot.get_channel(int(data["Welcome_channel_ID"]))
        await channel.send(f"""{member.mention}離開伺服器""")

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):  # 當使用者進入語音頻道
        channel = self.bot.get_channel(int(data["Channel_ID"]))  # 要發布訊息的頻道ID
        if str(after.channel) == "APEX":  # 當使用者進入語音頻道
            await channel.send(f"""APEX TIME!! {str(member.mention)}""")
        if str(before.channel) == "APEX":  # 當使用者離開語音頻道
            await channel.send(f"""{str(member.mention)}休息了""")

    # 處理"指令"發生的錯誤 Error Handler
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        # 檢查指令是否有自己的error handler:如果有就跳過
        if hasattr(ctx.command, "on_error"):
            return

        if isinstance(error, commands.errors.MissingRequiredArgument):
            await ctx.send("遺失參數")
        elif isinstance(error, commands.errors.CommandNotFound):
            await ctx.send("沒這指令哦")
        else:
            await ctx.send("發生錯誤")

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        # 新增反應貼圖獲取身分組
        # 判斷反應訊息是否為指定訊息
        if payload.message_id == 826027919112929290:
            if str(payload.emoji) == "<:cry:707537153336541185>":
                guild = self.bot.get_guild(payload.guild_id)  # 取得當前所在伺服器
                role = guild.get_role(826024319100125244)  # 取得伺服器指定的身分組
                await payload.member.add_roles(role)  # 給予該成員身分組
                await payload.member.send(f"你取得了{role}身分組!")

            if str(payload.emoji) == "<:surprised:707537153978138675>":
                guild = self.bot.get_guild(payload.guild_id)  # 取得當前所在伺服器
                role = guild.get_role(826024390130401321)  # 取得伺服器指定的身分組
                await payload.member.add_roles(role)  # 給予該成員身分組
                await payload.member.send(f"你取得了{role}身分組!")

            if str(payload.emoji) == "<:angry:707537153822818335>":
                guild = self.bot.get_guild(payload.guild_id)  # 取得當前所在伺服器
                role = guild.get_role(826024214162440212)  # 取得伺服器指定的身分組
                await payload.member.add_roles(role)  # 給予該成員身分組
                await payload.member.send(f"你取得了{role}身分組!")

            if str(payload.emoji) == "💩":
                guild = self.bot.get_guild(payload.guild_id)  # 取得當前所在伺服器
                role = guild.get_role(826023593376743444)  # 取得伺服器指定的身分組
                await payload.member.add_roles(role)  # 給予該成員身分組
                await payload.member.send(f"你取得了{role}身分組!")

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        # 新增反應貼圖取消身分組
        # 判斷反應訊息是否為指定訊息
        if payload.message_id == 826027919112929290:
            if str(payload.emoji) == "<:cry:707537153336541185>":
                guild = self.bot.get_guild(payload.guild_id)  # 取得當前所在伺服器
                user = guild.get_member(payload.user_id)  # 取得使用者ID
                role = guild.get_role(826024319100125244)  # 取得伺服器指定的身分組
                await user.remove_roles(role)  # 取消該成員身分組
                await user.send(f"你移除了{role}身分組!")

            if str(payload.emoji) == "<:surprised:707537153978138675>":
                guild = self.bot.get_guild(payload.guild_id)  # 取得當前所在伺服器
                user = guild.get_member(payload.user_id)  # 取得使用者ID
                role = guild.get_role(826024390130401321)  # 取得伺服器指定的身分組
                await user.remove_roles(role)  # 取消該成員身分組
                await user.send(f"你移除了{role}身分組!")

            if str(payload.emoji) == "<:angry:707537153822818335>":
                guild = self.bot.get_guild(payload.guild_id)  # 取得當前所在伺服器
                user = guild.get_member(payload.user_id)  # 取得使用者ID
                role = guild.get_role(826024214162440212)  # 取得伺服器指定的身分組
                await user.remove_roles(role)  # 取消該成員身分組
                await user.send(f"你移除了{role}身分組!")

            if str(payload.emoji) == "💩":
                guild = self.bot.get_guild(payload.guild_id)  # 取得當前所在伺服器
                user = guild.get_member(payload.user_id)  # 取得使用者ID
                role = guild.get_role(826023593376743444)  # 取得伺服器指定的身分組
                await user.remove_roles(role)  # 取消該成員身分組
                await user.send(f"你移除了{role}身分組!")



    @commands.Cog.listener()
    async def on_message(self, msg):
        if "常用英雄" in msg.content:
            input = msg.content
            data = get_data(input[4:])
            embed = discord.Embed(title=input[4:].strip() + "個人資料",
                                  url="https://apex.tracker.gg/apex/profile/origin/" + input[4:] + "/overview",
                                  description=data["title"], color=0xc12525)
            embed.set_thumbnail(url=data["pict_url"])
            embed.add_field(name=data["name1"], value=data["value1"], inline=True)
            embed.add_field(name=data["name2"], value=data["value2"], inline=True)
            embed.add_field(name=data["name3"], value=data["value3"], inline=True)
            await msg.channel.send(embed=embed)
        if "排位" in msg.content:
            input = msg.content
            data = get_overview(input[2:])
            embed = discord.Embed(title=input[2:].strip() + "個人資料",
                                  url="https://apex.tracker.gg/apex/profile/origin/" + input[2:] + "/overview",
                                  color=0x1cc45d)
            embed.set_thumbnail(url=data["url"])
            embed.add_field(name="排位", value=data["suptext"], inline=True)
            embed.add_field(name="分數", value=data["text"], inline=True)
            await msg.channel.send(embed=embed)

        if msg.content == "指令":
            embed = discord.Embed(title="指令說明", color=0xdbd514)
            embed.add_field(name="!ping", value="機器人延遲", inline=True)
            embed.add_field(name="!porn", value="porn picture", inline=True)
            embed.add_field(name="!clean num", value="刪除num個訊息", inline=True)
            embed.add_field(name="!sayd Hello", value="機器人發話，並標註所有人", inline=True)
            embed.add_field(name="常用英雄 Player", value="返回Player常用英雄數據", inline=True)
            embed.add_field(name="排位 Player", value="返回Player排位", inline=True)
            embed.add_field(name="!pump", value="當日PTT表特版抽一張圖", inline=True)
            embed.set_footer(text="身分組：請到身分組勾選確認")
            await msg.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Event(bot))
