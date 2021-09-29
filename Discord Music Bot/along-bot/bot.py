# Started project on the 30/08/2021
import discord
from discord.ext import commands, tasks
import os
import json
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq


@tasks.loop(seconds=45.0)
async def findcases():
    myurl = 'https://www.health.nsw.gov.au/Infectious/covid-19/Pages/stats-nsw.aspx'
    uClient = uReq(myurl)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")
    containers = page_soup.findAll("span", {"class":"number"})
    known = containers[6].text
    unknown = containers[10].text

    known = int(known.replace(",",""))
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

client.run('ODgxNzY3OTg0MDgxODAxMjY2.YSxobQ.pM4gGtHM0VQPnprpA-pOIq14jVA')

