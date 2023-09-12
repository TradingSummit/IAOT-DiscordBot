import discord
from discord import app_commands
from discord.ext import commands, tasks
import asyncio

intents = discord.Intents.all()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@tree.command(name = "hello", description = "Let's begin!", guild=discord.Object(id=1043655320733491362))
async def first_command(interaction):
    await interaction.response.send_message("\n".join([
    f"Hi **<@{interaction.user.id}>**, thank you for saying **hello** to me.",
    "", "__**What is In and Out?**__",
    "<:IAOTLogo:1045015878678360084> **In And Out Trading**  is a trading team where we help each other in trading and discuss our ideas about the markets! <:IAOTLogo:1045015878678360084>",
    "",
    "<:rp:1044260758449557534> Our goal is to have a **disciplined** community, and build relationships <:rp:1044260758449557534>",
    "",
    f"<:illuminati:1046868311260020736>You can find more info about our channels in <#{1043655425637240853}> <:illuminati:1046868311260020736>",
    "", f":man_mage:Start **chatting** in <#{1043655431135957032}> :man_mage:"
  ]))
    
@tree.command(name = "help", description = "I will help you!", guild=discord.Object(id=1043655320733491362))
async def first_command(interaction):
    await interaction.response.send_message(f"If you need any help, feel free to open a ticket in <#{1043655432234876948}>")   

@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=1043655320733491362))
    await reminder()

    print("Ready!")
TIMER = 7195
from datetime import datetime


async def reminder():
    print("timer started")
    while True:
        global TIMER
        TIMER +=1
        if TIMER == 7200:
            TIMER = 0
            now = datetime.utcnow()
            channel = client.get_channel(1043655461238476913)
            print("done")
            if now.hour >4 and now.hour <=22:
                await channel.send("<@&1043655353457451038> bump please")
            else:
                await channel.send("<@&1044711196605026354> bump please")
            
        await asyncio.sleep(1) #Sleeps 2 hours.


@client.event
async def on_message(message):
  print(message.content)
  
  msg = ""
  reaction = ""
  if 'in' == message.content.lower():
    msg = "and **Out**"
    reaction = "<:IAOTLogo:1066784613424431245>"
  elif len([
      x for x in ['niga', "nigger", "nigga", "niger", "nig", "black monkey"]
      if x in message.content.lower()
  ]) > 0:
    msg = ""
    reaction = "👍🏿"
  elif 'ping' == message.content.lower():
    msg = "**pong**"
  elif len([x for x in ['help'] if x in message.content.lower()
            ]) > 0 and "@" not in message.content.lower() and message.author.id != 882241695293526116:
    msg = "<@&1043655353457451038>"
  elif message.channel.id == 1043655461238476913 and message.author.id != 882241695293526116:  #not bot
    if message.author.id == 302050872383242240:
        msg = "bumped"
        global TIMER
        TIMER = 0  
  if msg != "":
    await message.reply(msg)
  if reaction != "":
    await message.add_reaction(reaction)
    




      
client.run("TOKEN HERE")
