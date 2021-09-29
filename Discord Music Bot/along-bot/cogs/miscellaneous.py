import discord
import random
from discord.ext import commands

class Miscellaneous(commands.Cog):

    def __init__(self, client):
        self.client = client

    # set a new prefix for the server
    # @commands.command()
    # async def changeprefix(ctx, prefix):
    #     with open('prefixes.json', 'r') as f:
    #         prefixes = json.load(f)
        
    #     prefixes[str(ctx.guild.id)] = prefix

    #     with open('prefixes.json', 'w') as f:
    #         json.dump(prefixes, f, indent = 4)

    # get ping of command
    @commands.command()
    async def ping(self, message):
        await message.send(f'Current ping is : {round(self.client.latency * 1000)}ms')

    # heads or tails
    @commands.command(aliases = ['chance', 'coin', 'flip'])
    async def coinflip(self, message):
        responses = ['Heads', 'Tails']
        await message.send(random.choice(responses))


    # dice
    @commands.command(aliases = ['roll'])
    async def dice(self, message):
        responses = ['1', '2', '3' , '4', '5', '6']
        await message.send(random.choice(responses))

def setup(client):
    client.add_cog(Miscellaneous(client))
