from .reactcmds import ReactCmds

async def setup(bot):
    cog = ReactCmds(bot)
    bot.add_cog(cog)
    await cog.initialize()
