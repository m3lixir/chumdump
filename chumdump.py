#!/usr/bin/env python3
import click
from modules.bait import bait_command
from modules.scramble import scramble_command
# from modules.purge import purge_command
# from modules.vanish import vanish_command

@click.group()
def chumdump():
    """🐟 chumdump — Chum the waters. Then disappear."""
    pass

chumdump.add_command(bait_command)
chumdump.add_command(scramble_command)
# chumdump.add_command(purge_command)
# chumdump.add_command(vanish_command)

if __name__ == "__main__":
    chumdump()
