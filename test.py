#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import www.orm as orm
import asyncio
from www.model import User, Blog, Comment

loop = asyncio.get_event_loop()

async def test():
    await orm.create_pool(user='root', password='password', database='awesome',loop=loop)

    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')

    await u.save()

loop.run_until_complete(test())