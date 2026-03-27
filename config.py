#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8763521420:AAHk2Z5zuyQ-AVcxCSpWVRaYatqTSTHGbEA")
    API_ID = int(os.environ.get("API_ID", "30296254"))
    API_HASH = os.environ.get("API_HASH", "c2b5306f4ccd2d795405a026c10b4c62")
    AUTH_USERS = "7660916897"

