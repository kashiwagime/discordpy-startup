from discord.ext import commands
import os
import traceback

import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@bot.event
async def on_message(message):
    try:
        if message.author.bot:
            return
        await bot.process_commands(message)
    except Exception:
        await message.channel.send(f'```\n{traceback.format_exc()}\n```')
async def on_command_error(ctx, error):
    await ctx.send(str(error))


@bot.command()


bot.run(token)
