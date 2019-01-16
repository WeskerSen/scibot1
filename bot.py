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
linkids = ["491281612642713602", "509247504382951424", "508208698615660544", "508208902446383105", "508226756356997141"]
banned_sites = ["https://", "http://"]

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.author.server_permissions.administrator:
        return
    else:
        if message.channel.id not in channelids and message.server.id in guildids:
            def check(message):
                return message.content
            spam = await client.wait_for_message(author=message.author, channel= message.channel,check=check, timeout=2)
            spam1 = await client.wait_for_message(author=message.author, check=check, timeout=2, channel= message.channel)
            spam2 = await client.wait_for_message(author=message.author, check=check, timeout=2, channel= message.channel)
            await client.delete_message(spam)
            await client.delete_message(spam1)
            await client.delete_message(spam2)
        if message.channel.id not in linkids and message.server.id in guildids and banned_sites in message.content:
            await client.delete_message(message)
            await client.send_message(message.channel, f'Do not post link {message.author.name}')

client.run(os.environ['Token'])
