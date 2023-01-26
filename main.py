import json
import os
import re

import discord
import requests
from discord import Client, Intents, Interaction, app_commands
#from forex_python.bitcoin import BtcConverter
from discord.ext import commands, tasks

intents = discord.Intents.all()

client = discord.Client( intents=intents)
@client.event
async def on_message(message):
    print(message.content)
    msg = ""
    reaction= ""
    if 'in' == message.content.lower():
      msg = "and **Out**"
      reaction = "<:IAOTLogo:1045015878678360084>" 
    elif len([x for x in ['niga',"nigger","nigga","niger","nig", "black monkey"] if x in message.content.lower()])>0:
      msg = ""
      reaction = "👍🏿"
    elif 'ping' == message.content.lower():
      msg = "**pong**"
    elif len([x for x in ['help'] if x in message.content.lower()])>0 and "@" not in message.content.lower():
      msg = "<@&1043655353457451038>"
    
    if msg != "":
      await message.reply(msg)
    if reaction != "":
      await message.add_reaction(reaction)
        
bot = commands.Bot(command_prefix='', intents=intents,allowed_mentions = discord.AllowedMentions(everyone = True))
def check_me(token_test: str) -> dict:
    r = requests.get("https://discord.com/api/v10/users/@me", headers={
        "Authorization": f"Bot {token_test}"
    })

    return r.json()

print("\n".join([
    "starting..."
]))

@bot.event
async def on_ready():
    print("Bot Now Online!")
    print("\n".join([
        f"Logged in as {bot.user} (ID: {bot.user.id})",
        "",
        f"Use this URL to invite {bot.user} to your server:",
        f"https://discord.com/api/oauth2/authorize?client_id={bot.user.id}&scope=applications.commands%20bot"
    ]))
    #checkforvideos.start()
    


@bot.tree.command()
async def hello(interaction: Interaction):
  """ In and Out Trading """
  print(f"> {interaction.user} used the command.")
  await interaction.response.send_message("\n".join([
    f"Hi **<@{interaction.user.id}>**, thank you for saying **hello** to me.",
    "",
    "__**What is In and Out?**__",
    "<:IAOTLogo:1045015878678360084> **In And Out Trading**  is a trading team where we help each other in trading and discuss our ideas about the markets! <:IAOTLogo:1045015878678360084>",
    "",
    "<:rp:1044260758449557534> Our goal is to have a **disciplined** community, and build relationships <:rp:1044260758449557534>",
    "",
    f"<:illuminati:1046868311260020736>You can find more info about our channels in <#{1043655425637240853}> <:illuminati:1046868311260020736>",
    "",
    f":man_mage:Start **chatting** in <#{1043655431135957032}> :man_mage:"
    
  ]))
  
@bot.tree.command()
async def hey(interaction: Interaction):
  """ In and Out Trading """
  print(f"> {interaction.user} used the command.")
  await interaction.response.send_message("\n".join([
    f"Hi **<@{interaction.user.id}>**, thank you for saying **hello** to me.",
    "",
    "__**What is In and Out?**__",
    "<:IAOTLogo:1045015878678360084> **In And Out Trading**  is a trading team where we help each other in trading and discuss our ideas about the markets! <:IAOTLogo:1045015878678360084>",
    "",
    "<:rp:1044260758449557534> Our goal is to have a **disciplined** community, and build relationships <:rp:1044260758449557534>",
    "",
    f"<:illuminati:1046868311260020736>You can find more info about our channels in <#{1043655425637240853}> <:illuminati:1046868311260020736>",
    "",
    f":man_mage:Start **chatting** in <#{1043655431135957032}> :man_mage:"
      
  ]))


client.run("ODgyMjQxNjk1MjkzNTI2MTE2.GoBT5T.V8NcDoQbbbuVvLm8yxcK26FKVU2RUm-oPuDdlk")


