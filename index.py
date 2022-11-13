import json
import os
import re

import discord
import requests
import scrapetube
from discord import Client, Intents, Interaction, app_commands
#from forex_python.bitcoin import BtcConverter
from discord.ext import commands, tasks

intents = discord.Intents(messages=True, guilds=True)

bot = commands.Bot(command_prefix='$', intents=intents,allowed_mentions = discord.AllowedMentions(everyone = True))

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
    checkforvideos.start()
    
class FunnyBadge(Client):
    def __init__(self, *, intents: Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self) -> None:
        await self.tree.sync(guild=None)

client = FunnyBadge(intents=Intents.none())

@bot.tree.command()
async def hello(interaction: Interaction):
    """ In and Out Trading """
    print(f"> {interaction.user} used the command.")
    await interaction.response.send_message("\n".join([
      f"Hi **{interaction.user}**, thank you for saying hello to me.",
      "",
      "__**What is In and Out?**__",
      "<:inandoutlogofekete:1014902819079344179> In And Out Trading  is a trading team where we help each other in trading and discuss our ideas about the markets! <:inandoutlogofekete:1014902819079344179>",
      "",
      "<:RoleSupport:1035899393087373392> Our goal is to have a disciplined community, and build relationships <:RoleSupport:1035899393087373392>",
      "",
      f"<:inandoutlogofeher:1014902792411938926>You can find more info about our channels in <#{985238159480746034}> <:inandoutlogofeher:1014902792411938926>"
      
  ]))

@tasks.loop(seconds=10)
async def checkforvideos():
  print("Now Checking!")
  with open("youtubedata.json", "r") as f:
    data=json.load(f)
  #printing here to show

  #checking for all the channels in youtubedata.json file
  for youtube_channel in data:
    #getting youtube channel's url
    channel = f"https://www.youtube.com/channel/{youtube_channel}"
    #getting html of the /videos page
    html = requests.get(channel+"/videos").text
    #getting the latest video's url
    #put this line in try and except block cause it can give error some time if no video is uploaded on the channel
    videos = scrapetube.get_channel("UCRqber9SjCK7TtX_PqV87Pg")
  
    for video in videos:
      latest_video_url ="https://www.youtube.com/watch?v="+video['videoId']
      break

    #checking if url in youtubedata.json file is not equals to latest_video_url
    if not str(data[youtube_channel]["latest_video_url"]) == latest_video_url:

      #changing the latest_video_url
      data[str(youtube_channel)]['latest_video_url'] = latest_video_url

      #dumping the data
      with open("youtubedata.json", "w") as f:
        json.dump(data, f)

      #getting the channel to send the message
      discord_channel_id = data[str(youtube_channel)]['notifying_discord_channel']
      discord_channel = bot.get_channel(int(discord_channel_id))

      #sending the msg in discord channel
      #you can mention any role like this if you want
      msg = f"@everyone **{data[str(youtube_channel)]['nick_name']}** Just Uploaded A Video! Go Check It Out: {latest_video_url}"
      #if you'll send the url discord will automaitacly create embed for it
      #if you don't want to send embed for it then do <{latest_video_url}>

      await discord_channel.send(msg)
      
#creating command to add more youtube accounds data in youtubedata.json file
#you can also use has_role if you don't want to allow everyone to use this command
@bot.command()
@commands.has_role("Youtube")
async def add_youtube_notification_data(ctx, channel_id: str, *, channel_name: str):
  with open("youtubedata.json", "r") as f:
    data = json.load(f)
  
  data[str(channel_id)]={}
  data[str(channel_id)]["channel_name"]=channel_name
  data[str(channel_id)]["latest_video_url"]="none"

  #you can also get discord_channe id from the command 
  #but if the channel is same then you can also do directly
  data[str(channel_id)]["notifying_discord_channel"]="1041300944039718922"

  with open("youtubedata.json", "w") as f:
    json.dump(data, f)
  await ctx.send("Added Your Account Data!")


bot.run("asd")