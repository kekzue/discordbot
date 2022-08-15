import os
from discord.ext import commands
import discord
from dotenv import load_dotenv
from discord import Member
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import random
import asyncio
import json
import requests
import random

load_dotenv('DISCORD_TOKEN.env')#loads client secret from the .env file in the same directory
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='^') #change it to whatever you want
bot.remove_command("help")


@bot.command()
@commands.has_permissions(ban_members=True)#bans members if admin role is true
async def ban(ctx, user: discord.Member, *, reason="No reason provided"):
        await user.ban(reason=reason)
        ban = discord.Embed(title=f":boom: Banned {user.name}!", description=f"Reason: {reason}\nBy: {ctx.author.mention}",color=0xB026FF)
        await ctx.message.delete()
        await ctx.channel.send(embed=ban)
        await user.send(embed=ban)

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member, *, reason="No reason provided"):
        await user.kick(reason=reason)
        ban = discord.Embed(title=f":boot: Kicked {user.name}!", description=f"Reason: {reason}\nBy: {ctx.author.mention}",color=0xB026FF)
        await ctx.message.delete()
        await ctx.channel.send(embed=ban)
        await user.send(embed=ban)

@bot.command()## get mentioned users avatar
async def av(ctx, *,  avamember : discord.Member=None):
    userAvatarUrl = avamember.avatar_url
    await ctx.send(userAvatarUrl)
bot.command()##help command
async def help(ctx):
    em = discord.Embed(title="Tutorial Bot command list:", description="", color=0x2f3136)
    em.add_field(name="`^ban {user}`", value="Bans the user.")
    em.add_field(name="`^kick {user}`", value="Kicks user.")
    em.add_field(name="`^av {user}`", value="Gets the mentioned users pfp.")

    em.set_footer(text="GitHub Discord bot made by cyber")
    await ctx.send(embed=em)

client = discord.Client()

sad_words = ["sad", "depressed", "unhappy", "miserable", "depressing"]

racist_starter = ["im black", "i’m black", "african", "africa", "Im black", "I'm black"]

greeting_staretr = ["hi", "Hi","Hey", "hey", "hello", "Hello"]

homo_starter = ["im gay", "gay", "homosexual", "lets kiss", "bf", "kiss"]

homo_words = [
  "Ew no one likes gays",
  "Oh you're a fag",
  "No wonder your dad left, you are gay",
  "Hows the the life being a unliked gay?"
]

normal_starter = ["im straight", "straight", "I like girls", "gf", "girlfriend"]

normal_words = ["We love straight people",
               "Enjoy the server straight man"]

greeting_words = [
  "Hi Monkey Boy",
  "Stop say hi no one likes you",
  "Say hi to your dad, oh wait he's not in your life... hahahahaha"
]

racist_words = [
  "shut up monkey",
  "youre black stfu",
  "monkey boy"
]

starter_encourgements = [
  "die bitch",
  "hang yourself",
  "man up pussy",
  "thats why your father left",
  "gonna cry?",
  "fuck up pooron"
]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'
          .format(client))

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
          
        msg = message.content

        if message.content.startswith('$socials'):
          await message.channel.send('https://instagram.com/pxeq')


        if message.content.startswith('exchange'):
          await message.channel.send('exchanges fees are free , DM kekzue#2434')

        if message.content.startswith('bye'):
          await message.channel.send('bye nigga make sure to checkout https://instagram/kekzue and https://instagram.com/vensiraa')
        

        if any(word in msg for word in sad_words):
          await message.channel.send(random.choice
                                    (starter_encourgements))

        if any(word in msg for word in racist_starter):
          await message.channel.send(random.choice
                                    (racist_words))
        if any(word in msg for word in greeting_staretr):
          await message.channel.send(random.choice
                                    (greeting_words))
        if any(word in msg for word in homo_starter):
          await message.channel.send(random.choice
                                    (homo_words))
          

        if any(word in msg for word in normal_starter):
          await message.channel.send(random.choice
                                    (normal_words))
                                     
client.run('MTAwNzQwNDM2NDE3ODE0OTUwMg.GWADtQ.CHZvcM1_vfTO08cmSIfeM7osyxysyWk2-T20OQ')
