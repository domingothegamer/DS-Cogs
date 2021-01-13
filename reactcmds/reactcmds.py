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


log = logging.getLogger("red.trusty-cogs.reactcmds")
_ = Translator("ReactCmds", __file__)




@cog_i18n(_)
class ReactCmds(ReactEvents, commands.Cog):

    __author__ = ["domingothegamer"]
    __version__ = "1.0.0"

    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=218773382617890828, force_registration=True)
        self.config.register_global(version="0.0.0")
        default_guild = {
            "reaction_roles": {},
            "auto_roles": [],
        }
        default_role = {
            "sticky": False,
            "auto": False,
            "reactions": [],
            "selfassignable": False,
            "selfremovable": False,
        }
        default_member = {"sticky_roles": []}
        self.config.register_guild(**default_guild)
        self.config.register_role(**default_role)
        self.config.register_member(**default_member)
        self.settings = {}

    async def initialize(self):
        
        self.settings = await self.config.all_guilds()
