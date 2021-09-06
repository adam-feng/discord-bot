# Started project on the 30/08/2021
import discord
from discord.ext import commands
import os
import json

def get_prefix(client, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
    
    return prefixes[str(message.guild.id)]


client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
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

client.run('ODgxNzY3OTg0MDgxODAxMjY2.YSxobQ.L3Q3PgSii246Vn9Ybkvda2xqQEQ')

