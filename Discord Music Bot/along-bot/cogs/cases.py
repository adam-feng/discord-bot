import discord
import random
from discord.ext import commands
import json
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

class Cases(commands.Cog):

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
    async def cases(self, message):
        myurl = 'https://www.health.nsw.gov.au/Infectious/covid-19/Pages/stats-nsw.aspx'
        uClient = uReq(myurl)
        page_html = uClient.read()
        uClient.close()
        page_soup = soup(page_html, "html.parser")
        # containers1 = page_soup.findAll("div", {"id":"known"})
        # containers2 = page_soup.findAll("div", {"id":"unknown"})
        # container1 = containers1[0]
        # number1 = container1.findAll("span", {"class":"number"})
        # container2 = containers2[0]
        # number2 = container2.findAll("span", {"class":"number"})


        # known = number1[0].text
        # unknown = number2[0].text

        # known = int(known)
        # unknown = int(unknown.replace(",",""))
        # number = known + unknown
        # total = str(number)
        containers = page_soup.findAll("span", {"class":"number"})

        known = containers[6].text
        unknown = containers[10].text

        known = int(known.replace(",",""))
        unknown = int(unknown.replace(",",""))
        number = known + unknown
        total = str(number)
        # 18
        await message.send("NSW has " + total + " cases")


def setup(client):
    client.add_cog(Cases(client))
