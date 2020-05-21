#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import math
import os
import time

from tobrot import (
    FINISHED_PROGRESS_STR,
    UN_FINISHED_PROGRESS_STR
)


async def progress_for_pyrogram(
    current,
    total,
    ud_type,
    message,
    start
):
    now = time.time()
    diff = now - start
    if diff % 10 < 0.3 or current == total:
        percentage = current * 100 / total
        speed = current / diff
        time_to_completion = time_formatter(int((total - current) / speed))
        progress_str = \
            "__{}__ : `{}`\n" + \
            "```[{}{}]```\n" + \
            "**Progress** : `{}%`\n" + \
            "**Completed** : `{}`\n" + \
            "**Total** : `{}`\n" + \
            "**Speed** : `{}/s`\n" + \
            "**ETA** : `{}`"
        progress_str = progress_str.format(
            ud_type,
            file_name,
            ''.join(["█" for i in range(floor(percentage / 5))]),
            ''.join(["░" for i in range(20 - floor(percentage / 5))]),
            round(percentage, 2),
            humanbytes(current),
            humanbytes(total),
            humanbytes(speed),
            time_to_completion if time_to_completion else "0 s")
        try:
            await message.edit(progress_str)
        except MessageNotModified:
            pass
        except FloodWait as f_e:
            time.sleep(f_e.x)
