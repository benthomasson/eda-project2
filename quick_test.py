#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ansible_events_ui.manager import activate_rulesets
import asyncio

async def read_output(proc):

    done = False
    while not done:
        line =  await proc.stdout.readline()
        if len(line) == 0:
            break
        line = line.decode()
        print(f'{line}', end='')


async def main():

    print('start')

    with open('hello_events.yml') as f:
        rules = f.read()
    with open('inventory.yml') as f:
        inventory = f.read()
    with open('vars.yml') as f:
        extravars = f.read()
    print('activate')
    cmd, proc = await activate_rulesets('quay.io/bthomass/events-demo-ci-cd:latest', rules, inventory, extravars)
    print('running')

    print(f'pid {proc.pid}')

    task1 = asyncio.create_task(read_output(proc))

    await proc.wait()
    stdout, stderr = await proc.communicate()

    print(f'[{cmd!r} exited with {proc.returncode}]')

    await task1

asyncio.run(main())
