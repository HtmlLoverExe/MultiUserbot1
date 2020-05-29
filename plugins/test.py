import configparser
import time

from pyrogram import Client, Filters

config = configparser.ConfigParser()
config.read("config.ini")
prefixes = list(config["prefixes"].keys())

@Client.on_message(Filters.user("self") & Filters.command("test", prefixes=prefixes))
def test_command(c, msg):
 import random
numcasuale=str(random.randint(0,100))
print("You are " + numcasuale + " %gay!")



print("[MultiUserbot] Loaded \"test.py\" plugin")
