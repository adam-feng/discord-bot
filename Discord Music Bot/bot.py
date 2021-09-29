# Started project on the 30/08/2021
import discord
from discord.ext import commands, tasks
import os
import json
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import asyncio


total = ""
@tasks.loop(seconds=30.0)
async def findcases():
    global total
    myurl = 'https://www.health.nsw.gov.au/Infectious/covid-19/Pages/stats-nsw.aspx'
    uClient = uReq(myurl)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")
    containers1 = page_soup.findAll("div", {"id":"known"})
    containers2 = page_soup.findAll("div", {"id":"unknown"})
    container1 = containers1[0]
    number1 = container1.findAll("span", {"class":"number"})
    container2 = containers2[0]
    number2 = container2.findAll("span", {"class":"number"})


    known = number1[0].text
    unknown = number2[0].text

    known = int(known)
    unknown = int(unknown.replace(",",""))
    number = known + unknown
    total = str(number)
    # 18
    await client.change_presence(activity=discord.Game("NSW has " + total + " cases"))
    # print(total)



# t1 = threading.Thread(target=findcases)
# t1.start()

def get_prefix(client, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
    
    return prefixes[str(message.guild.id)]


client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
    # await client.change_presence(activity=discord.Game("1"))
    findcases.start()
    print('Along is ready')

# @client.event
# async def on_guild_join(guild):
#     with open('prefixes.json', 'r') as f:
#         prefixes = json.load(f)
    
#     prefixes[str(guild.id)] = '.'

#     with open('prefixes.json', 'w') as f:
#         json.dump(prefixes, f, indent = 4)

# @client.event
# async def on_guild_remove(guild):
#     with open('prefixes.json', 'r') as f:
#         prefixes = json.load(f)
    
#     prefixes.pop(str(guild.id))

#     with open('prefixes.json', 'w') as f:
#         json.dump(prefixes, f, indent = 4)


# @client.command(aliases = ['p'])
# async def play(message, url : str):
#         voiceChannel = discord.utils.get(message.guild.voice_channels, name = 'General')
#         voice =  discord.utils.get(client.voice_clients, guild = message.guild)
#         await message.send('Playing ' + url)
#         await voiceChannel.connect()
        
# client.change_presence(activity=discord.Game('At Your Service'))

# @client.command()
# async def load(ctx, extension):
#     client.load_extension(f'cogs.{extension}')

# @client.command()
# async def unload(ctx, extension):
#     client.unload_extension(f'cogs.{extension}')

# @client.event
# async def on_error(message, error):
#     # if isinstance(error, commands.MissingRequiredArgument):
#     #     await message.send('Please input all required arguments')
#     pass

for i in os.listdir('./cogs'):
    if i.endswith('.py'):
        client.load_extension(f'cogs.{i[:-3]}')

client.run('ODgxNzY3OTg0MDgxODAxMjY2.YSxobQ.3qhFwgkOLqkQ8vOKz5-oiEjbCqE')

