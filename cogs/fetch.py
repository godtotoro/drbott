import discord
from discord.ext import commands


class Fetch:
    """Fetching stuff"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def 給(self, user: discord.Member, *, stuff):
        """Fetches stuff to user"""

        await self.bot.say(user.mention+"這是你的 " + stuff)


def setup(bot):
    bot.add_cog(Fetch(bot))
