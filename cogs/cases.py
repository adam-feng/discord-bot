import discord
import random
from discord.ext import commands
import json
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq


class Cases(commands.Cog):

    def __init__(self, client):
        self.client = client

    # get ping of command
    @commands.command()
    async def cases(self, message):
        myurl = 'https://www.health.nsw.gov.au/Infectious/covid-19/Pages/stats-nsw.aspx'
        uClient = uReq(myurl)
        page_html = uClient.read()
        uClient.close()
        page_soup = soup(page_html, "html.parser")
        containers1 = page_soup.findAll("div", {"id":"known"})
        containers2 = page_soup.findAll("div", {"id":"unknown"})
        container1 = containers1[0]
        container2 = containers2[0]

        spans1 = page_soup.findAll()

        number1 = container1.findAll("span", {"class":"number"})
        number2 = container2.findAll("span", {"class":"number"})



        known = number1[0].text
        unknown = number2[0].text

        known = int(known)
        unknown = int(unknown.replace(",",""))
        total = known + unknown
        total = str(total)

        await message.send("Today NSW had " + total + " cases")



def setup(client):
    client.add_cog(Cases(client))
