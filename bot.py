import discord
import os
import asyncio
import time

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)

guildids = ["489333893988745217", "520623784370110475", "518308389617401867"]
channelids = ["491621917204414466", "520831140324573184", "519849314168602643"]

@client.event
async def on_message(message):
    if message.author.server_permissions.administrator:
        return
    else:
        if message.channel.id not in channelids and message.server.id in guildids:
            def check(message):
                return message.content
            spam = await client.wait_for_message(author=message.author, channel= message.channel,check=check, timeout=1)
            spam1 = await client.wait_for_message(author=message.author, check=check, timeout=1, channel= message.channel)
            spam2 = await client.wait_for_message(author=message.author, check=check, timeout=1, channel= message.channel)
            await client.delete_message(spam)
            await client.delete_message(spam1)
            await client.delete_message(spam2)

client.run(os.environ['Token'])
