#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ansible_events_ui.manager import activate_rulesets
import asyncio
import requests


async def main():

    with open("hello_events.yml") as f:
        rules = f.read()
    with open("inventory.yml") as f:
        inventory = f.read()
    with open("vars.yml") as f:
        extravars = f.read()

    try:
        r = requests.post(
            "http://localhost:8000/rulesetbook/", json=dict(name="hello", rules=rules)
        )
        rules_id = r.json()["id"]
        r = requests.post(
            "http://localhost:8000/inventory/",
            json=dict(name="hello", inventory=inventory),
        )
        inventory_id = r.json()["id"]
        r = requests.post(
            "http://localhost:8000/extravars/",
            json=dict(name="hello", extravars=extravars),
        )
        extravars_id = r.json()["id"]
        r = requests.post(
            "http://localhost:8000/activation/",
            json=dict(
                name="hello",
                rulesetbook_id=rules_id,
                inventory_id=inventory_id,
                extravars_id=extravars_id,
            ),
        )
        activation_id = r.json()["id"]
        print(rules_id, inventory_id, extravars_id, activation_id)
    except Exception as e:
        print(r.url)
        print(r.json())


asyncio.run(main())
