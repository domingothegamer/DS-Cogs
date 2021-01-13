import asyncio
import logging

from typing import Optional, Union

import discord
from redbot.core import Config, commands
from redbot.core.i18n import Translator, cog_i18n
from redbot.core.commands import Context
from redbot.core.utils.chat_formatting import pagify, humanize_list
from redbot.core.utils.predicates import ReactionPredicate
from redbot.core.utils.menus import start_adding_reactions

from .events import ReactEvents

default_settings = {
    "ENABLED": False,
    "ROLE": [],
    "CHANNELS": []
}


log = logging.getLogger("red.ds-cogs.reactcmds")
_ = Translator("ReactCmds", __file__)




@cog_i18n(_)
class ReactCmds(ReactEvents, commands.Cog):

    __author__ = ["domingothegamer"]
    __version__ = "1.0.0"

    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=451690489)
        self.config.register_global(version="0.0.0")
        self.config.register_guild(**default_settings)
        self.settings = {}

    async def initialize(self):

        self.settings = await self.config.all_guilds()
