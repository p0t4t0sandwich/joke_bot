#!/bin/python3
#--------------------------------------------------------------------
# Project: Minecraft Joke Discord Bot
# Purpose: Get relevant information from Minecraft servers.
# Author: Dylan Sperrer (p0t4t0sandwich|ThePotatoKing)
# Date: 4AUGUST2021
# Updated: 4AUGUST2022 - p0t4t0sandwich
#   - Overhauled the entire codebase
#   - Converted to the requests library for API calls
#--------------------------------------------------------------------
# API documentation: https://api.mcsrvstat.us/
# Credit: Anders G. Jørgensen - spirit55555.dk

import discord
from discord.ext import commands
import requests
import os
import json
import curlify
import bot_library as b

path = "./joke_bot/"

class Joke_Bot():
    """
    Purpose:
        To handle all aspects of the Joke Bot.
    Pre-Conditions:
        None
    Post-Conditions:
        Handles all of the Bot's events and classes.
    Return:
        None
    """

    class Bot():
        """
        Purpose:
            To serve as a hacked-together extension of the discord.Client() class.
        Pre-Conditions:
            None
        Post-Conditions:
            Responds to the Bot's events.
        """
        def __init__(self, bot_id):
            self.bot_id = bot_id

        # Logging function to decrease clutter.
        def log(self, channel, author, content):
            b.bot_logger(path, "joke_bot", f'[{channel}] [{author}] {content}')

        def joke(self, channel, author, joke_type):
            """
            Purpose:
                To get jokes from various APIs.
            Pre-Conditions:
                :param channel: The discord server the message was sent in (message.guild)
                :param author: The Bot's name (discord.Client.user)
                :param joke_type: The joke_type user input.
            Post-Conditions:
                None
            Return:
                A discord.Embed object
            """
            if joke_type == "dad":
                res = requests.get("https://icanhazdadjoke.com/", headers={"Accept":"application/json"}).content.decode()
                title = "Dad Joke:"
                dct = json.loads(res)
                print(dct)
                joke = dct["joke"]
                print(dct["id"])
                description = f"{joke}"
                color = 0x65bf65

                # Log the output
                #self.log(channel, author, description)
            
            # # Error response
            # title = f"Error:"
            # description = f"Whoops, something went wrong,\ncouldn't reach {address}.\t¯\\\\_(\"/)\_/¯"
            # color = 0xbf0f0f

            # Output Discord Embed object
            #return discord.Embed(title = title, description = description, color = color)
            return description

        

        def run(self):
            """
            Purpose:
                The main handler of the Bot's events, plus handling setup and discord.Client.run().
            Pre-Conditions:
                :param bot_id: The Discord bot's super secret id.
            Post-Conditions:
                Responds to the Bot's events.
            Return:
                None
            """
            client = commands.Bot(command_prefix="!")

            # Startup response.
            @client.event
            async def on_ready():
                b.bot_logger(path, "joke_bot", f'We have logged in as {client.user}')

            # The !joke command and logging logic.
            @client.command()
            async def joke(ctx, address):
                channel = ctx.guild.name
                author = ctx.author
                content = ctx.message.content

                self.log(channel, author, content)
                statement = self.joke(channel, client.user, address)

                await ctx.send(embed=statement)

            client.remove_command('help')
            client.run(self.bot_id)


if __name__ == "__main__":
    #Joke_Bot.Bot(os.getenv("BOT_ID")).run()
    a = Joke_Bot.Bot("")
    joke = a.joke(channel="null", author="null", joke_type="dad")

    print(joke)

    # Consider a favorite joke command