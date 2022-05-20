#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ansible_events_ui.manager import activate_rulesets
import asyncio


async def main():

    with open('hello_events.yml') as f:
        rules = f.read()
    with open('inventory.yml') as f:
        inventory = f.read()
    with open('vars.yml') as f:
        extravars = f.read()
    await activate_rulesets('quay.io/bthomass/events-demo-ci-cd:latest', rules, inventory, extravars)


asyncio.run(main())
